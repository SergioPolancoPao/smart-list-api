from django.db import transaction
from typing import TypedDict
from products.models import Product
from products.services import (
    create_product_or_update_searches,
)
from lists.models import List


class ProductAbstract(TypedDict):
    name: str
    size: int
    brand: str
    unit: str


@transaction.atomic()
def create_list(name: str, products: list[ProductAbstract]) -> List:
    list = List()
    list.name = name
    list.save()

    for product_data in products:
        product_name: str = product_data["name"]
        product_size: int = product_data["size"]
        unit_name: str = product_data.get("unit", None)
        brand_name: str = product_data.get("brand", None)

        product: Product = create_product_or_update_searches(
            product_name, product_size, brand_name, unit_name
        )

        list.products.add(product)

    return list
