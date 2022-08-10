from django.db import models
from inventory.models import Product
from user.models import Customer, Staff

# Create your models here.
class Invoice(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    seller = models.ForeignKey(Staff, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=30)
    total = models.FloatField()

    def __str__(self) -> str:
        return self.pk

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    invoice = models.ForeignKey(Invoice, related_name="orders", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    discount = models.IntegerField()
    total = models.FloatField()
    tax = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.product.name} {self.quantity}"
