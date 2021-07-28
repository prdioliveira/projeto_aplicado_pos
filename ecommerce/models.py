from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .user_managers import CustomUserManager


# Create your models here.
class Cliente(AbstractUser):
    class Meta:
        db_table = 'cliente'
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    username = None
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    nome = models.CharField(max_length=50)
    CPF = models.CharField(max_length=20)
    endereco = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.CPF + ' - ' + self.nome


class Categoria(models.Model):
    class Meta:
        db_table = 'categoria'
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    codigo_categoria = models.CharField(max_length=20, primary_key=True, name='codigo_categoria')
    nome_categoria = models.CharField(max_length=30)

    def __str__(self):
        return self.nome_categoria


class Produto(models.Model):
    class Meta:
        db_table = 'produto'
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'

    codigo_produto = models.CharField(max_length=20, primary_key=True, name='codigo_produto')
    nome_produto = models.CharField(max_length=100)
    preco_produto = models.CharField(max_length=30)
    quantidade_estoque = models.CharField(max_length=15)
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT, error_messages ={"unique":"The Geeks Field you enetered is not unique."})

    def __str__(self):
        return self.nome_produto


class ItensDoPedido(models.Model):
    class Meta:
        db_table = 'itens_pedido'
        verbose_name = 'itens_pedido'
        verbose_name_plural = 'itens_pedidos'

    produto = models.ForeignKey('Produto', on_delete=models.RESTRICT, error_messages ={"unique":"The Geeks Field you enetered is not unique."})
    pedido = models.ForeignKey('Pedido', on_delete=models.RESTRICT, error_messages ={"unique":"The Geeks Field you enetered is not unique."})
    quantidade = models.CharField(max_length=10)

    def __str__(self):
        return self.quantidade + "Teste"


class Pedido(models.Model):
    class Meta:
        db_table = 'pedido'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'

    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT, related_name='cliente', error_messages ={"unique":"The Geeks Field you enetered is not unique."})
    codigo_pedido = models.CharField(max_length=20, primary_key=True, name='codigo_pedido')
    data_pedido = models.DateField()
    produtos = models.ManyToManyField(Produto, through=ItensDoPedido)

    def __str__(self):
        return self.codigo_pedido + "-" + self.cliente.nome
