from rest_framework.parsers import FormParser,JSONParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import status
from .serializers import FileConvertSerializer
from .tasks import doc_to_pdf_convert

class FileConvertView(CreateAPIView):
    parser_classes = (MultiPartParser,)
    serializer_class = FileConvertSerializer

    ACCEPTED_FILE_TYPE = ['txt', 'doc', 'docx']

    def create(self, request, *args, **kwargs):

        # print(request.data)
        # print(request.data.__dir__())

        # Access the uploaded file
        file = request.data.get('file')

        # this channel_id will be used to connect websocket
        channel_id = request.data.get('channel_id')

        # print(file, file.name, file.size)
        # print('channel_id', channel_id)
        
        # Get all attributes of the file
        # print(file.__dict__)

        file_ext = str(file.name).split('.')[-1]
        # print('file_ext', file_ext)

        if file_ext not in self.ACCEPTED_FILE_TYPE:
            return Response(
                {
                    'message': 'file not valid' , 
                    'acceptable_extensions' : str(self.ACCEPTED_FILE_TYPE),
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if file.size > (20 * 1024 * 1024):
            return Response(
                {
                    'message': 'Max size of file is 20 MB',
                    'file_size': f'Current file size is {file.size / (1024 * 1024)}'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # print(serializer.data)

        file_id = serializer.data.get('id')

        # call celery task to convert file
        doc_to_pdf_convert.delay(file_id, channel_id)

        headers = self.get_success_headers(serializer.data)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

    

    

