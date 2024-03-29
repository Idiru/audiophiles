"""audiophiles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from ecommerce.urls import router as products_router
from rest_framework import routers
from django.urls import path, include
from .views import index
from django.contrib import admin
from ecommerce import views


router = routers.DefaultRouter()
router.register('products', views.productsViewSet)

urlpatterns = [
    path('', index, name="index"),
    path('ecommerce/', include("ecommerce.urls")),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
