from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product

def say_hello(request):
    # Products: inventory = price 
    query_set = Product.objects.filter(inventory=F('price'))

    for product in query_set:
        print(product)

    return render(request, 'hello.html', { 'name': 'Ankit', 'products': list(query_set)})
