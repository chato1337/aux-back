from django.urls import path
from django.urls.resolvers import URLPattern
from rest_framework import routers
from inventory import views


urlpatterns = [
    path('product/', views.GetView.as_view(), name="product"),
    path('product/add/', views.AddView.as_view(), name="add-product"),
    path('supplier/', views.GetSuppliersView.as_view(), name="supplier"),
    path('supplier/add/', views.AddSupplierView.as_view(), name="add-supplier"),
    path('supplier/edit/', views.EditSupplierView.as_view(), name="add-supplier"),
    path('category/', views.GetCategoryView.as_view(), name="add-category"),
    path('category/edit/', views.EditCategoryView.as_view(), name="edit-category"),
    path('category/add/', views.AddCategoryView.as_view(), name="category")
]