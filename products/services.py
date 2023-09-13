from django.db.models import F
from django.core import exceptions

from .models import Unit, Brand, Product


def create_unit_or_update_searches(name: str) -> Unit:
    try:
        unit: Unit = Unit.objects.get(name=name)
        unit.searches = F("searches") + 1
        unit.save(update_fields=["searches"])
    except exceptions.ObjectDoesNotExist:
        unit = Unit(name=name)
        unit.save()

    return unit


def create_brand_or_update_searches(name: str) -> Brand:
    try:
        brand: Brand = Brand.objects.get(name=name)
        brand.searches = F("searches") + 1
        brand.save(update_fields=["searches"])
    except exceptions.ObjectDoesNotExist:
        brand = Brand(name=name)
        brand.save()

    return brand


def create_product_or_update_searches(
    name: str, size: int, brand_name: str, unit_name: str
) -> Product:
    brand = None
    unit = None

    if brand_name:
        brand: Brand = create_brand_or_update_searches(brand_name)

    if unit_name:
        unit: Unit = create_unit_or_update_searches(unit_name)

    try:
        product: Product = Product.objects.get(name=name)
        product.searches = F("searches") + 1
        product.save(update_fields=["searches"])
    except exceptions.ObjectDoesNotExist:
        product = Product(name=name, size=size, brand=brand, unit=unit)
        product.save()

    return product
