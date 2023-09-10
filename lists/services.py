from django.db import transaction
from django.db.models import F
from django.core import exceptions
from products.models import Product, Brand, Unit
from lists.models import List

@transaction.atomic()
def create_list(product_name: str, product_size: str, unit_name: str, brand_name: str) -> List:
    try:
        unit: Unit = Unit.objects.select_for_update().get("name", unit_name)
    except exceptions.ObjectDoesNotExist:
        unit = Unit(name=unit)
        unit.searches = F("searches") + 1
        unit.save(update_fields="searches")

    try:
        brand: Brand = Brand.objects.get("name", brand_name)
    except exceptions.ObjectDoesNotExist:
        brand = Brand(name=unit)
        brand.searches = F("searches") + 1
        brand.save(update_fields="searches")

    try:
        product: Product = Product.objects.get("name", product_name)
    except exceptions.ObjectDoesNotExist:
        product = Product(
            name=product_name,
            size=product_size,
            brand=brand,
            unit=unit
        )
        product.searches = F("searches") + 1
        product.save(update_fields="searches")

    
    list = List()
    list.save()
    list.products.add(product)

    return list
