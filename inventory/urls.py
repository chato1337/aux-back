from django.urls import path
from django.urls.resolvers import URLPattern
from rest_framework import routers
from inventory import views


urlpatterns = [
    path('product/', views.GetView.as_view(), name="product"),
    path('product/add/', views.AddView.as_view(), name="add-product"),
    path('supplier/', views.GetSuppliersView.as_view(), name="supplier"),
    path('supplier/add/', views.AddSupplierView.as_view(), name="add-supplier")
]