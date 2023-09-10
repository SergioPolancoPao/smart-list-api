from rest_framework import mixins, viewsets
from rest_framework.response import Response

from .models import List
from .serializers import ListSerializer
from .services import create_list

class ListsViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = ListSerializer
    queryset = List.objects.order_by("pk")

    def create(self, request) -> Response:
        print('dsfsfa', request.data["products"])
        products = request.data["products"]
        list = create_list(products)
        serialized = self.get_serializer(list)
        return Response(serialized.data)