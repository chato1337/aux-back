from rest_framework import serializers
from inventory.models import Product


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = []