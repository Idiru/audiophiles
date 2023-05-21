from rest_framework import serializers
from ecommerce.models import Products


class ecommerceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'