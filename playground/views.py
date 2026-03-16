from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product

def say_hello(request):
    # Sorting the data
    query_set = Product.objects.order_by('title')

    # product = Product.objects.latest('price')
    # product = Product.objects.earliest('price')
    # product = Product.objects.order_by('price')[0]
    # query_set = Product.objects.filter(collection__id=1).order_by('price')
    # query_set = Product.objects.order_by('title').reverse()
    # query_set = Product.objects.order_by('price', '-title')
    # query_set = Product.objects.order_by('-title')
    for product in query_set:
        print(product)

    return render(request, 'hello.html', { 'name': 'Ankit', 'products': list(query_set)})
