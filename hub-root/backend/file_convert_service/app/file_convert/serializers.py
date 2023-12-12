from rest_framework import serializers
from .models import FileConvert


class FileConvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileConvert
        fields = '__all__'