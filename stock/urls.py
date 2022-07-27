from django.urls import path
from django.urls.resolvers import URLPattern
from rest_framework import routers
from stock import views


urlpatterns = [
    path('', views.GetBillView.as_view(), name="stocks"),
    path('pay/', views.AddBillView.as_view(), name="pay"),
]