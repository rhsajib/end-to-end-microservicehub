from django.urls import path
from . import views


app_name = 'chat'
urlpatterns = [
    path('<str:chat_id>/messages/', views.messages_view, name='messages_view'),
]
