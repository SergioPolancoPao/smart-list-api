from django.db.models import F
from typing import TypedDict

from .models import Unit, Brand, Product

class UnitAbstract(TypedDict):
    name: str

class BrandAbstract(TypedDict):
    name: str



def create_unit_or_update_searches(name: str) -> Unit:
    unit, created = Unit.objects.get_or_create(
        name=name,
        defaults={"name": name}
    )

    if not created:
        unit.searches = F("searches") + 1
        unit.save(update_fields=["searches"])

    return unit

def create_brand_or_update_searches(name: str) -> Brand:
    brand, created = Brand.objects.get_or_create(
        name=name,
        defaults={"name": name}
    )

    if not created:
        brand.searches = F("searches") + 1
        brand.save(update_fields=["searches"])

    return brand

def create_product_or_update_searches(
    name: str, size: int, brand: BrandAbstract, unit: UnitAbstract
) -> Product:
    brand_result = None
    unit_result = None

    if brand:
        brand_name = brand["name"]
        brand_result: Brand = create_brand_or_update_searches(brand_name)

    if unit:
        unit_name = unit["name"]
        unit_result: Unit = create_unit_or_update_searches(unit_name)

    product_data = {
        "name": name,
        "size": size,
        "brand": brand_result,
        "unit": unit_result
    }

    product, created = Product.objects.select_for_update().get_or_create(
        name=name,
        defaults=product_data
    )

    if not created:
        product.update_when_used(unit=unit_result, brand=brand_result)

    return product

