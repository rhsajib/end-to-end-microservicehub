from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import requests


@api_view(['POST'])
def doc_to_pdf_view(request):
    file = request.data.get('file', False)
    
    # print(file)

    if not file:
        return Response(
            {'message': 'file key is missing in body'},
            status=status.HTTP_400_BAD_REQUEST
        )
    try:
        # Forward the entire request
        response = requests.post('http://127.0.0.1:8002/api/v1/convert/doc-to-pdf', files={'file': file})

        print(response.json())   # it will be the same as `serializer.data`

        if response.status_code == 201:
                # Success response from microservice
                return Response({
                    'message': 'Conversion initiated successfully',
                    'microservice_data': response.json()  # Include any data from microservice
                }, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Conversion failed'}, status=response.status_code)
        
    except:
         return Response({'error': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)



