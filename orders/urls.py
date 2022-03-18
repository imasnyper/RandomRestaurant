from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('menu', views.menu, name='menu'),
    path('order_pending', views.order_pending, name='order_pending')
]