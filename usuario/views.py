from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from .models import Usuario, Comentario
from .serializers import UsuarioSerializer, ComentarioSerializer

class UsuarioViewset(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ComentarioViewset(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer