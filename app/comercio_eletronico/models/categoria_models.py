from django.db import models

class Categoria(models.Model):
    class Meta:
        db_table = 'categoria'
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    codigo_categoria = models.CharField(max_length=15)
    nome_categoria = models.CharField(max_length=30)

    def __str__(self):
        return self.nome_categoria