from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F, Value, Func, Count, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat 
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.contrib.contenttypes.models import ContentType 
from store.models import Product, OrderItem, Customer
from tags.models import TaggedItem

def say_hello(request):
    content_type = ContentType.objects.get_for_model(Product)
    
    return render(request, 'hello.html', { 'name': 'Ankit', 'tags': queryset})
