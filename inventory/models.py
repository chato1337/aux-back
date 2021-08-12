from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    stock = models.IntegerField()
    unit = models.CharField(max_length=32)
    is_active = models.CharField(max_length=16, default="active")
