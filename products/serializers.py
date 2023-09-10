from rest_framework import serializers
from .models import Product, Unit, Brand

class ProductSerializer(serializers.ModelSerializer):
    unit = serializers.CharField(source="unit.name", read_only=True)
    brand = serializers.CharField(source="brand.name", read_only=True)

    class Meta:
        model = Product
        fields: list[str] = [
            "pk",
            "name",
            "size",
            "created_at",
            "searches",
            "unit",
            "brand"
        ]

        read_only_fields: list[str] = ["pk", "searches"]
    
class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields: list[str] = ["pk", "name", "created_at", "searches"]

        read_only_fields: list[str] = ["pk", "searches"]

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields: list[str] = ["pk", "name", "created_at", "searches"]

        read_only_fields: list[str] = ["pk", "searches"]