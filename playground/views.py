from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F, Value, Func, Count, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat 
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.contrib.contenttypes.models import ContentType 
from store.models import Product, OrderItem, Customer, Order
from tags.models import TaggedItem

def say_hello(request):
    collection = Collection()
    # collection = Collection(title='Video Games')
    collection.title = 'Video Games'
    collection.featured_product = Product(pk=1)
    # collection.featured_product_id = 1
    collection.save()
    collection.id

    # collection = Collection.objects.create(name='a', featured_product_id=1)
    # collection.id 
    
    return render(request, 'hello.html', { 'name': 'Ankit', 'tags': queryset})
