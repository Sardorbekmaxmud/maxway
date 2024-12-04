from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from user_side.models import Category, Product, Customer
from .forms import CategoryForm, ProductForm, CustomerForm
from .services import (get_categories, get_products, get_customers,
                       get_orders, get_product_by_category, get_top_sold_products,
                       get_orders_by_id, get_customer_order_id_list)


# Create your views here.
def login_required_decorator(func):
    return login_required(function=func, login_url='login-page')


@login_required_decorator
def logout_page(request):
    logout(request=request)
    return redirect('login-page')


def login_page(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request=request, user=user)
            return redirect('home-page')
    return render(request=request, template_name='dashboard/login.html')


@login_required_decorator
def home_page(request):
    categories = get_categories()
    products = get_products()
    customers = get_customers()
    orders = get_orders()
    product_by_category = get_product_by_category()
    top_sold_pd = get_top_sold_products()

    context = {
        'counts': {
            'categories': len(categories),
            'products': len(products),
            'customers': len(customers),
            'orders': len(orders),
            'top_sold_pd': top_sold_pd,
        },
        "product_by_category": product_by_category,
    }
    # print(context)

    return render(request=request, template_name="dashboard/index.html", context=context)


@login_required_decorator
def category_list(request):
    categories = get_categories()
    ctx = {
        'categories': categories
    }
    return render(request=request, template_name='dashboard/category/list.html', context=ctx)


@login_required_decorator
def category_create(request):
    model = Category()
    form = CategoryForm(data=request.POST, instance=model)

    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You created category: {request.POST.get('name')}"]
        request.session['actions'] = actions

        category_count = request.session.get('category_count', 0)
        category_count += 1
        request.session['category_count'] = category_count

        return redirect('category-list')
    ctx = {
        'form': form
    }
    return render(request=request, template_name='dashboard/category/form.html', context=ctx)


@login_required_decorator
def category_edit(request, pk):
    model = Category.objects.get(pk=pk)
    form = CategoryForm(data=request.POST or None, instance=model)

    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You edited category: {request.POST.get('name')}"]
        request.session['actions'] = actions

        return redirect('category-list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request=request, template_name='dashboard/category/form.html', context=ctx)


@login_required_decorator
def category_delete(request, pk):
    model = Category.objects.get(pk=pk)
    model.delete()

    actions = request.session.get('actions', [])
    actions += [f"You deleted category: id={pk}"]
    request.session['actions'] = actions

    return redirect('category-list')


@login_required_decorator
def product_list(request):
    products = Product.objects.all().order_by('category__name', 'name')
    print(products.query)
    ctx = {
        'products': products
    }
    return render(request=request, template_name='dashboard/product/list.html', context=ctx)


@login_required_decorator
def product_create(request):
    model = Product()
    form = ProductForm(request.POST or None, request.FILES or None, instance=model)

    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You created product: {request.POST.get('name')}"]
        request.session['actions'] = actions

        product_count = request.session.get('product_count', 0)
        product_count += 1
        request.session['product_count'] = product_count

        return redirect('product-list')
    ctx = {
        'form': form
    }
    return render(request=request, template_name='dashboard/product/form.html', context=ctx)


@login_required_decorator
def product_edit(request, pk):
    model = Product.objects.get(pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=model)

    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You edited product: {request.POST.get('name')}"]
        request.session['actions'] = actions

        return redirect('product-list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request=request, template_name='dashboard/product/form.html', context=ctx)


@login_required_decorator
def product_delete(request, pk):
    model = Product.objects.get(pk=pk)
    model.delete()

    actions = request.session.get('actions', [])
    actions += [f"You deleted product: id={pk}"]
    request.session['actions'] = actions

    return redirect('product-list')


@login_required_decorator
def customer_list(request):
    customers = get_customers()
    ctx = {
        'customers': customers
    }
    return render(request=request, template_name='dashboard/customer/list.html', context=ctx)


@login_required_decorator
def customer_create(request):
    model = Customer()
    form = CustomerForm(data=request.POST, instance=model)

    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You created customer: {request.POST.get('name')}"]
        request.session['actions'] = actions

        customer_count = request.session.get('customer_count', 0)
        customer_count += 1
        request.session['customer_count'] = customer_count

        return redirect('customer-list')
    ctx = {
        'form': form
    }
    return render(request=request, template_name='dashboard/customer/form.html', context=ctx)


@login_required_decorator
def customer_edit(request, pk):
    model = Customer.objects.get(pk=pk)
    form = CustomerForm(data=request.POST or None, instance=model)

    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You edited customer: {request.POST.get('name')}"]
        request.session['actions'] = actions

        return redirect('customer-list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request=request, template_name='dashboard/customer/form.html', context=ctx)


@login_required_decorator
def customer_delete(request, pk):
    model = Customer.objects.get(pk=pk)
    model.delete()

    actions = request.session.get('actions', [])
    actions += [f"You deleted customer: id={pk}"]
    request.session['actions'] = actions

    return redirect('customer-list')


@login_required_decorator
def customer_order_id_list(request, pk):
    customer_orders = get_customer_order_id_list(pk)

    if customer_orders[0]['order_id'] is None:
        customer_orders[0]['order_id'] = 0

    ctx = {
        'customer_order': customer_orders
    }
    return render(request=request, template_name='dashboard/customer_order/list.html', context=ctx)


@login_required_decorator
def order_list(request):
    orders = get_orders()
    ctx = {
        'orders': orders
    }
    return render(request=request, template_name='dashboard/order/list.html', context=ctx)


# @login_required_decorator
# def order_create(request):
#     model = Order()
#     form = OrderForm(data=request.POST, instance=model)
#
#     if request.POST and form.is_valid():
#         form.save()
#
#         actions = request.session.get('actions', [])
#         actions += [f"You created order: {request.POST.get('name')}"]
#         request.session['actions'] = actions
#
#         order_count = request.session.get('order_count', 0)
#         order_count += 1
#         request.session['order_count'] = order_count
#
#         return redirect('order-list')
#     ctx = {
#         'form': form
#     }
#     return render(request=request, template_name='dashboard/order/form.html', context=ctx)
#
#
# @login_required_decorator
# def order_edit(request, pk):
#     model = Order.objects.get(pk=pk)
#     form = OrderForm(data=request.POST or None, instance=model)
#
#     if request.POST and form.is_valid():
#         form.save()
#
#         actions = request.session.get('actions', [])
#         actions += [f"You edited order: {request.POST.get('name')}"]
#         request.session['actions'] = actions
#
#         return redirect('order-list')
#     ctx = {
#         'model': model,
#         'form': form
#     }
#     return render(request=request, template_name='dashboard/order/form.html', context=ctx)
#
#
# @login_required_decorator
# def order_delete(request, pk):
#     model = Order.objects.get(pk=pk)
#     model.delete()
#
#     actions = request.session.get('actions', [])
#     actions += [f"You deleted order: id={pk}"]
#     request.session['actions'] = actions
#
#     return redirect('order-list')


@login_required_decorator
def order_by_id_list(request, pk):
    orders = get_orders_by_id(pk)
    total_price = 0
    for order in orders:
        total_price += int(order['total'])
    ctx = {
        'orders': orders,
        'total_price': total_price,
    }
    return render(request=request, template_name='dashboard/orderproduct/list.html', context=ctx)
