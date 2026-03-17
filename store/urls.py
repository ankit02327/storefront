from django.urls import path
from . import views

# URLConf module
urlpatterns = [path("products/", views.product_list)]
