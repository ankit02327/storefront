from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    # The following can be done (a simple explanation, not related to function)
    # Pull data from db
    # Transform data 
    # Send email 
    return HttpResponse('Hello World!')
