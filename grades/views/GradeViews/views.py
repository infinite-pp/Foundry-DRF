from rest_framework import viewsets

from grades.models import Grade
from grades.serializers import (
    GradeCreateSerializer,
    GradeDetailSerializer,
    GradeListSerializer,
    GradeUpdateSerializer,
)


class GradeViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing, creating, and updating grades with nested target chemistry.
    """

    queryset = Grade.objects.all()
    http_method_names = ["get", "post", "patch"]

    def get_serializer_class(self):
        if self.action == "list":
            return GradeListSerializer
        elif self.action == "retrieve":
            return GradeDetailSerializer
        elif self.action == "create":
            return GradeCreateSerializer
        elif self.action == "partial_update":
            return GradeUpdateSerializer
