from django.contrib import admin

from .models import Product, Evaluation, Coupon, Purchase;

admin.site.register(Product);
admin.site.register(Evaluation);
admin.site.register(Coupon);
admin.site.register(Purchase);