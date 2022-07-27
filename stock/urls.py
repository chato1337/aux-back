from django.urls import path
from django.urls.resolvers import URLPattern
from rest_framework import routers
from stock import views


urlpatterns = [
    path('bill/', views.GetBillView.as_view(), name="bill"),
    path('bill/add/', views.AddBillView.as_view(), name="add-bill"),
]