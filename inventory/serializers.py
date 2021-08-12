from rest_framework import serializers
from inventory.models import Store


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        exclude = []