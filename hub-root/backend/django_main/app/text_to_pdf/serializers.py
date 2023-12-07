from rest_framework import serializers
from .models import TextToPDF


class TextToPDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextToPDF
        fields = '__all__'