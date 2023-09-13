from django.urls import URLResolver, path, include
from rest_framework_extensions.routers import (
    ExtendedDefaultRouter,
)

from .views import ListsViewSet

router = ExtendedDefaultRouter()
lists_router = router.register("lists", ListsViewSet, basename="list")
urlpatterns: list[URLResolver] = [path("", include(router.urls))]
