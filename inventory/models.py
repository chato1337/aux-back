from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)

class Supplier(models.Model):
    name = models.CharField(max_length=30)
    identifier = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=30)
    other_details = models.CharField(max_length=150, null=True)

class Product(models.Model):
    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=300)
    price = models.FloatField()
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    expiration_date = models.DateField()
    entry_date = models.DateTimeField(auto_now=True)
    stock = models.IntegerField()
    unit = models.CharField(max_length=32)
    is_active = models.CharField(max_length=16, default="active")
