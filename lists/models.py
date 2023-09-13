from django.db import models
from products.models import Product


class List(models.Model):
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table: str = "shopping_list"
