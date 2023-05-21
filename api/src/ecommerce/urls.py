from django.urls import path
from .views import index, article
from rest_framework import routers
from ecommerce.views import productsViewSet

router = routers.SimpleRouter()
router.register('products', productsViewSet)

urlpatterns = [
    path('', index, name="ecommerce-index"),
    path('article-<str:numero_article>/', article, name="blog-article"),
]