from rest_framework import serializers
from ecommerce.models import Products
import django_filters


class ecommerceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Products
        fields = '__all__'