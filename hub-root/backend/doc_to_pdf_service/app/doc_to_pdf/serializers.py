from rest_framework import serializers
from .models import DocToPDF


class DocToPDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocToPDF
        fields = '__all__'