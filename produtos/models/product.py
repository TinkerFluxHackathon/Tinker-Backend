from django.db import models;
from uploader.models import Image;

class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False);
    description = models.CharField(max_length=1500, null=False, blank=False);
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False);
    image = models.ForeignKey(Image, related_name='+', null=False, blank=False, on_delete=models.CASCADE, default=None);
    shortDescription = models.CharField(max_length=200, null=False, blank=False);

    def __str__(self):
        return self.name;

    def averageScore(self):
        evaluation = self.evaluation.all();
        if not evaluation.exists():
            return 0;
        return round(sum(a.score for a in evaluation) / evaluation.count());