from django.db import models

from inventory.models import Product

# Create your models here.
class DinnerProduct(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    price = models.FloatField()
    category = models.CharField(max_length=40)
    image = models.CharField(max_length=300)

class DinnerOrder(models.Model):
    products = models.ManyToManyField(DinnerProduct, blank=True)
    owner = models.CharField(max_length=45)
    tips = models.IntegerField()
    subtotal = models.FloatField()

class Table(models.Model):
    number = models.IntegerField()
    orders = models.ManyToManyField(DinnerOrder, blank=True)
    customers = models.IntegerField()
    total = models.FloatField()
    isActive = models.BooleanField(default=True)

