from django.urls import path
from .views import TextToPDFView

app_name = 'text_to_pdf'

urlpatterns = [
    path('', TextToPDFView.as_view(), name='file-upload'),
]