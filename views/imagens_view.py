from rest_framework import generics

from django.db import connection
from rest_framework.response import Response
from rest_framework.views import APIView

from models.imagens_model import Imagem
from serializers.imagens_serializer import ImagemSerializer


class ImagemListCreateAPIView(generics.ListCreateAPIView):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer


class ImagemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer


class ListaImagemView(APIView):
    def get(self, request,):
        with connection.cursor() as cursor:
            cursor.execute(
                """select distinct i.placa_carro  from imagens i 
                """,
            )

            results = cursor.fetchall()

            return Response(results)
