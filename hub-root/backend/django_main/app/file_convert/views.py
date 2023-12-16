import requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from core.endpoints import SERVICE_API


@api_view(['POST'])
def file_convert_view(request):
    file = request.data.get('file', False)
    channel_id = request.data.get('channelId', False)

    api_endpoint = SERVICE_API.get('file_convert')

    # print(file)

    if not file or not channel_id:
        return Response(
            {'message': 'file key or channelId key is missing in body'},
            status=status.HTTP_400_BAD_REQUEST
        )
    try:
        # Forward the entire request
        response = requests.post(
            api_endpoint, 
            files={'file': file}, 
            data={'channel_id': channel_id}
        )

        print(response.json())   # it will print the same as `serializer.data`

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
