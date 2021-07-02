from app.comercio_eletronico.models.produto_models import Produto
from django.db import models
from django.db.models.base import Model
from .clientes_models import Cliente

class Pedido(models.Model):
    class Meta:
        db_table = 'pedido'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    codigo_pedido = models.CharField(max_length=20)
    data_pedido = models.DateField()
    produtos = models.ManyToManyField(Produto, related_name='itens_pedido', db_table='itens_pedido')

    def __str__(self):
        return self.codigo_pedido + "-" + self.cliente.nome