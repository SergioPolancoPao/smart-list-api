from django.db.models import F

from .models import Unit, Brand, Product


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
    name: str, size: int, brand_name: str, unit_name: str
) -> Product:
    brand = None
    unit = None

    if brand_name:
        brand: Brand = create_brand_or_update_searches(brand_name)

    if unit_name:
        unit: Unit = create_unit_or_update_searches(unit_name)

    product_data = {
        "name": name,
        "size": size,
        "brand": brand,
        "unit": unit
    }

    product, created = Product.objects.get_or_create(
        name=name,
        defaults=product_data
    )

    if not created:
        product.searches = F("searches") + 1
        product.save(update_fields=["searches"])

    return product
