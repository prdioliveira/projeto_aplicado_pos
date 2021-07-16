from django.http.response import Http404
from rest_framework.views import APIView
from .models import Categoria, ItensDoPedido
from .models import Cliente
from rest_framework import generics, request, serializers, viewsets
from .models import Cliente
from .models import Pedido
from .serializers import CategoriaSerializer, ClienteSerializer, ItensDoPedidoSerializer
from .serializers import PedidoSerializer
from .serializers import ProdutoSerializer
from .models import Produto
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer  
    authentication_classes = (TokenAuthentication, SessionAuthentication) 

    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )
    #@api_view(['GET', 'POST'])
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        if self.request.auth is None:
            raise PermissionDenied({"details":"Credenciais de acesso não fornecidas"})

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
    authentication_classes = (TokenAuthentication, SessionAuthentication) 
    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        if self.request.auth is None:
            raise PermissionDenied({"details":"Credenciais de acesso não fornecidas"})

        user = self.request.user
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
    
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, SessionAuthentication) 


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication) 
    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )

class ItensViewSet(viewsets.ModelViewSet):
    queryset = ItensDoPedido.objects.all()
    serializer_class = ItensDoPedidoSerializer
    #authentication_classes = [SessionAuthentication]
    authentication_classes = (TokenAuthentication, SessionAuthentication) 
    #permission_classes = (IsAuthenticated, )