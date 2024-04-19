from django.db import models

class Imagem(models.Model):
    id_imagem = models.AutoField(primary_key=True)
    placa_carro = models.CharField(max_length=20, null=True)
    nome_arquivo = models.CharField(max_length=255, null=True)
    # tipo = models.CharField(max_length=10, null=True)

    class Meta:
        db_table = 'imagens'
        app_label = 'models'
        managed = False
