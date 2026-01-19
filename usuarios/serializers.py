from rest_framework.serializers import ModelSerializer;
from .models import User, Contact;

class UserSerializer(ModelSerializer):
    class Meta:
        model = User;
        fields = '__all__';

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact;
        fields = '__all__';