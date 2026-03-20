from .models import Product
import django_filters


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="unit_price", lookup_expr="gt")
    max_price = django_filters.NumberFilter(field_name="unit_price", lookup_expr="lt")

    class Meta:
        model = Product
        fields = ["collection_id"]
