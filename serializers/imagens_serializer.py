from rest_framework import serializers
from models.imagens_model import Imagem

class ImagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = '__all__'