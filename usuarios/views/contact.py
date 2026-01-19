from rest_framework.viewsets import ModelViewSet;
from usuarios.models.contact import Contact;
from usuarios.serializers.contact import ContactSerializer;

class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer