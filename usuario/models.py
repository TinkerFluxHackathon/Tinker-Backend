from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=30, default='Nome')
    sobrenome = models.CharField(max_length=150, default='Sobrenome')
    username = models.CharField(max_length=50, default='Nome de usuário')
    email = models.EmailField(max_length=254)
    telefone = models.CharField(max_length=15)
    senha = models.CharField(max_length=100)
    foto_perfil = models.ImageField(upload_to='usuario', default='usuario/default.png')
    def __str__(self):
        return f'{self.nome} {self.sobrenome} - {self.username}' 
    
class Comentario(models.Model):
    nome = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    # nota = models.IntegerChoices(1, 5)
    mensagem = models.CharField(max_length=1000)
    # foto_perfil = models.ForeignKey(Usuario, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome