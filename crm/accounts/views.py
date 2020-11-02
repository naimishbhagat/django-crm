from django.shortcuts import render

from django.http import HttpResponse
from .models import *


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered')
    pending = orders.filter(status='Pending')
    context = {'orders': orders, 'customers': customers, 'total_orders': total_orders,
               'delivered': delivered.count(), 'pending': pending.count()}
    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    return render(request, 'accounts/customer.html', {'customer': customer})
