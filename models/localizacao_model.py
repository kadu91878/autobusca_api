from django.db import models


class Localizacao(models.Model):
    id_localizacao = models.AutoField(primary_key=True)
    endereco = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(max_length=100, null=True, blank=True)
    pais = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        app_label = 'models'
        db_table = 'localizacao'
        managed = False
