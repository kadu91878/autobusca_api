from django.db import connection
from rest_framework.response import Response
from rest_framework.views import APIView


class VeiculoLocalizacaoAPIView(APIView):
    def get(self, request,):
        with connection.cursor() as cursor:
            cursor.execute(
                """ select * from veiculo v
                    left join localizacao l 
                    on l.id_localizacao = v.id_localizacao 
                """,
            )

            results = cursor.fetchall()

            return Response(results)


class VeiculoLocalizacaoByIdView(APIView):
     def get(self, request, id):
        with connection.cursor() as cursor:
            cursor.execute(
                """ select * from veiculo v
                    left join localizacao l 
                    on l.id_localizacao = v.id_localizacao
                    where v.id_localizacao = %s
                """,
                [id]
            ), 

            results = cursor.fetchall()

            return Response(results)