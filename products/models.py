from django.db import models


class Unit(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    searches = models.PositiveBigIntegerField(default=0)


class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    searches = models.PositiveBigIntegerField(default=0)


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    size = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    unit = models.ForeignKey(Unit, on_delete=models.DO_NOTHING)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    searches = models.PositiveBigIntegerField(default=0)
