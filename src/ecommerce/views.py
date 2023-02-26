from django.shortcuts import render
from rest_framework import viewsets
from ecommerce.models import Products
from ecommerce.serializers import ecommerceSerializer
import django_filters


# Create your views here.
def index(request):
    return render(request, "ecommerce/index.html")


def article(request, numero_article):
    if numero_article in ["01", "02", "03"]:
        return render(request, f"ecommerce/article_{numero_article}.html")
    return render(request, "ecommerce/article_not_found.html")

class ProductsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter()
    category = django_filters.CharFilter()

    class Meta:
        model = Products
        fields = ['name','category']

class productsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ecommerceSerializer
    filterset_fields = ['name', 'category']


