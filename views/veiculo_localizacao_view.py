from django.db import connection
from rest_framework.response import Response
from rest_framework.views import APIView

from serializers.veiculo_localizacao_serializer import \
    VeiculoComLocalizacaoSerializer


class VeiculoLocalizacaoAPIView(APIView):
    def get(self, request,):
        with connection.cursor() as cursor:
            cursor.execute(
                """ select v.placa_carro,v.nome_veiculo, v.modelo,
v.preco, v.quilometragem, v.tipo_cambio,
v.ano_modelo, v.cor, v.tipo_combustivel,
v.categoria, v.quantidade_portas,
l.endereco, l.cidade, l.estado, l.pais 
from veiculo v 
left join localizacao l 
on l.id_localizacao = v.id_localizacao 
                    on l.id_localizacao = v.id_localizacao 
                """,
            )

            results = cursor.fetchall()

            serializer = VeiculoComLocalizacaoSerializer(results, many=True)
            return Response(serializer.data)


class VeiculoLocalizacaoByIdView(APIView):
    def get(self, request, id):
        with connection.cursor() as cursor:
            cursor.execute(
                """ select v.placa_carro,v.nome_veiculo, v.modelo,
v.preco, v.quilometragem, v.tipo_cambio,
v.ano_modelo, v.cor, v.tipo_combustivel,
v.categoria, v.quantidade_portas,
l.endereco, l.cidade, l.estado, l.pais 
from veiculo v 
left join localizacao l 
on l.id_localizacao = v.id_localizacao 
                    where v.id_localizacao = %s
                """,
                [id]
            ),

            results = cursor.fetchall()

            serializer = VeiculoComLocalizacaoSerializer(results, many=True)
            return Response(serializer.data)


class VeiculoLocalizacaoMainAPIView(APIView):
    def get(self, request,):
        with connection.cursor() as cursor:
            cursor.execute(
                """ select v.placa_carro,v.nome_veiculo, v.modelo,
v.preco, v.quilometragem, v.tipo_cambio,
v.ano_modelo, v.cor, v.tipo_combustivel,
v.categoria, v.quantidade_portas,
l.endereco, l.cidade, l.estado, l.pais 
from veiculo v 
left join localizacao l 
on l.id_localizacao = v.id_localizacao 
                    limit 5 
                """,
            )

            results = cursor.fetchall()

            serializer = VeiculoComLocalizacaoSerializer(results, many=True)
            return Response(serializer.data)
