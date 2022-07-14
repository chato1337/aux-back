from django.urls import path
from django.urls.resolvers import URLPattern
from rest_framework import routers
from stock import views


urlpatterns = [
    path('get/', views.GetView.as_view(), name="stocks"),
    path('add/', views.AddView.as_view(), name="create-stock"),
]