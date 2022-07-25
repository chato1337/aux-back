from rest_framework import serializers
from inventory.models import Product, Supplier, Category
from rest_framework.validators import UniqueValidator

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        exclude = []

class CreateSupplierSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30, validators=[UniqueValidator(queryset=Supplier.objects.all())])
    identifier = serializers.CharField(max_length=30, validators=[UniqueValidator(queryset=Supplier.objects.all())])
    phone = serializers.CharField(max_length=12, validators=[UniqueValidator(queryset=Supplier.objects.all())])
    email = serializers.CharField(max_length=30, validators=[UniqueValidator(queryset=Supplier.objects.all())])
    other_details = serializers.CharField(max_length=150)

    def create(self, data):
        return Supplier.objects.create(**data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.identifier = validated_data.get('identifier', instance.identifier)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.other_details = validated_data.get('other_details', instance.other_details)
        instance.save()

        return instance

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = []

class CreateCategorySerializer(serializers.Serializer):
    # name = serializers.CharField(max_length=30)
    name = serializers.CharField(max_length=30, validators=[UniqueValidator(queryset=Category.objects.all())])
    description = serializers.CharField(max_length=300)

    def create(self, data):
        return Category.objects.create(**data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        return instance

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    supplier = SupplierSerializer()

    class Meta:
        model = Product
        exclude = []

class CreateProductSerializer(serializers.Serializer):
    # supplier = serializers.SlugRelatedField(Supplier.objects.all(), slug_field="name")
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
        print(data)
        # return Product.objects.create(**data)

    class Meta:
        extra_kwargs = {'supplier': {'required': False}, 'category': {'required': False}}

