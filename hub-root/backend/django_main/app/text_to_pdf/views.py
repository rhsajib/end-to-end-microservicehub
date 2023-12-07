from rest_framework.parsers import FormParser,JSONParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework import status
from .models import TextToPDF
from .serializers import TextToPDFSerializer
from .tasks import text_to_pdf_convert

class TextToPDFView(CreateAPIView):
    parser_classes = (MultiPartParser,)
    serializer_class = TextToPDFSerializer

    def create(self, request, *args, **kwargs):

        # Access the uploaded file
        file = request.data.get('file', False)
        if not file:
            return Response(
                {'message': 'file key is missing in body'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        
        # print(file)
        # print(file.name)
        # print(file.size)

        # Check if a file was uploaded
        if file:
            # Get all attributes of the file
            file_attributes = file.__dict__
            print(file_attributes)


        # perform checks
        file_ext = str(file.name).split('.')[-1]
        # print('file_ext', file_ext)
        if file_ext not in ['txt', 'doc', 'docx']:
            return Response(
                {
                    'message': 'file not valid' , 
                    'acceptable_extensions' : '.txt, .doc, .docx',
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if file.size > 20 * 1024 * 1024:
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
        print(serializer.data)

        file_id = serializer.data.get('id')

        text_to_pdf_convert.delay(file_id)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

    

    

