from phonenumber_field.modelfields import PhoneNumberField
from django.db import models;

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(max_length=2000)

    def __str__(self):
        return self.nome
        return self.preco
        return self.descricao
    

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    telefone = PhoneNumberField()
    def __str__(self):
        return self.nome
        return self.email