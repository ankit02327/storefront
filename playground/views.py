from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product, OrderItem

def say_hello(request):
    query_set = Product.objects.only('id','title')

    # query_set = Product.objects.defer('description')
    for product in query_set:
        print(product)

    return render(request, 'hello.html', { 'name': 'Ankit', 'products': list(query_set)})
