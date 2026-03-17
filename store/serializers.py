from decimal import Decimal
from store.models import Product, Collection
from rest_framework import serializers


class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    # unit_price = serializers.DecimalField(max_digits=6, decimal_places=2,source='price')
    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")
    collection = serializers.HyperlinkedRelatedField(
        queryset=Collection.objects.all(), view_name="collection-detail"
    )
    # collection = CollectionSerializer()
    # collection = serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all())

    def calculate_tax(self, product: Product):
        return product.price * Decimal(1.1)
