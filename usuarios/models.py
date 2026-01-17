from django.db import models
from phonenumber_field.modelfields import PhoneNumberField;

class User(models.Model):
    name_user = models.CharField(max_length=100, unique=True, null=False, blank=False);
    photo_user = models.ImageField(null=False, blank=False);
    fullName_user = models.CharField(max_length=200, null=False, blank=False);
    email_user = models.EmailField(max_length=255, unique=True);
    senha_user = models.CharField(max_length=100, null=False, blank=False);

    def __str__(self):
        return f'{self.name_user}';

class Contact(models.Model):
    topic_con = models.CharField(max_length=100, null=False, blank=False);
    message_con = models.CharField(max_length=2000, null=False, blank=False);
    phone_con = PhoneNumberField(null=False, blank=True);
    user = models.ForeignKey(User, to_field="name_user", related_name='contact_by_username', on_delete=models.PROTECT);
    email_con = models.ForeignKey(User, to_field="email_user", related_name='contact_by_email', on_delete=models.PROTECT);

    def __str__(self): 
        return f'{self.user}';