from rest_framework.viewsets import ModelViewSet;
from produtos.models.coupon import Coupon;
from produtos.serializers.coupon import CouponSerializer;

class CouponViewSet(ModelViewSet):
    queryset = Coupon.objects.all();
    serializer_class = CouponSerializer;