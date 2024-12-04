from django.urls import path
from .views import (login_page, logout_page, home_page,
                    category_list, category_create, category_edit, category_delete,
                    product_list, product_create, product_edit, product_delete,
                    customer_list, customer_create, customer_edit, customer_delete,
                    customer_order_id_list, order_list, order_by_id_list)

urlpatterns = [
    path('', home_page, name='home-page'),
    path('login/', login_page, name='login-page'),
    path('logout/', logout_page, name='logout-page'),

    path('category/list/', category_list, name='category-list'),
    path('category/create/', category_create, name='category-create'),
    path('category/<int:pk>/edit/', category_edit, name='category-edit'),
    path('category/<int:pk>/delete/', category_delete, name='category-delete'),

    path('product/list/', product_list, name='product-list'),
    path('product/create/', product_create, name='product-create'),
    path('product/<int:pk>/edit/', product_edit, name='product-edit'),
    path('product/<int:pk>/delete/', product_delete, name='product-delete'),

    path('customer/list/', customer_list, name='customer-list'),
    path('customer/order/<int:pk>/list/', customer_order_id_list, name='customer-order-list'),
    path('customer/create/', customer_create, name='customer-create'),
    path('customer/<int:pk>/edit/', customer_edit, name='customer-edit'),
    path('customer/<int:pk>/delete/', customer_delete, name='customer-delete'),

    path('order/list/', order_list, name='order-list'),
    # path('order/create/', order_create, name='order-create'),
    # path('order/<int:pk>/edit/', order_edit, name='order-edit'),
    # path('order/<int:pk>/delete/', order_delete, name='order-delete'),

    path('orderproduct/<int:pk>/list/', order_by_id_list, name='orderproduct-list'),
]
