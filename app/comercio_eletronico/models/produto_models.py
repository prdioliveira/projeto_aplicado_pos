from django.db import models
from .categoria_models import Categoria

class Produto(models.Model):
    class Meta:
        db_table = 'produto'
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'

    codigo_produto = models.CharField(max_length=15)
    nome_produto = models.CharField(max_length=100)
    preco_produto = models.CharField(max_length=30)
    quantidade_estoque = models.CharField(max_length=15)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)


    def __str__(self):
        return self.nome_produto