from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)

class User(models.Model):
    identifier = models.CharField(max_length=12, null=True, unique=True)
    id_type = models.CharField(max_length=10, default="CC")
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    name = models.CharField(max_length=70, unique=True)
    email = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=24, default="disabled")
    created_at = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=60)
    leverage = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=True)

class Organization(models.Model):
    name = models.CharField(max_length=32, unique=True)
    owner = models.ForeignKey(User, related_name="organization", on_delete=models.CASCADE)
    identifier = models.CharField(max_length=17, unique=True)
    phone = models.PositiveBigIntegerField(unique=True)
    address = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    logo = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return f"{self.name} {self.identifier}"

class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    address = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
