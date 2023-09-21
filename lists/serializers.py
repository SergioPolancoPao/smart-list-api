from rest_framework import serializers
from .models import List
from products.serializers import ProductSerializer
from .services import create_list


class ListSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, allow_empty=False)

    class Meta:
        model = List
        fields: list[str] = ["pk", "products", "created_at"]

        read_only_fields: list[str] = ["pk"]

    def create(self, validated_data) -> List:
        products_data = validated_data.pop("products")
        list: List = create_list(products_data)
        return list
