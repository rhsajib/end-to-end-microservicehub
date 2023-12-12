from django.urls import path
from .views import file_convert_view

app_name = 'file_convert'

urlpatterns = [
    path('', file_convert_view, name='file_convert'),
]