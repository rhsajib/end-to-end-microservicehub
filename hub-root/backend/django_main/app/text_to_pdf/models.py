from django.db import models
from core.storage_backends import PublicMediaStorage

class FileSizeField(models.PositiveIntegerField):
    description = 'A custom model field for storing file size in bytes.'

    def get_internal_type(self):
        return 'PositiveIntegerField'

class TextToPDF(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='text-to-pdf/', storage=PublicMediaStorage())
    # file = models.FileField(upload_to='text-to-pdf/')
    file_size = FileSizeField(editable=False, null=True, blank=True)

    def __str__(self):
        return self.file.name

    def save(self, *args, **kwargs):
        # Calculate and update the file size before saving
        self.file_size = self.file.size
        super().save(*args, **kwargs)
    

# class TextToPDF(models.Model):
#     uploaded_at = models.DateTimeField(auto_now_add=True)
#     file = models.FileField(upload_to='text-to-pdf')


#     @property
#     def file_size(self):
#         return self.file.size

