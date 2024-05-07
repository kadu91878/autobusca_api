from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from views.imagens_load_view import carregar_imagens
from views.imagens_view import (ImagemListCreateAPIView,
                                ImagemRetrieveUpdateDestroyAPIView,
                                ListaImagemView)
from views.teste_view import TesteView
from views.veiculo_localizacao_view import (VeiculoLocalizacaoAPIView,
                                            VeiculoLocalizacaoByIdView,
                                            VeiculoLocalizacaoMainAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/veiculo-detail', VeiculoLocalizacaoAPIView.as_view(),
         name='veiculo-detail'),
    path('api/teste', TesteView.as_view(), name='teste'),
    path('api/veiculo-detail/<str:id>',
         VeiculoLocalizacaoByIdView.as_view(), name='veiculo-detail-id'),
    path('api/imagens', ImagemListCreateAPIView.as_view(), name='imagens'),
    path('api/imagens/<int:pk>',
         ImagemRetrieveUpdateDestroyAPIView.as_view(), name='imagens-id'),
    path('api/carregar-imagens/',
         carregar_imagens, name='imagens_por_placa'),
    path('api/listar-placas', ListaImagemView.as_view(), name='listar-placas'),
    path('api/veiculo-detail-paginado', VeiculoLocalizacaoMainAPIView.as_view(), name='veiculo-detail-paginado'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
