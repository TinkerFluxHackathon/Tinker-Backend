from django.db import models;
from usuarios.models import User;
from django.core.validators import MinValueValidator, MaxValueValidator;

class Product(models.Model):
    name_pro = models.CharField(max_length=100, null=False, blank=False);
    description_pro = models.CharField(max_length=1500, null=False, blank=False);
    price_pro = models.DecimalField(max_digits=5, decimal_places=2);
    image_pro = models.ImageField(null=False, blank=False);
    shortDescription_pro = models.CharField(max_length=200, null=False, blank=False);
    # score = 
    def __str__(self):
        return f'{self.name_pro}';

    def averageScore(self):
        evaluation = self.evaluation.all();
        if not evaluation.exists():
            return 0;
        return round(sum(a.score for a in evaluation) / evaluation.count());

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
        return f"{self.user}";

class Coupon(models.Model):
    name_cup = models.CharField(max_length=20, null=False, blank=False);
    value_cup = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False);

    def __str__(self):
        return f"{self.name_cup}";

# Finalizar tabela Compras e ItensCarrinho