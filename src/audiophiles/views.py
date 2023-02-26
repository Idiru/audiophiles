from django.shortcuts import render
from datetime import datetime
from ecommerce.models import Products
from rest_framework import viewsets
from django.http import JsonResponse
from .serializers import ecommerceSerializer


def index(request):

    date = datetime.today()

    return render(request, "audiophiles/index.html", context={"date": date})

def db(viewsets.ModelViewSet):
    data = Products.objects.all()
    serializer_class = ecommerceSerializer
    #dico_liste = []

   # for donnee in data:
        # dico_donnee = {'slug': donnee.slug, "image": donnee.image, "category": donnee.category}
       # dico_liste.append(dico_donnee)

    #return JsonResponse({'donnees': dico_liste})

