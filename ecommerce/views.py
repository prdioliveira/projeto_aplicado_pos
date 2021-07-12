from .models import Categoria, ItensDoPedido
from .models import Cliente
from rest_framework import generics, viewsets
from .models import Cliente
from .models import Pedido
from .serializers import CategoriaSerializer, ClienteSerializer, ItensDoPedidoSerializer
from .serializers import PedidoSerializer
from .serializers import ProdutoSerializer
from .models import Produto
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound

# Create your views here.
class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer

    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )
    #@api_view(['GET', 'POST'])
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        
        user = self.request.user.email
        queryset = Cliente.objects.filter(email=user)
        email = self.request.query_params.get('email')
        if email is not None:
            queryset = queryset.filter(email=email)
            # exemplo: http://localhost:8000/clientes?email=teste@teste.com
        return queryset

class PedidoViewSet(viewsets.ModelViewSet):
    serializer_class = PedidoSerializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        queryset = Pedido.objects.filter(cliente_id=user.id)
        data_pedido = self.request.query_params.get('data_pedido')
        if data_pedido is not None:
            queryset = queryset.filter(data_pedido=data_pedido)
            # exemplo: http://localhost:8000/pedidos?data_pedido=2021-07-08
        return queryset
    
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )

class ItensViewSet(viewsets.ModelViewSet):
    queryset = ItensDoPedido.objects.all()
    serializer_class = ItensDoPedidoSerializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )