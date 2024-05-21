from django.urls import path
from . import views

urlpatterns = [
    # path('ratings', views.RatingsView.as_view()),
    path('index', views.index, name='home'),
    path('lemons', views.lemons, name='lemons'),
    path('orders', views.Orders.listOrders),
]