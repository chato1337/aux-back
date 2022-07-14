from turtle import ondrag
from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)

class User(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=64)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    address = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now=True)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=60)
    leverage = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=True)
