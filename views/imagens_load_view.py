import os
from django.http import JsonResponse
from django.conf import settings


def carregar_imagens(request, placa):
    # Supondo que as imagens estejam armazenadas em um diretório chamado "imagens" dentro da pasta de mídia do Django
    # Caminho para o diretório das imagens
    diretorio_imagens = os.path.join(settings.MEDIA_ROOT, 'imagens', placa)

    if os.path.isdir(diretorio_imagens):  # Verificar se o diretório existe
        imagens_urls = []
        for nome_arquivo in os.listdir(diretorio_imagens):
            # Verificar se o arquivo é uma imagem
            if nome_arquivo.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                # Construir URL absoluta para a imagem
                url_imagem = request.build_absolute_uri(
                    f"{settings.MEDIA_URL}imagens/{placa}/{nome_arquivo}")

                imagens_urls.append(url_imagem)

        return JsonResponse({'imagens': imagens_urls})
    else:
        return JsonResponse({'erro': f'Nenhuma imagem encontrada para a placa {placa}'}, status=404)
