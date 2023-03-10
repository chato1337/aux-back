from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=30)
    identifier = models.CharField(max_length=30, unique=True)
    phone = models.CharField(max_length=12, unique=True)
    email = models.CharField(max_length=30, unique=True)
    other_details = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.CASCADE)
    code = models.CharField(max_length=120, null=True, unique=True)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=300)
    price = models.FloatField()
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    expiration_date = models.DateField()
    entry_date = models.DateField(auto_now=True)
    stock = models.IntegerField()
    unit = models.CharField(max_length=32)
    is_active = models.CharField(max_length=16, default="active")
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
