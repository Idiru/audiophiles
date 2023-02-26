from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "ecommerce/index.html")


def article(request, numero_article):
    if numero_article in ["01", "02", "03"]:
        return render(request, f"ecommerce/article_{numero_article}.html")
    return render(request, "ecommerce/article_not_found.html")