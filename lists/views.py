from rest_framework import mixins, viewsets

from .models import List
from .serializers import ListSerializer

class ListsViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = ListSerializer
    queryset = List.objects.order_by("pk")
