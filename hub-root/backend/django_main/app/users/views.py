import bcrypt
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSignUpSerializer
from .managers import PasswordManager


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer

    def perform_create(self, serializer):
        # Hash the user's password using PasswordManager
        password = serializer.validated_data.get('password')
        hashed_password = PasswordManager.hash_password(password)
        serializer.save(password=hashed_password)
    
    # Example usage in a view or another method
    # def some_view_or_method(self, request):
    #     # Get a user from the database, for example
    #     user = User.objects.get(id=1)

    #     # Assuming 'password' is the plain-text password provided by the user
    #     provided_password = 'password'

    #     # Validate the provided password against the hashed password stored in the database using PasswordManager
    #     is_valid_password = PasswordManager.validate_password(provided_password, user.password)

    #     if is_valid_password:
    #         # Password is valid
    #         return Response({"message": "Password is valid"})
    #     else:
    #         # Password is not valid
    #         return Response({"message": "Password is not valid"}, status=status.HTTP_400_BAD_REQUEST)








    # In Django Rest Framework (DRF), the @action decorator is used to define custom actions within a viewset. The detail=True parameter in the @action decorator specifies whether the action is intended to operate on a single instance of the resource (detail view) or on the entire collection of resources (list view).

    # If detail=True, the action is intended to operate on a single instance of the resource. In the context of a viewset, this means that the action is associated with a specific object (e.g., a specific user) identified by its primary key.

    # If detail=False (or not specified), the action is intended to operate on the entire collection of resources. In this case, it is associated with the list view of the resource.

    # @action(detail=True, methods=['patch'], url_path='accept', url_name='sign_up_user')
    # def sign_up_user(self, request, pk=None):
    #     """
    #     Users to sign up for the first time.
    #     """
    #     user = self.get_object()
    #     serialized = UserSignUpSerializer(user, request.data, partial=True)

    #     if serialized.is_valid():
    #         serialized.save()
    #         return Response(
    #             {'message': 'User signed up successfully'},
    #             status=status.HTTP_201_CREATED
    #         )
    









    # def create(self, request, *args, **kwargs):
    #     # Override the create method to hash the password before saving
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)

    #     # Hash the password before saving
    #     hashed_password = request.data.get('hashed_password')  # Assuming 'hashed_password' is the field in the serializer
    #     hashed_password = hash_password_function(hashed_password)  # Replace with your hashing function

    #     serializer.validated_data['hashed_password'] = hashed_password

    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def perform_create(self, serializer):
    #     serializer.save()

    # Additional custom actions can be added here

    # def create(self, request, *args, **kwargs):
    #     # Custom logic for user creation
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def update(self, request, *args, **kwargs):
    #     # Custom logic for user update
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     return Response(serializer.data)

    # def destroy(self, request, *args, **kwargs):
    #     # Custom logic for user deletion
    #     instance = self.get_object()
    #     self.perform_destroy(instance)
    #     return Response(status=status.HTTP_204_NO_CONTENT)
