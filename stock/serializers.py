from rest_framework import serializers
from inventory.models import Product
from inventory.serializers import ProductSerializer
from stock.models import Bill, Order
from user.models import Customer, Staff
from user.serializers import CustomerSerializer, StaffSerializer

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Order
        exclude = []

class CreateOrderSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    bill = serializers.PrimaryKeyRelatedField(queryset=Bill.objects.all())
    quantity = serializers.IntegerField()
    discount = serializers.IntegerField()
    total = serializers.IntegerField()
    tax = serializers.IntegerField()
    # created_at = serializers.DateTimeField()

    def create(self, data):
        return Order.objects.create(**data)

    class Meta:
        extra_kwargs = {'created_at': {'required': False}}

class BillSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True)
    customer = CustomerSerializer()
    seller = StaffSerializer()
    class Meta:
        model = Bill
        exclude = []

class BillFlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        exclude = []

class CreateBillSerializer(serializers.Serializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    seller = serializers.PrimaryKeyRelatedField(queryset=Staff.objects.all())
    payment_type = serializers.CharField(max_length=30)
    total = serializers.IntegerField()

    def create(self, data):
        return Bill.objects.create(**data)

    def update(self, instance, validated_data):
        instance.customer = validated_data.get('customer', instance.customer)
        instance.seller = validated_data.get('seller', instance.seller)
        instance.payment_type = validated_data.get('payment_type', instance.payment_type)
        instance.total = validated_data.get('total', instance.total)
        instance.save()

        return instance

    class Meta:
        extra_kwargs = {'created_at': {'required': False}}


