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
    query_set = List.objects.order_by("pk")

    def post(self, request) -> Response:
        list = create_list(request)
        serialized = self.get_serializer(list)
        return Response(serialized)