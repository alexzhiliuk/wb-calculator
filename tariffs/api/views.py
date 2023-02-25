from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from tariffs.models import *
from tariffs.api.serializers import *


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer