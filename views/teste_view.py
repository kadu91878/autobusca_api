from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response


class TesteView(APIView):
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
