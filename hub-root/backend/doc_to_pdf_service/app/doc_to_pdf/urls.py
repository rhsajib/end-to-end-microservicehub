from django.urls import path
from .views import DocToPDFView

app_name = 'doc_to_pdf'

urlpatterns = [
    path('', DocToPDFView.as_view(), name='doc_to_pdf'),
]