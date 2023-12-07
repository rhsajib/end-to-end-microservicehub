from celery import shared_task
from .managers import TextToPdfFileManager
from .pspdfkit import convert


@shared_task
def text_to_pdf_convert(file_id):

    object = TextToPdfFileManager(file_id)
    object.change_status_to('in_progress')

    try:
        file_content = object.get_file_content()
        converted_content = convert(file_content)

        object.file(converted_content)
        object.change_status_to('completed')
        
        current_object = object.get_object()
        print(current_object.file_size)

    except:
        object.change_status_to('failed')


    
    
    
