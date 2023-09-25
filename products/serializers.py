from django.db.models import F
from rest_framework import serializers
from .models import Product, Unit, Brand


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields: list[str] = ["pk", "name", "created_at", "updated_at", "searches"]

        read_only_fields: list[str] = ["pk", "searches"]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields: list[str] = ["pk", "name", "created_at", "updated_at", "searches"]

        read_only_fields: list[str] = ["pk", "searches"]


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[])
    unit = serializers.CharField(source="unit.name", required=False)
    brand = serializers.CharField(source="brand.name", required=False)

    class Meta:
        model = Product
        fields: list[str] = [
            "pk",
            "name",
            "size",
            "created_at",
            "updated_at",
            "searches",
            "unit",
            "brand",
        ]

        read_only_fields: list[str] = ["pk", "searches"]
