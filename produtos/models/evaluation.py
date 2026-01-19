from django.db import models;
from usuarios.models.user import User;
from .product import Product;
from django.core.validators import MinValueValidator, MaxValueValidator;

class Score(models.IntegerChoices):
    Zero = 0, '0';
    One = 1, '1';
    Two = 2, '2';
    Three = 3, '3';
    Four = 4, '4';
    Five = 5, '5';

class Evaluation(models.Model):
    evaluation = models.ForeignKey(Product, related_name='product_by_evaluation', on_delete=models.PROTECT);
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=False, blank=False);   
    message = models.CharField(max_length=1000, null=False, blank=False);
    image = models.ImageField(null=False, blank=False);
    product = models.ForeignKey(Product, on_delete=models.PROTECT);
    user = models.ForeignKey(User, on_delete=models.PROTECT);

    def __str__(self):
        return self.user;
