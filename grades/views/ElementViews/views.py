from rest_framework import viewsets

from grades.models import Element
from grades.serializers import (
    ElementCreateSerializer,
    ElementDetailSerializer,
    ElementListSerializer,
    ElementUpdateSerializer,
)


class ElementViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing, creating, and updating elements.
    """

    queryset = Element.objects.all()
    http_method_names = ["get", "post", "patch"]

    def get_serializer_class(self):
        if self.action == "list":
            return ElementListSerializer
        if self.action == "retrieve":
            return ElementDetailSerializer
        elif self.action == "create":
            return ElementCreateSerializer
        elif self.action == "partial_update":
            return ElementUpdateSerializer
