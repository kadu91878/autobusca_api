import os
from django.http import JsonResponse
from django.conf import settings


def carregar_imagens(request):
    diretorio_imagens = os.path.join(settings.MEDIA_ROOT, 'imagens')

    imagens_por_placa = {}

    for placa in os.listdir(diretorio_imagens):
        placa_dir = os.path.join(diretorio_imagens, placa)
        if os.path.isdir(placa_dir):
            imagens_urls = []
            for nome_arquivo in os.listdir(placa_dir):
                if nome_arquivo.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                    url_imagem = request.build_absolute_uri(
                    f"{settings.MEDIA_URL}imagens/{placa}/{nome_arquivo}")
                    imagens_urls.append(url_imagem)
            imagens_por_placa[placa] = imagens_urls

    if imagens_por_placa:
        return JsonResponse(imagens_por_placa)
    else:
        return JsonResponse({'erro': 'Nenhuma imagem encontrada'}, status=404)
