from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product, OrderItem

def say_hello(request):
    # select_related (1)
    # prefetch_related (n)
    query_set = Product.objects.select_related('collection').all()

    # query_set = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    # query_set = Product.objects.prefetch_related('promotions').select_related('collection').all()
    # query_set = Product.objects.prefetch_related('promotions').all()
    # query_set = Product.objects.all()

    for product in query_set:
        print(product)

    return render(request, 'hello.html', { 'name': 'Ankit', 'products': list(query_set)})
