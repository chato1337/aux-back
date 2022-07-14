from rest_framework import serializers
from stock.models import Order


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = []