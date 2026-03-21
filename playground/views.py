from django.shortcuts import render
from store.models import Product

def say_hello(request):
    queryset = Product.objects.raw('SELECT * FROM store_product')
    # with connection.cursor() as cursor:
    #    cursor.execute()

        # cursor.callproc('get_customers', [1,2])
    return render(request, 'hello.html', { 'name': 'Ankit', 'result': list(queryset)})
