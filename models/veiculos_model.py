from django.db import models
from models.localizacao_model import Localizacao

class Veiculo(models.Model):
    placa_carro = models.CharField(max_length=20, primary_key=True)
    nome_veiculo = models.CharField(max_length=100, null=True, blank=True)
    modelo = models.CharField(max_length=50, null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quilometragem = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tipo_cambio = models.CharField(max_length=20, null=True, blank=True)
    ano_modelo = models.IntegerField(null=True, blank=True)
    cor = models.CharField(max_length=30, null=True, blank=True)
    tipo_combustivel = models.CharField(max_length=20, null=True, blank=True)
    categoria = models.CharField(max_length=30, null=True, blank=True)
    quantidade_portas = models.IntegerField(null=True, blank=True)
    id_localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)
    
    class Meta:
        app_label = 'models'
        db_table = 'veiculo'
        managed = False
        
    