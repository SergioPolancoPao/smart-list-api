from django.db import models
from django.db.models import F


class Unit(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    searches = models.PositiveBigIntegerField(default=1)

    class Meta:
        db_table: str = "unit"


class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    searches = models.PositiveBigIntegerField(default=1)

    class Meta:
        db_table: str = "brand"


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    size = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    unit = models.ForeignKey(Unit, null=True, on_delete=models.DO_NOTHING)
    brand = models.ForeignKey(Brand, null=True, on_delete=models.DO_NOTHING)
    searches = models.PositiveBigIntegerField(default=1)

    class Meta:
        db_table: str = "product"

    def update_when_used(self, unit: Unit = None, brand: Brand = None):
        update_fields: list[str] = ["searches"]
        self.searches: F = F("searches") + 1

        if brand:
            self.brand: Brand = brand
            update_fields.append("brand")

        if unit:
            self.unit: Unit = unit
            update_fields.append("unit")

        self.save(update_fields=update_fields)
