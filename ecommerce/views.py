from .models import Categoria
from .models import Cliente
from rest_framework import generics, viewsets
from .models import Cliente
from .models import Pedido
from .serializers import CategoriaSerializer, ClienteSerializer
from .serializers import PedidoSerializer
from .serializers import ProdutoSerializer
from .models import Produto
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

# Create your views here.
class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer

    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Cliente.objects.all()
        email = self.request.query_params.get('email')
        if email is not None:
            print('-------------------->', email)
            queryset = queryset.filter(email=email)
            print('++++++++++++++++', queryset)
        return queryset


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )