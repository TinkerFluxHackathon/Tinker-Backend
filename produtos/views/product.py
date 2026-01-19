from rest_framework.viewsets import ModelViewSet;
from produtos.models.product import Product;
from produtos.serializers.product import ProductSerializer;

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all();
    serializer_class = ProductSerializer;
