from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from user.models import Customer, Organization, Role, Staff, User
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from user.serializers import (
    CreateCustomerSerializer,
    CreateOrganizationSerializer,
    CreateRoleSerializer,
    CreateStaffSerializer,
    CreateUserSerializer,
    CustomerSerializer,
    OrganizationSerializer,
    RoleSerializer,
    StaffFlatSerializer,
    StaffSerializer,
    UserFlatSerializer,
    UserLoginSerializer,
    UserSerializer
)
from user.services.user_service import UserService

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
        #generate username
        username = request.data['email'].replace('@', '_')

        #get role with owner role stored in db
        role = Role.objects.get(name='owner')
        role_serializer = RoleSerializer(role).data

        # create user
        user_data = { **request.data, 'name': username, 'role': role_serializer['id'], 'status': 'to-activate' }
        serializer = CreateUserSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user_serializer = UserSerializer(user).data

        # create staff
        staff_data = { **request.data, 'user': user_serializer['id'], 'organization': None }
        staff_serializer = CreateStaffSerializer(data=staff_data)
        staff_serializer.is_valid(raise_exception=True)
        created_staff = staff_serializer.save()

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
    ordering_fields = ('id', 'first_name', 'last_name', 'address',)

    def get_queryset(self):
        # get only organziation
        owner = self.request.query_params.get('owner')
        return Staff.objects.filter(organization=owner)

class AddStaffView(APIView):
    def post(self, request):
        #generate username
        username = request.data['email'].replace('@', '_')

        #get role with owner role stored in db
        role = Role.objects.get(name='employ')
        role_serializer = RoleSerializer(role).data

        # create user
        user_data = { **request.data, 'name': username, 'role': role_serializer['id'], 'status': 'active' }
        serializer = CreateUserSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user_serializer = UserSerializer(user).data

        # create staff
        staff_data = { **request.data, 'user': user_serializer['id']}
        staff_serializer = CreateStaffSerializer(data=staff_data)
        staff_serializer.is_valid(raise_exception=True)
        created_staff = staff_serializer.save()

        return Response(StaffSerializer(created_staff).data)

class EditStaffView(APIView):
    def put(self, request):
        staff = Staff.objects.get(pk=request.data["id"])
        serializer_staff = StaffFlatSerializer(staff).data
        payload_staff = { **serializer_staff, **request.data }
        edit_staff = CreateStaffSerializer(staff, data=payload_staff)
        edit_staff.is_valid(raise_exception=True)
        updated_staff = edit_staff.save()

        return Response(StaffSerializer(updated_staff).data)

class GetCustomerView(generics.ListAPIView):
    serializer_class = CustomerSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('fullname',)
    ordering_fields = ('id', 'user', 'fullname', 'leverage',)

    def get_queryset(self):
        return Customer.objects.all()

class AddCustomerView(APIView):
    def post(self, request):
        #create user
        username = request.data['email'].replace('@', '_')
        #getting role for customer
        role = Role.objects.get(name='customer')
        #parse to dict
        role_serializer = RoleSerializer(role).data
        user_data = {
            **request.data,
            'name': username,
            'role': role_serializer['id'],
            'status': 'to-activate',
            'password': 'invalid-passwd'
        }
        user_serializer = CreateUserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        created_user = user_serializer.save()
        #parse to dict
        user = UserSerializer(created_user).data

        #create customer
        customer_data = { **request.data, 'user': user['id'] }
        serializer = CreateCustomerSerializer(data=customer_data)
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
        # create organization
        serializer = CreateOrganizationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # update status for org owner db instance
        org_owner = User.objects.get(pk=request.data['owner'])
        org_owner_serializer = UserFlatSerializer(org_owner).data
        payload_status = { **org_owner_serializer, 'status': 'active' }

        update_user = CreateUserSerializer(org_owner, payload_status)
        update_user.is_valid(raise_exception=True)
        new_organization = serializer.save()
        org_serializer = OrganizationSerializer(new_organization).data
        update_user.save()

        # get updated staff user with org db instance
        staff_user = Staff.objects.get(user=org_owner_serializer["id"])
        staff_serializer = StaffFlatSerializer(staff_user).data
        payload_org = { **staff_serializer, 'organization': org_serializer['id'] }
        updated_staff = CreateStaffSerializer(staff_user, payload_org)
        updated_staff.is_valid(raise_exception=True)
        final_staff = updated_staff.save()

        data = {
            'staff': StaffSerializer(final_staff).data,
            'organization': org_serializer
        }

        return Response(data)

class EditOrganizationView(APIView):
    def put(self, request):
        pass

class ShowOrganizationView(generics.RetrieveAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class LoginView(TokenObtainPairView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        username = request.data.get('email')
        password = request.data.get('password')

        isValid = UserService.authenticate(username, password)

        if isValid:
            user = User.objects.get(email=username)

            refresh = RefreshToken.for_user(user)

            user_serializer = UserSerializer(user).data
            staff = Staff.objects.get(user=user_serializer['id'])
            organization = Organization.objects.get(owner=user_serializer['id'])

            data = {
                'staff': StaffSerializer(staff).data,
                'organization':  OrganizationSerializer(organization).data,
                'token':  str(refresh.access_token),
                'refresh_token':  str(refresh),
            }

            return Response(data)
        return Response({ 'error': 'wrong user or password2' }, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        user = User.objects.filter(id=request.data.get('id', ''))

        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({ 'message': 'session closed' }, status=status.HTTP_200_OK)
        Response({ 'error': 'wrong user or password' }, status=status.HTTP_400_BAD_REQUEST)
