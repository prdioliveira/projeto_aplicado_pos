from rest_framework.views import APIView
from .models import Categoria, ItensDoPedido
from .models import Cliente
from rest_framework import viewsets
from .models import Cliente
from .models import Pedido
from .serializers import CategoriaSerializer, ClienteSerializer, ItensDoPedidoSerializer
from .serializers import PedidoSerializer
from .serializers import ProdutoSerializer
from .models import Produto
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer  
    authentication_classes = (TokenAuthentication,) 
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        if self.request.auth is None:
            raise PermissionDenied({"details": "As credenciais de autenticação não foram fornecidas."})

        user = self.request.user.email
        queryset = Cliente.objects.filter(email=user)
        email = self.request.query_params.get('email')

        if email is not None:
            queryset = queryset.filter(email=email)
            # exemplo: http://localhost:8000/clientes?email=teste@teste.com
        return queryset


class ClienteApiView(APIView):
    def get(self, request):
        user = self.request.user.email
        clientes = Cliente.objects.filter(email=user)
        serializer = ClienteSerializer(clientes, many=True)

        return Response(serializer.data)


class PedidoViewSet(viewsets.ModelViewSet):
    serializer_class = PedidoSerializer
    authentication_classes = (TokenAuthentication,) 
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        if self.request.auth is None:
            raise PermissionDenied({"details": "As credenciais de autenticação não foram fornecidas."})

        user = self.request.user

        # if not user.nome and not user.CPF:
        #     raise PermissionDenied({"details": "Favor completar o perfil de usuário."})

        queryset = Pedido.objects.filter(cliente_id=user.id)
        data_pedido = self.request.query_params.get('data_pedido')
            
        if data_pedido is not None:
            queryset = queryset.filter(data_pedido=data_pedido)
            # exemplo: http://localhost:8000/pedidos?data_pedido=2021-07-08
        return queryset


class PedidoApiView(APIView):
    def get(self, request):
        user = self.request.user
        pedidos = Pedido.objects.filter(cliente_id=user.id)
        serializer = PedidoSerializer(pedidos, many=True)

        return Response({"pedidos": serializer.data})

    def post(self, request):
        serializer = PedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProdutoApiView(APIView):
    def get(self, request):
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response({"produtos": serializer.data})


class ProdutoViewSet(viewsets.ModelViewSet):
    serializer_class = ProdutoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    #http://localhost:8000/produtos?nome_produto=Sabão
    def get_queryset(self):
        queryset = Produto.objects.all()
        nome_produto = self.request.query_params.get('nome_produto')
        if nome_produto is not None:
            queryset = queryset.filter(nome_produto__contains=nome_produto)
        return queryset


class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    authentication_classes = (TokenAuthentication,) 
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        queryset = Categoria.objects.all()
        nome_categoria = self.request.query_params.get('nome_categoria')

        if nome_categoria is not None:
            queryset = queryset.filter(nome_categoria__contains=nome_categoria)
        return queryset


class ItensViewSet(viewsets.ModelViewSet):    
    serializer_class = ItensDoPedidoSerializer
    authentication_classes = (TokenAuthentication,) 
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        if self.request.auth is None:
            raise PermissionDenied({"details": "As credenciais de autenticação não foram fornecidas."})

        user = self.request.user

        # if not user.nome and not user.CPF:
        #     raise PermissionDenied({"details": "Favor completar o perfil de usuário."})

        codigo_pedido = Pedido.objects.get(cliente_id=user.id).codigo_pedido

        print('----------------', codigo_pedido)
        queryset = ItensDoPedido.objects.filter(pedido_id=codigo_pedido)
        return queryset