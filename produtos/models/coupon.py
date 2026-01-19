from django.db import models;

class Coupon(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False);
    value = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=False, blank=False);

    def __str__(self):
        return self.name_cup;