from django.urls import URLResolver, path, include
from rest_framework_extensions.routers import (
    ExtendedDefaultRouter,
)


from .views import ProductsVieset, UnitsVieset, BrandsVieset

router = ExtendedDefaultRouter()
product_router = router.register("products", ProductsVieset, basename="product")
product_router = router.register("brands", BrandsVieset, basename="brand")
product_router = router.register("units", UnitsVieset, basename="unit")
urlpatterns: list[URLResolver] = [path("", include(router.urls))]