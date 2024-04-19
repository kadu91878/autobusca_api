from rest_framework import serializers
from models.localizacao_model import Localizacao


class LocalizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localizacao
        fields = '__all__'