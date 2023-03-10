from django.urls import path
from django.urls.resolvers import URLPattern
from rest_framework import routers
from inventory import views


urlpatterns = [
    path('product/', views.GetView.as_view(), name="product"),
    path('product/category/', views.ProductCategoryView.as_view(), name="product-category"),
    path('product/add/', views.AddView.as_view(), name="add-product"),
    path('product/edit/', views.EditView.as_view(), name="edit-product"),
    path('supplier/', views.GetSuppliersView.as_view(), name="supplier"),
    path('supplier/full/', views.GetSuppliersView.as_view(), name="supplier-full"),
    path('supplier/add/', views.AddSupplierView.as_view(), name="add-supplier"),
    path('supplier/edit/', views.EditSupplierView.as_view(), name="add-supplier"),
    path('category/', views.GetCategoryView.as_view(), name="category"),
    path('category/full/', views.GetCategoryView.as_view(), name="category-full"),
    path('category/edit/', views.EditCategoryView.as_view(), name="edit-category"),
    path('category/add/', views.AddCategoryView.as_view(), name="add-category"),
    path('brands/', views.CountBrandsView.as_view(), name="count-brands")
]