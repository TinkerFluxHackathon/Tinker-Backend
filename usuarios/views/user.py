from rest_framework.viewsets import ModelViewSet;
from usuarios.models.user import User;
from usuarios.serializers.user import UserSerializer;

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer