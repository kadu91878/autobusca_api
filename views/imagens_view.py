from rest_framework import generics

from models.imagens_model import Imagem
from serializers.imagens_serializer import ImagemSerializer


class ImagemListCreateAPIView(generics.ListCreateAPIView):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer
    
class ImagemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer
