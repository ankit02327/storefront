from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product, OrderItem

def say_hello(request):
    query_set = Product.objects.values('id','title')

    # query_set = Product.objects.filter(
    #    id__in= OrderItem.objects.values('product_id').distinct()).order_by('title')
    # query_set = OrderItem.objects.values('product_id').distinct()
    # query_set = Product.objects.values_list('id','title')
    # query_set = Product.objects.values_list('id','title')
    # query_set = Product.objects.values('id','title','collection__id')
    for product in query_set:
        print(product)

    return render(request, 'hello.html', { 'name': 'Ankit', 'products': list(query_set)})
