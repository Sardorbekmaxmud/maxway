from django.urls import path
from .views import main_page, home_page, order_page, main_order

urlpatterns = [
    path('', main_page, name='main-page'),
    path('home_page/', home_page, name='home_page'),
    path('order_page/', order_page, name='order-page'),
    path('order/', main_order, name='main-order'),
]
