from django.shortcuts import render
from rest_framework import viewsets
from ecommerce.models import Products
from ecommerce.serializers import ecommerceSerializer


# Create your views here.
def index(request):
    return render(request, "ecommerce/index.html")


def article(request, numero_article):
    if numero_article in ["01", "02", "03"]:
        return render(request, f"ecommerce/article_{numero_article}.html")
    return render(request, "ecommerce/article_not_found.html")


class productsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ecommerceSerializer
