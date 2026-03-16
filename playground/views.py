from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product

def say_hello(request):
    # 0, 1, 2, 3, 4
    query_set = Product.objects.all()[:5]

    # query_set = Product.objects.all()[5:10] # 5,6,7,8,9
    for product in query_set:
        print(product)

    return render(request, 'hello.html', { 'name': 'Ankit', 'products': list(query_set)})
