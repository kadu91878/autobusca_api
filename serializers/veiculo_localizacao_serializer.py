from rest_framework import serializers
from models.localizacao_model import Localizacao
from models.veiculos_model import Veiculo

class VeiculoLocalizacaoSerializer(serializers.Serializer):
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
    id_localizacao = serializers.IntegerField()
    endereco = serializers.CharField(max_length=255, allow_null=True)
    cidade = serializers.CharField(max_length=100, allow_null=True)
    estado = serializers.CharField(max_length=100, allow_null=True)
    pais = serializers.CharField(max_length=100, allow_null=True)

    def to_representation(self, instance):
        # Construa a representação personalizada dos dados
        representation = {
            'placa_carro': instance.placa_carro,
            'nome_veiculo': instance.nome_veiculo,
            'modelo': instance.modelo,
            'preco': instance.preco,
            'quilometragem': instance.quilometragem,
            'tipo_cambio': instance.tipo_cambio,
            'ano_modelo': instance.ano_modelo,
            'cor': instance.cor,
            'tipo_combustivel': instance.tipo_combustivel,
            'categoria': instance.categoria,
            'quantidade_portas': instance.quantidade_portas,
            'id_localizacao': instance.id_localizacao,
            'endereco': instance.endereco,
            'cidade': instance.cidade,
            'estado': instance.estado,
            'pais': instance.pais,
        }
        return representation