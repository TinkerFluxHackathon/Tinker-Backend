from django.db import models
from phonenumber_field.modelfields import PhoneNumberField;

class User(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False);
    photo = models.ImageField(null=False, blank=False);
    fullName = models.CharField(max_length=200, null=False, blank=False);
    email = models.EmailField(max_length=255, null=False, blank=False, unique=True);
    senha = models.CharField(max_length=100, null=False, blank=False);

    def __str__(self):
        return f'{self.name}';

class Contact(models.Model):
    topic = models.CharField(max_length=100, null=False, blank=False);
    message = models.CharField(max_length=2000, null=False, blank=False);
    phone = PhoneNumberField(null=False, blank=True);
    user = models.ForeignKey(User, to_field="name", related_name='contact_by_username', on_delete=models.PROTECT);
    email = models.ForeignKey(User, to_field="email", related_name='contact_by_email', on_delete=models.PROTECT);

    def __str__(self): 
        return f'{self.user}';

# Erro de no pdm run python manage.py migrate