from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

"""
GET /users/: List all users
POST /users/: Create a new user
GET /users/{pk}/: Retrieve details of a specific user
PUT /users/{pk}/: Update details of a specific user
PATCH /users/{pk}/: Partial update of a specific user
DELETE /users/{pk}/: Delete a specific user
PATCH /users/{pk}/accept/: Custom action for user sign-up
"""

app_name = 'users'
urlpatterns = [
    path('', include(router.urls)),
]
