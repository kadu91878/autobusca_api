from rest_framework import serializers
from models.localizacao_model import Localizacao
from models.veiculos_model import Veiculo

class VeiculoComLocalizacaoSerializer(serializers.Serializer):
    placa_carro = serializers.CharField(max_length=20)
    nome_veiculo = serializers.CharField(max_length=100, allow_null=True)
    modelo = serializers.CharField(max_length=50, allow_null=True)
    preco = serializers.DecimalField(max_digits=10, decimal_places=2, allow_null=True)
    quilometragem = serializers.DecimalField(max_digits=10, decimal_places=2, allow_null=True)
    tipo_cambio = serializers.CharField(max_length=20, allow_null=True)
    ano_modelo = serializers.IntegerField(allow_null=True)
    cor = serializers.CharField(max_length=30, allow_null=True)
    tipo_combustivel = serializers.CharField(max_length=20, allow_null=True)
    categoria = serializers.CharField(max_length=30, allow_null=True)
    quantidade_portas = serializers.IntegerField(allow_null=True)
    
    endereco = serializers.CharField(max_length=255, allow_null=True)
    cidade = serializers.CharField(max_length=100, allow_null=True)
    estado = serializers.CharField(max_length=100, allow_null=True)
    pais = serializers.CharField(max_length=100, allow_null=True)

    def to_representation(self, instance):
        representation = {
            'placa_carro': instance[0],
            'nome_veiculo': instance[1],
            'modelo': instance[2],
            'preco': instance[3],
            'quilometragem': instance[4],
            'tipo_cambio': instance[5],
            'ano_modelo': instance[6],
            'cor': instance[7],
            'tipo_combustivel': instance[8],
            'categoria': instance[9],
            'quantidade_portas': instance[10],
            'endereco': instance[11],
            'cidade': instance[12],
            'estado': instance[13],
            'pais': instance[14],
        }
        return representation