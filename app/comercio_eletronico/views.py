from app.comercio_eletronico.models.categoria_models import Categoria
from inspect import cleandoc
from app.comercio_eletronico.models.clientes_models import Cliente
from django.shortcuts import render
from rest_framework import viewsets
from app.comercio_eletronico.models.clientes_models import Cliente
from app.comercio_eletronico.models.pedido_models import Pedido
from app.comercio_eletronico.serializers import CategoriaSerializer, ClienteSerializer
from app.comercio_eletronico.serializers import PedidoSerializer
from app.comercio_eletronico.serializers import ProdutoSerializer
from app.comercio_eletronico.models.produto_models import Produto

# Create your views here.
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer