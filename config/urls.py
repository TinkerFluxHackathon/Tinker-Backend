from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from produtos.views import ProdutoViewSet
from usuario.views import UsuarioViewset, ComentarioViewset
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)
router.register(r'usuario', UsuarioViewset)
router.register(r'comentario', ComentarioViewset)

urlpatterns = [
    path('', RedirectView.as_view(url='api/', permanent=False)),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)