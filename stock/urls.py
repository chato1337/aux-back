from django.urls import path
from django.urls.resolvers import URLPattern
from rest_framework import routers
from stock import views


urlpatterns = [
    path('invoice/', views.GetInvoiceView.as_view(), name="invoice"),
    path('invoice/add/', views.AddInvoiceView.as_view(), name="add-invoice"),
]