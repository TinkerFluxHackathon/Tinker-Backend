from rest_framework.serializers import ModelSerializer;
from usuarios.models.contact import Contact;

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact;
        fields = '__all__';