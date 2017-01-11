from __future__ import unicode_literals
from django.db import models
from django.utils.timezone import now
# Create your models here.

class ProductManager(models.Manager):
    def update(self, id, from_info):
        product = Product.objects.get(id = id)
        product.name = from_info['name']
        product.description = from_info['description']
        product.price = from_info['price']
        product.save()
        
class Product(models.Model):
    name = models.CharField(max_length =45)
    description = models.CharField(max_length =200)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProductManager()
