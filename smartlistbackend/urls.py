"""
URL configuration for smartlistbackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import URLResolver, path, include
from rest_framework_extensions.routers import (
    ExtendedDefaultRouter,
)

from lists.urls import router as list_router
from products.urls import router as product_router

router = ExtendedDefaultRouter()

router.registry.extend(list_router.registry)
router.registry.extend(product_router.registry)

urlpatterns: list[URLResolver] = [
    path("api/", include(router.urls)),
    path("admin/", admin.site.urls),
]
