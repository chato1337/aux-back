from rest_framework import serializers

from dinner.models import DinnerOrder, DinnerProduct, Table
from inventory.serializers import ProductSerializer


class DinnerProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DinnerProduct
        exclude = []

class DinnerOrderSelializer(serializers.ModelSerializer):
    products = DinnerProductSerializer(many=True)

    class Meta:
        model = DinnerOrder
        exclude = []


class CreateDinnerOrderSerializer(serializers.Serializer):
    owner = serializers.CharField(max_length=45)
    tips = serializers.IntegerField()
    subtotal = serializers.FloatField()
    products = serializers.PrimaryKeyRelatedField(queryset=DinnerProduct.objects.all(), many=True)

    def create(self, data):
        products = data.pop('products')
        order = DinnerOrder.objects.create(**data)

        for product in products:

            order.products.add(product)

        return order


class TableSerializer(serializers.ModelSerializer):
    orders = DinnerOrderSelializer(many=True)
    class Meta:
        model = Table
        exclude = []

class CreateTableSerializer(serializers.Serializer):
    number = serializers.IntegerField()
    orders = serializers.PrimaryKeyRelatedField(queryset=DinnerOrder.objects.all(), many=True, required=False)
    customers = serializers.IntegerField()
    total = serializers.FloatField()

    def create(self, data):
        if 'orders' in data:
            orders = data.pop('orders')
            table = Table.objects.create(**data)

            for order in orders:
                table.orders.add(order)

            return table

        return Table.objects.create(**data)
    def update(self, instance, validated_data):
        instance.number = validated_data.get('number', instance.number)
        instance.customers = validated_data.get('customers', instance.customers)
        instance.total = validated_data.get('total', instance.total)

        orders = validated_data.get('orders', None)
        if orders is not None:
            instance.orders.set(orders)
        instance.save()
        return instance

        return super().update(instance, validated_data)