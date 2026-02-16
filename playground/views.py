from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

def say_hello(request):
    query_set = Product.objects.filter(unit_price__range = (20, 50) )

    print(query_set)


    return render(request, 'hello.html', {'name': 'Mayanja', 'products': list(query_set)})
