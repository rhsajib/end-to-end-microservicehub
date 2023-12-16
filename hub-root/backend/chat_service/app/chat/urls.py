from django.urls import include, path
from .views import MessageViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'messages', MessageViewSet, basename='messages')

app_name = 'chat'
urlpatterns = [
    path('<str:chat_id>/', include(router.urls)),
]
