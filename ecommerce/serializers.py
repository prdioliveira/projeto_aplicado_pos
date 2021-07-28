from  .models import Categoria, ItensDoPedido
from .models import Pedido
from rest_framework import serializers
from .models import Cliente
from .models import Pedido
from .models import Produto


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'id',
            'nome',
            'CPF',
            'endereco',
            'estado',
            'municipio',
            'telefone'
        ]


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'id',
            'nome',
            'CPF',
            'endereco',
            'estado',
            'municipio',
            'telefone',
            'email',
            'password'
        ]


class ClienteCPFSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['CPF']


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = [
            'codigo_categoria',
            'nome_categoria'
        ]


class ProdutoSerializer(serializers.ModelSerializer):
    nome_categoria = serializers.CharField(source='categoria', read_only=True)
    class Meta:
        model = Produto
        fields = [
            'codigo_produto',
            'nome_produto',
            'preco_produto',
            'quantidade_estoque',
            'categoria',
            'nome_categoria'
        ]


class ItensDoPedidoSerializer(serializers.ModelSerializer):
    nome_produto = serializers.CharField(source='produto', read_only=True)
    preco_produto = serializers.SerializerMethodField(read_only=True)
    preco_total_produto = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ItensDoPedido
        fields = [
            'id',
            'pedido',
            'produto',
            'nome_produto',
            'preco_produto',
            'quantidade',
            'preco_total_produto'
        ]
    
    # retorna o preço do produto de acordo com a FK
    def get_preco_produto(self, obj):
        return Produto.objects.get(pk=obj.produto_id).preco_produto
    
    # Retornar o preco total do item no pedido de acordo com a quantidade e a FK
    def get_preco_total_produto(self, obj):
        quantidade = float(ItensDoPedido.objects.get(pk=obj.id).quantidade)
        preco_unitario = float(Produto.objects.get(pk=obj.produto_id).preco_produto)
        return quantidade * preco_unitario


class PedidoSerializer(serializers.ModelSerializer):
    produtos = ItensDoPedidoSerializer(source='itensdopedido_set', many=True, read_only=True)
    nome_cliente = serializers.CharField(source='cliente', read_only=True)
    class Meta:
        model = Pedido
        fields = [
            'codigo_pedido',
            'cliente',
            'nome_cliente',
            'data_pedido',
            'produtos'
        ]
