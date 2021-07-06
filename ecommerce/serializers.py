from  .models import Categoria
from .models import Pedido
from rest_framework import serializers
from .models import Cliente
from .models import Pedido
from .models import Produto


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'CPF', 'endereco', 'estado', 'municipio', 'telefone']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'CPF', 'endereco', 'estado', 'municipio', 'telefone', 'email']


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id', 'cliente', 'codigo_pedido', 'data_pedido', 'produtos']



class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'codigo_produto', 'nome_produto', 'preco_produto', 'quantidade_estoque', 'categoria']


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['codigo_categoria', 'nome_categoria']