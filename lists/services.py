from django.db import transaction
from django.db.models import F
from django.core import exceptions
from products.models import Product, Brand, Unit
from lists.models import List


class ProductAbstract:
    def __init__(self, name: str, size: int, brand: str, unit: str) -> None:
        self.name: str = name
        self.size: int = size
        self.brand: str = brand
        self.unit: str = unit


@transaction.atomic()
def create_list(products: list[ProductAbstract]) -> List:
    list = List()
    list.save()

    for product_data in products:
        product_name = product_data["name"]
        product_size = product_data["size"]
        unit_name = product_data["unit"]
        brand_name = product_data["brand"]

        try:
            unit: Unit = Unit.objects.get(name=unit_name)
            unit.searches = F("searches") + 1
            unit.save(update_fields=["searches"])
        except exceptions.ObjectDoesNotExist:
            unit = Unit(name=unit_name)
            unit.save()

        try:
            brand: Brand = Brand.objects.get(name=brand_name)
            brand.searches = F("searches") + 1
            brand.save(update_fields=["searches"])
        except exceptions.ObjectDoesNotExist:
            brand = Brand(name=brand_name)
            brand.save()

        try:
            product: Product = Product.objects.get(name=product_name)
            product.searches = F("searches") + 1
            product.save(update_fields=["searches"])
        except exceptions.ObjectDoesNotExist:
            product = Product(
                name=product_name, size=product_size, brand=brand, unit=unit
            )
            product.save()

        list.products.add(product)

    return list
