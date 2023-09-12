from django.db import models


class Unit(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    searches = models.PositiveBigIntegerField(default=0)

    class Meta:
        db_table: str = "unit"


class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    searches = models.PositiveBigIntegerField(default=0)

    class Meta:
        db_table: str = "brand"


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    size = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    unit = models.ForeignKey(Unit, null=True, on_delete=models.DO_NOTHING)
    brand = models.ForeignKey(Brand, null=True, on_delete=models.DO_NOTHING)
    searches = models.PositiveBigIntegerField(default=0)

    class Meta:
        db_table: str = "product"
