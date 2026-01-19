from rest_framework.viewsets import ModelViewSet;
from .models import User, Contact;
from .serializers import UserSerializer, ContactSerializer;

class UserViewSet(ModelViewSet):
    queryset = User.objects.all();
    serializer_class = UserSerializer;

class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all();
    serializer_class = ContactSerializer;