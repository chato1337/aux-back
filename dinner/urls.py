from django.urls import path
from dinner import views

urlpatterns = [
    path('orders/', views.OrderListCreateView.as_view(), name="dinner-orders"),
    path('tables/', views.TableListCreateView.as_view(), name="tables"),
    path('products/', views.DinnerProductView.as_view(), name="dinner-product"),
    path('tables/<int:pk>', views.TableUpdateView.as_view(), name="update-table"),
]