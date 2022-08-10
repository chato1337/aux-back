from rest_framework import serializers
from user.models import Customer, Organization, Role, Staff, User
from rest_framework.validators import UniqueValidator

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        exclude = []

class CreateRoleSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    description = serializers.CharField(max_length=300)

    def create(self, validated_data):
        return Role.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        return instance

class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        exclude = []

class CreateOrganizationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=32, validators=[UniqueValidator(queryset=Organization.objects.all())])
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    identifier = serializers.CharField(max_length=17, validators=[UniqueValidator(queryset=Organization.objects.all())])
    phone = serializers.IntegerField()
    address = serializers.CharField(max_length=64)
    email = serializers.EmailField()

    def create(self, data):
        return Organization.objects.create(**data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer()
    organization = OrganizationSerializer(many=True)

    class Meta:
        model = User
        exclude = []

class UserFlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = []

class CreateUserSerializer(serializers.Serializer):
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all())
    name = serializers.CharField(max_length=70, validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    phone = serializers.CharField(max_length=12, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(max_length=64)
    status = serializers.CharField(max_length=24)
    # is_active = serializers.BooleanField()
    # created_at = serializers.DateTimeField()

    def create(self, data):
        return User.objects.create(**data)

    def update(self, instance, validated_data):
        instance.role = validated_data.get('role', instance.role)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.password = validated_data.get('password', instance.password)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        return instance

    class Meta:
        extra_kwargs = {'created_at': {'required': False}, 'is_active': {'required': False}}

class StaffSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Staff
        exclude = []

class CreateStaffSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    first_name = serializers.CharField(max_length=35)
    last_name = serializers.CharField(max_length=35)
    address = serializers.CharField(max_length=60)
    # created_at = serializers.DateTimeField()

    def create(self, data):
        return Staff.objects.create(**data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    class Meta:
        extra_kwargs = {'created_at': {'required': False}}

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        exclude = []

class CreateCustomerSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    full_name = serializers.CharField(max_length=60)
    leverage = serializers.CharField(max_length=60)
    # created_at = serializers.DateTimeField()

    def create(self, data):
        return Customer.objects.create(**data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    class Meta:
        extra_kwargs = {'created_at': {'required': False}}

