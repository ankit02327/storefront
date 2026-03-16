from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F, Value, Func, Count, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat 
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product, OrderItem, Customer

def say_hello(request):
    discounted_price = ExpressionWrapper(F('price')*0.8, output_field=DecimalField())
    queryset = Product.objects.annotate(
        discounted_price = discounted_price)
    return render(request, 'hello.html', { 'name': 'Ankit', 'result': queryset})
