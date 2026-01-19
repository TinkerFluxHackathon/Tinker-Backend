from rest_framework.viewsets import ModelViewSet;
from .models import Product, Evaluation, Coupon, Purchase;
from .serializers import ProductSerializer, EvaluationSerializer, CouponSerializer, PurchaseSerializer;

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all();
    serializer_class = ProductSerializer;

class EvaluationViewSet(ModelViewSet):
    queryset = Evaluation.objects.all();
    serializer_class = EvaluationSerializer;

class CouponViewSet(ModelViewSet):
    queryset = Coupon.objects.all();
    serializer_class = CouponSerializer;

class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all();
    serializer_class = PurchaseSerializer;