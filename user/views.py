from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from user.models import Customer, Organization, Role, Staff, User

from user.serializers import (
    CreateCustomerSerializer,
    CreateOrganizationSerializer,
    CreateRoleSerializer,
    CreateStaffSerializer,
    CreateUserSerializer,
    CustomerSerializer,
    OrganizationSerializer,
    RoleSerializer,
    StaffSerializer,
    UserSerializer
)

# Create your views here.
class GetRoleView(generics.ListAPIView):
    serializer_class = RoleSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('name',)

    def get_queryset(self):
        return Role.objects.all()

class AddRoleView(APIView):
    def post(self, request):
        serializer = CreateRoleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        role = serializer.save()

        return Response(RoleSerializer(role).data)

class EditRoleView(APIView):
    pass

class GetUserView(generics.ListAPIView):
    serializer_class = UserSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('name',)

    def get_queryset(self):
        return User.objects.all()

class AddUserView(APIView):
    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(UserSerializer(user).data)

class EditUserView(APIView):
    pass


class GetStaffView(generics.ListAPIView):
    serializer_class = StaffSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('first_name',)
    ordering_fields = ('first_name', 'last_name', 'address',)

    def get_queryset(self):
        return Staff.objects.all()

class AddStaffView(APIView):
    def post(self, request):
        serializer = CreateStaffSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        staff = serializer.save()

        return Response(StaffSerializer(staff).data)

class EditStaffView(APIView):
    pass

class GetCustomerView(generics.ListAPIView):
    serializer_class = CustomerSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('first_name',)
    ordering_fields = ('first_name', 'last_name', 'address',)

    def get_queryset(self):
        return Customer.objects.all()

class AddCustomerView(APIView):
    def post(self, request):
        serializer = CreateCustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        customer = serializer.save()

        return Response(CustomerSerializer(customer).data)

class EditCustomerView(APIView):
    pass

class GetOrganizationView(generics.ListAPIView):
    serializer_class = OrganizationSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name')
    ordering_fields = ('id', 'name', 'phone', 'address')

    def get_queryset(self):
        return Organization.objects.all()

class AddOrganizationView(APIView):
    def post(self, request):
        serializer = CreateOrganizationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        organization = serializer.save()

        return Response(OrganizationSerializer(organization).data)

class EditOrganizationView(APIView):
    def put(self, request):
        pass