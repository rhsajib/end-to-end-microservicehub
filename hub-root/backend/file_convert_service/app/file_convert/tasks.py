from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .managers import FileConvertManager
from .pspdfkit import get_converted_content
import time


@shared_task
def doc_to_pdf_convert(file_id, channel_id):

    channel_layer = get_channel_layer()
    room_group_name = channel_id   

    object = FileConvertManager(file_id)

    try:
        # Send file status to WebSocket
        # we do not need to establish distinct connnection with channel layer
        # we can just subscribe or publish the layer
        async_to_sync(channel_layer.group_send)(
            room_group_name,
            {"type": "update_status",
             "status": "In progress..."}
        )
        # time.sleep(10)
        file_content = object.get_file_content()

        # use third party api to convert file
        converted_content = get_converted_content(file_content)

        object.file(converted_content)
        object.change_status_to('completed')
        object.save()

        # Notify the group that the conversion is completed
        async_to_sync(channel_layer.group_send)(
            room_group_name,
            {"type": "update_status", "status": "Completed"}
        )

    except Exception as e:
        object.change_status_to('failed')
        object.save()

        # Notify the group that the conversion has failed
        async_to_sync(channel_layer.group_send)(
            room_group_name,
            {"type": "update_status", "status": "Failed"}
        )
