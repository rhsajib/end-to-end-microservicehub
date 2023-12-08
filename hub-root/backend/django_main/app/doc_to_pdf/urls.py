from django.urls import path
from .views import doc_to_pdf_view

app_name = 'doc_to_pdf'

urlpatterns = [
    path('', doc_to_pdf_view, name='doc_to_pdf_view'),
]