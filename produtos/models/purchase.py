from django.db import models;
from usuarios.models.user import User;

class Purchase(models.Model):
    qrCode = models.CharField(max_length=200, null=False, blank=False);
    user = models.ForeignKey(User, on_delete=models.PROTECT);
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=False, blank=False);

    def __str__(self):
        return self.user;

