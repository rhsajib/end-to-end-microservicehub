from django.urls import path
from .views import FileConvertView

app_name = 'file_convert'

urlpatterns = [
    path('', FileConvertView.as_view(), name='file_convert'),
]