from rest_framework.viewsets import ModelViewSet;
from produtos.models.purchase import Purchase;
from produtos.serializers.purchase import PurchaseSerializer;

class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all();
    serializer_class = PurchaseSerializer;