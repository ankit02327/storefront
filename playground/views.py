from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from store.models import Product

def say_hello(request):
    # Products: inventory < 10 or price < 20
    query_set = Product.objects.filter(Q(inventory__lt=10) | Q(price__lt=20))

    for product in query_set:
        print(product)

    return render(request, 'hello.html', { 'name': 'Ankit', 'products': list(query_set)})
