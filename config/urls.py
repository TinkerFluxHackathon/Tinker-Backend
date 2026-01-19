from django.conf import settings;
from django.conf.urls.static import static;
from django.contrib import admin;
from django.urls import include, path;
from uploader.router import router as uploader_router;
from rest_framework.routers import DefaultRouter;
from usuarios.views import UserViewSet, ContactViewSet;
from produtos.views import ProductViewSet, EvaluationViewSet, CouponViewSet, PurchaseViewSet;
from user.router import router as usuario_router;

# JWT

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter();

# Users

router.register(r'users', UserViewSet);
router.register(r'contacts', ContactViewSet);

# Products

router.register(r"products", ProductViewSet);
router.register(r"evaluations", EvaluationViewSet);
router.register(r"coupons", CouponViewSet);
router.register(r"purchases", PurchaseViewSet);

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh', TokenRefreshView.as_view(), name="token_refresh"),
    path('api/', include(usuario_router.urls)),
    path('api/media/', include(uploader_router.urls)),
];

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT);
