from rest_framework.serializers import ModelSerializer

from grades.models import TargetChemistry


class TargetChemistryCreateSerializer(ModelSerializer):
    """Serializer for creating target chemistries."""

    class Meta:
        model = TargetChemistry
        fields = [
            "grade",
            "element",
            "min_rate",
            "max_rate",
            "relaxed_min_rate",
            "relaxed_max_rate",
        ]


class GradeTargetChemistrySerializer(ModelSerializer):
    """Serializer for handling target chemistry input in grades."""

    class Meta:
        model = TargetChemistry
        fields = [
            "element",
            "min_rate",
            "max_rate",
            "relaxed_min_rate",
            "relaxed_max_rate",
        ]
