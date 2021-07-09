from django.contrib import admin
from .models import Cliente, Produto, Categoria, Pedido, ItensDoPedido


# Register your models here.
admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(ItensDoPedido)