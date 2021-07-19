from  .models import Categoria, ItensDoPedido
from .models import Pedido
from rest_framework import request, serializers
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
        fields = ['id', 'nome', 'CPF', 'endereco', 'estado', 'municipio', 'telefone', 'email', 'password']

class ClienteCPFSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['CPF']
        
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['codigo_categoria', 'nome_categoria']

class ProdutoSerializer(serializers.ModelSerializer):
    nome_categoria = serializers.CharField(source='categoria', read_only=True)
    class Meta:
        model = Produto
        fields = ['codigo_produto', 'nome_produto', 'preco_produto', 'quantidade_estoque', 'categoria', 'nome_categoria']

class ItensDoPedidoSerializer(serializers.ModelSerializer):
    nome_produto = serializers.CharField(source='produto', read_only=True)
    class Meta:
        model = ItensDoPedido
        fields = ['id', 'pedido', 'produto', 'nome_produto', 'quantidade']


class PedidoSerializer(serializers.ModelSerializer):
    cpf_cliente = ClienteCPFSerializer(read_only=True)
    produtos = ItensDoPedidoSerializer(source='itensdopedido_set', many=True, read_only=True)
    class Meta:
        model = Pedido
        fields = ['codigo_pedido', 'cliente', 'cpf_cliente', 'data_pedido', 'produtos']


