from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from .models import Produto
from .serializers import ProdutoSerializer

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer