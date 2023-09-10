from rest_framework import serializers
from .models import List
from products.serializers import ProductSerializer

class ListSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = List
        fields: list[str] = ["pk", "products", "created_at"]

        read_only_fields: list[str] = ["pk"]