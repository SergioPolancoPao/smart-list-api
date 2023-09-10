from rest_framework import mixins, viewsets

from .models import Product, Unit, Brand
from .serializers import ProductSerializer, UnitSerializer, BrandSerializer

class ProductsVieset(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = ProductSerializer
    query_set = Product.objects.order_by("pk")

class UnitsVieset(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = UnitSerializer
    query_set = Unit.objects.order_by("pk")

class BrandsVieset(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = BrandSerializer
    query_set = Brand.objects.order_by("pk")