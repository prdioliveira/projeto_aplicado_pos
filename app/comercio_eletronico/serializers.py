from app.comercio_eletronico.models.categoria_models import Categoria
from app.comercio_eletronico.models.pedido_models import Pedido
from rest_framework import serializers
from app.comercio_eletronico.models.clientes_models import Cliente
from app.comercio_eletronico.models.pedido_models import Pedido
from app.comercio_eletronico.models.produto_models import Produto

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'CPF', 'endereco', 'estado', 'municipio', 'telefone', 'email', 'senha']


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