# Generated by Django 4.2.4 on 2023-09-20 19:43

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="List",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("products", models.ManyToManyField(to="products.product")),
            ],
            options={
                "db_table": "shopping_list",
            },
        ),
    ]
