from io import BytesIO
from .models import FileConvert
from django.core.files.base import ContentFile

class FileConvertManager:
    def __init__(self, id):
        self.object = FileConvert.objects.get(pk=id)
        self.object_name = 'result'
    
        if self.object.file.name:
            name = self.object.file.name
            self.object_name =  name.split('/')[-1].split('.')[0]

    def get_object(self):
        return self.object

    def get_file_content(self):
        content = BytesIO(self.object.file.read())
        return content
    
    def change_status_to(self, status):
        self.object.status = status

    def _change_file_size(self):
        new_file_size = self.object.file.size
        self.object.file_size = new_file_size

    def file(self, content):
        file_content = ContentFile(content)
        self.object.file.save(f'{self.object_name}.pdf', file_content)
        self._change_file_size()       
        
    def save(self):
        self.object.save()

        
