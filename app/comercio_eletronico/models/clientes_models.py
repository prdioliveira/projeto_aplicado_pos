from django.db import models
import hashlib

class Cliente(models.Model):
    class Meta:
        db_table = 'cliente'
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    nome = models.CharField(max_length=50)
    CPF = models.CharField(max_length=20)
    endereco = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=12)

    def save(self, *args, **kwargs):
        md5 = hashlib.md5()
        md5.update(self.senha.encode())
        self.senha = md5.hexdigest()
        return super(Cliente, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome