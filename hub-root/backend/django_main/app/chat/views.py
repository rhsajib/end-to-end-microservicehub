import requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from core.endpoints import SERVICE_API
from core.config import config




@api_view(['GET','POST'])
def messages_view(request, chat_id, *args, **kwargs):

    endpoint = f'{config.CHAT_SERVICE_BASE_URL}/api/v1/chat/{chat_id}/messages/'

    
    if request.method == 'GET':
        print("********************************************")
        response = requests.get(endpoint)

        print(response.json())   # it will print the same as `serializer.data`

        if response.status_code == 200:
            # Success response from microservice
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Messages get failed'}, status=response.status_code)
        # except:
        #     return Response({'error': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        # # try:
        #     response = requests.get(endpoint)

        #     print(response.json())   # it will print the same as `serializer.data`

        #     if response.status_code == 200:
        #         # Success response from microservice
        #         return Response(response.json(), status=status.HTTP_200_OK)
        #     else:
        #         return Response({'error': 'Messages get failed'}, status=response.status_code)
        # except:
        #     return Response({'error': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'POST':
        try:
            message = request.data.get('message', None)
            response = requests.post(endpoint, data={'message': message})

            print(response.json())   # it will print the same as `serializer.data`

            if response.status_code == 201:
                # Success response from microservice
                return Response(response.json(), status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Messages creation failed'}, status=response.status_code)
        except:
            return Response({'error': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
