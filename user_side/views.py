from django.http import JsonResponse
from django.shortcuts import render, redirect
from config.settings import MEDIA_ROOT
from .models import Category, Product, Customer, Order, OrderProduct
from .services import get_product_by_id, get_user_by_phone_number
from .forms import CustomerForm, OrderForm
import json


# Create your views here.
def main_page(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    orders = []
    order_list = request.COOKIES.get("orders")
    total_price = request.COOKIES.get("total_price", 0)
    print(f'{order_list=}')
    print(f'{total_price=}')

    if order_list:
        for key, value in json.loads(order_list).items():
            orders.append(
                {
                    'product': Product.objects.get(pk=int(key)),
                    'count': value
                }
            )

    ctx = {
        'categories': categories,
        'products': products,
        'orders': orders,
        'total_price': total_price,
        'MEDIA_ROOT': MEDIA_ROOT,
    }
    response = render(request=request, template_name='user_side/index.html', context=ctx)
    response.set_cookie('kalit', 'Assalomu alaykum')
    return response


def home_page(request):
    if request.GET:
        product = get_product_by_id(pk=request.GET.get("product_id", 0))
        print(f'{product=}')
        return JsonResponse(product)


def order_page(request):
    if request.GET:
        user = get_user_by_phone_number(request.GET.get('phone_number', 0))
        print(f"{user=}")
        if user:
            return JsonResponse(user)


def main_order(request):
    model = Customer()
    if request.POST:
        try:
            model = Customer.objects.get(phone_number=request.POST.get("phone_number", ""))
        except Exception as e:
            print(f'Xatolik: {e}')
            model = Customer()
        form = CustomerForm(request.POST or None, instance=model)
        if form.is_valid():
            customer = form.save()
            form_order = OrderForm(request.POST or None, instance=Order())
            if form_order.is_valid():
                order = form_order.save(customer=customer)
                print("order:", order)
                orders_list = request.COOKIES.get("orders")

                for key, value in json.loads(orders_list).items():
                    product = get_product_by_id(int(key))

                    counts = value
                    order_product = OrderProduct(
                        amount=counts,
                        # price=product['price'],
                        product_id=product['id'],
                        order_id=order.id
                    )
                    order_product.save()

                return redirect("main-page")
            else:
                print(f"{form_order.errors=}")
        else:
            print(f"{form.errors=}")

    categories = Category.objects.all()
    products = Product.objects.all()
    orders = []
    orders_list = request.COOKIES.get("orders")
    total_price = request.COOKIES.get("total_price")
    if orders_list:
        for key, val in json.loads(orders_list).items():
            orders.append(
                {
                    "product": Product.objects.get(pk=int(key)),
                    "count": val
                }
            )
    ctx = {
        'categories': categories,
        'products': products,
        'orders': orders,
        'total_price': total_price,
        'MEDIA_ROOT': MEDIA_ROOT,
    }

    response = render(request, 'user_side/order.html', ctx)
    response.set_cookie("greeting", 'hello')
    return response
