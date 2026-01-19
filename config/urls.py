
from django.contrib import admin;
from django.urls import include, path;
from rest_framework.routers import DefaultRouter;
from usuarios.views import UserViewSet, ContactViewSet;

router = DefaultRouter();
router.register(r'users', UserViewSet);
router.register(r'contacts', ContactViewSet);

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
