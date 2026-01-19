from django.db import models
from uploader.models import Image;


class User(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False);
    photo = models.ForeignKey(Image, related_name='+', null=False, blank=False, on_delete=models.CASCADE, default=None);
    fullName = models.CharField(max_length=200, null=False, blank=False);
    email = models.EmailField(max_length=255, null=False, blank=False, unique=True);
    senha = models.CharField(max_length=100, null=False, blank=False);

    def __str__(self):
        return f'{self.name}';
