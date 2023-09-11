from rest_framework import mixins, viewsets

from .models import Product, Unit, Brand
from .serializers import ProductSerializer, UnitSerializer, BrandSerializer


class ProductsVieset(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = ProductSerializer
    queryset = Product.objects.order_by("pk")


class UnitsVieset(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = UnitSerializer
    queryset = Unit.objects.order_by("pk")


class BrandsVieset(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = BrandSerializer
    queryset = Brand.objects.order_by("pk")
