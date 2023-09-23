from django.db import models
from products.models import Product


class List(models.Model):
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table: str = "shopping_list"
