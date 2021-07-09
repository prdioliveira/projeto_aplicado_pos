from django.db.models import fields
from  .models import Categoria, ItensDoPedido
from .models import Pedido
from rest_framework import request, serializers
from .models import Cliente
from .models import Pedido
from .models import Produto


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome', 'CPF', 'endereco', 'estado', 'municipio', 'telefone']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome', 'CPF', 'endereco', 'estado', 'municipio', 'telefone', 'email']


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['codigo_produto', 'nome_produto', 'preco_produto', 'quantidade_estoque', 'categoria']


class ItensDoPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensDoPedido
        fields = ['produto', 'quantidade']
        depth = 1


class PedidoSerializer(serializers.ModelSerializer):
    produtos = ItensDoPedidoSerializer(source='itensdopedido_set', many=True, read_only=True)
    class Meta:
        model = Pedido
        fields = ['codigo_pedido', 'cliente', 'data_pedido', 'produtos']
        depth = 1


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['codigo_categoria', 'nome_categoria']
