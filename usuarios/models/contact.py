from django.db import models
from phonenumber_field.modelfields import PhoneNumberField;
from .user import User;

class Contact(models.Model):
    topic = models.CharField(max_length=100, null=False, blank=False);
    message = models.CharField(max_length=2000, null=False, blank=False);
    phone = PhoneNumberField(null=False, blank=True);
    user = models.ForeignKey(User, to_field="name", related_name='contact_by_name', on_delete=models.PROTECT);
    email = models.ForeignKey(User, to_field="email", related_name='contact_by_email', on_delete=models.PROTECT);

    def __str__(self): 
        return f'{self.user}';