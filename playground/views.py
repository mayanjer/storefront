from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from store.models import Product, Customer, Collection, Order, OrderItem

def say_hello(request):
    query_set = Product.objects.filter(Q(unit_price__lt=10) & Q(inventory__gt=10))

    return render(request, 'hello.html', {'name': 'Mayanja', 'products': list(query_set)})
