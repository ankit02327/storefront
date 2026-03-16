from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F, Value, Func, Count
from django.db.models.functions import Concat 
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product, OrderItem, Customer
# from django.db.models.aggregates import Count 
def say_hello(request):
    queryset = Customer.objects.annotate(
        orders_count=Count('order')
    )
    return render(request, 'hello.html', { 'name': 'Ankit', 'result': queryset})
