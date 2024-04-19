from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from views.imagens_view import (ImagemListCreateAPIView,
                                ImagemRetrieveUpdateDestroyAPIView)
from views.teste_view import TesteView
from views.veiculo_localizacao_view import (VeiculoLocalizacaoAPIView,
                                            VeiculoLocalizacaoByIdView)
from views.imagens_load_view import carregar_imagens

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/veiculo-detail', VeiculoLocalizacaoAPIView.as_view(), name='veiculo-detail'),
    path('api/teste', TesteView.as_view(), name='teste'),
    path('api/veiculo-detail/<int:id>', VeiculoLocalizacaoByIdView.as_view(), name='veiculo-detail-id'),
    path('api/imagens', ImagemListCreateAPIView.as_view(), name='imagens'),
    path('api/imagens/<int:pk>', ImagemRetrieveUpdateDestroyAPIView.as_view(), name='imagens-id'),
    path('api/carregar-imagens/<str:placa>/', carregar_imagens, name='imagens_por_placa'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
