from rest_framework.serializers import ModelSerializer;
from produtos.models.purchase import Purchase;

class PurchaseSerializer(ModelSerializer):
    class Meta:
        model = Purchase;
        fields = '__all__';