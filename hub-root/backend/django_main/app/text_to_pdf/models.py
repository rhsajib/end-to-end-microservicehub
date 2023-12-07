from django.db import models
from core.storage_backends import PublicMediaStorage

class FileSizeField(models.PositiveIntegerField):
    description = 'A custom model field for storing file size in bytes.'

    def get_internal_type(self):
        return 'PositiveIntegerField'

class TextToPDF(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='text-to-pdf/', storage=PublicMediaStorage())
    file_size = FileSizeField(editable=False, null=True, blank=True)

    status = models.CharField(
        max_length=20, 
        default='pending',
        choices=[
            ('pending', 'Pending'),
            ('in_progress', 'In Progress'),
            ('completed', 'Completed'),
            ('failed', 'Failed'),
        ],
    )

    class Meta:
        db_table = 'TextToPDF'
        ordering = ['-uploaded_at']


    def save(self, *args, **kwargs):
        # Calculate and update the file size before saving
        self.file_size = self.file.size
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.file.name


