from .models import Product
# from rest_framework import generics, mixins, viewsets
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer


class ProductViewset(viewsets.ModelViewSet):
  serializer_class = ProductSerializer
  queryset = Product.objects.all()
  permission_classes = [IsAuthenticated]
