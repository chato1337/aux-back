from django.urls import path
from django.urls.resolvers import URLPattern
from rest_framework import routers
from user import views


urlpatterns = [
    path('', views.GetUserView.as_view(), name="user"),
    path('add/', views.AddUserView.as_view(), name="add-user"),
    path('edit/', views.EditUserView.as_view(), name="edit-user"),
    path('role/', views.GetRoleView.as_view(), name="role"),
    path('role/add/', views.AddRoleView.as_view(), name="add-role"),
    path('role/edit/', views.EditRoleView.as_view(), name="add-role"),
    path('staff/', views.GetStaffView.as_view(), name="staff"),
    path('staff/edit/', views.EditStaffView.as_view(), name="edit-staff"),
    path('staff/add/', views.AddStaffView.as_view(), name="add-staff"),
    path('customer/', views.GetCustomerView.as_view(), name="customer"),
    path('customer/edit/', views.EditCustomerView.as_view(), name="edit-customer"),
    path('customer/add/', views.AddCustomerView.as_view(), name="add-customer"),
    path('organization/', views.GetOrganizationView.as_view(), name="organization"),
    path('organization/add/', views.AddOrganizationView.as_view(), name="add-organization"),
    path('organization/edit/', views.EditOrganizationView.as_view(), name="edit-organization"),
    path('organization/<int:pk>', views.ShowOrganizationView.as_view(), name="show-organization"),
    path('login/', views.LoginView.as_view(), name="login"),
]