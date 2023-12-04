from django.db import models

# Create your models here.

class TextToPDF(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField()