from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from produtos.views import ProdutoViewSet
from usuario.views import UsuarioViewset, ComentarioViewset

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)
router.register(r'usuario', UsuarioViewset)
router.register(r'comentario', ComentarioViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]