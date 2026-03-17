from django.db import transaction, connection
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F, Value, Func, Count, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat 
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.contrib.contenttypes.models import ContentType 
from store.models import Product, OrderItem, Customer, Order, Collection
from tags.models import TaggedItem

def say_hello(request):
    queryset = Product.objects.raw('SELECT * FROM store_product')
    # with connection.cursor() as cursor:
    #    cursor.execute()

        # cursor.callproc('get_customers', [1,2])
    return render(request, 'hello.html', { 'name': 'Ankit', 'result': list(queryset)})
