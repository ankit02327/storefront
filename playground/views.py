from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product, OrderItem

def say_hello(request):
    result = Product.objects.aggregate(Count('id'))

    # result = Product.objects.filter(collect__id=1).aggregate(count=Count('id'), min_price=Min(price))
    # result = Product.objects.aggregate(count=Count('id'), min_price=Min(price))
    # result = Product.objects.aggregate(count=Count('id'))
    return render(request, 'hello.html', { 'name': 'Ankit', 'result': result})
