from rest_framework.routers import DefaultRouter

# from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views
# from pprint import pprint

# router = SimpleRouter()
router = DefaultRouter()
router.register("products", views.ProductViewSet)
router.register("collections", views.CollectionViewSet)
# pprint(router.urls)
# URLConf module
urlpatterns = router.urls
