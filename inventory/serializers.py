from rest_framework import serializers
from inventory.models import Product, Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        exclude = []

class CreateSupplierSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    identifier = serializers.CharField(max_length=30)
    phone = serializers.CharField(max_length=12)
    email = serializers.CharField(max_length=30)
    other_details = serializers.CharField(max_length=150)

    def create(self, data):
        return Supplier.objects.create(**data)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = []

class CreateProductSerializer(serializers.Serializer):
    supplier = SupplierSerializer()
    name = serializers.CharField(max_length=64)
    description = serializers.CharField(max_length=300)
    # category = serializers.IntegerField()
    price = serializers.FloatField()
    expiration_date = serializers.DateField()
    entry_date = serializers.DateTimeField()
    stock = serializers.IntegerField()
    unit = serializers.CharField(max_length=32)
    is_active = serializers.CharField(max_length=16)

    def create(self, data):
        return Product.objects.create(**data)