from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from user.models import Customer, Organization, Role, Staff, User
from rest_framework import status

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
    UserFlatSerializer,
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
        username = request.data['email'].replace('@', '_')
        role = Role.objects.get(name='owner')
        role_serializer = RoleSerializer(role).data
        user_data = { **request.data, 'name': username, 'role': role_serializer['id'], 'status': 'to-activate' }
        serializer = CreateUserSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user_serializer = UserSerializer(user).data

        staff_data = { **request.data, 'user': user_serializer['id'] }
        staff_serializer = CreateStaffSerializer(data=staff_data)
        created_staff = staff_serializer.is_valid(raise_exception=True)
        created_staff.save()

        data = {
            'staff': StaffSerializer(created_staff).data,
            'token': 'awesometoken123'
        }

        return Response(data)

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

        user = User.objects.get(pk=request.data['owner'])

        user_serializer = UserFlatSerializer(user).data
        user_status = { **user_serializer, 'status': 'active' }

        update_user = CreateUserSerializer(user, user_status)
        update_user.is_valid(raise_exception=True)
        serializer_org = serializer.save()
        update_user.save()
        staff_user = Staff.objects.get(pk=staff_user)

        data = {
            'staff': StaffSerializer(staff_user).data,
            'organization': OrganizationSerializer(serializer_org).data
        }

        return Response(data)

class EditOrganizationView(APIView):
    def put(self, request):
        pass

class LoginView(APIView):
    def post(self, request):
        try:
            user = User.objects.get(email=request.data['email'])
            user_serializer = UserSerializer(user).data
            staff = Staff.objects.get(user=user_serializer['id'])
            organization = None
            data = {
                'staff': StaffSerializer(staff).data,
                'organization': organization,
                'token': 'super_token123'
            }

            return Response(data)

        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
