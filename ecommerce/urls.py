from django.urls import path
from .views import ClienteApiView, PedidoApiView, ProdutoApiView

app_name = 'ecommerce'

urlpatterns = [
    path('clientes/', ClienteApiView.as_view()),
    path('pedidos/', PedidoApiView.as_view()),
    path('produtos/', ProdutoApiView.as_view()),
]