from django.db import transaction
from rest_framework.serializers import ModelSerializer, ValidationError

from grades.models import Grade, TargetChemistry

from .relatedserializers import (
    GradeTargetChemistrySerializer,
    TargetChemistryCreateSerializer,
)
from .serializerutils import calculate_tolerance
from .serializervalidators import GradeSerValidator, GradeTcSerValidator


class GradeListSerializer(ModelSerializer):
    """Serializer for listing grades without nested target chemistry."""

    class Meta:
        model = Grade
        fields = ["id", "name", "code"]


class GradeDetailSerializer(ModelSerializer):
    """Serializer for detailing grades with nested target chemistry."""

    grade_tc = GradeTargetChemistrySerializer(many=True, read_only=True)

    class Meta:
        model = Grade
        fields = ["id", "name", "code", "grade_tc"]


class GradeCreateSerializer(ModelSerializer):
    """Serializer for creating grades with nested target chemistry."""

    grade_tc = GradeTargetChemistrySerializer(many=True)

    class Meta:
        model = Grade
        fields = ["id", "name", "code", "grade_tc"]

    def validate(self, data):
        result = super().validate(data)
        custom_errors = [
            *GradeSerValidator(data).validate(),
            *GradeTcSerValidator(data).validate(),
        ]
        if custom_errors:
            raise ValidationError(custom_errors)
        return result

    @transaction.atomic
    def create(self, validated_data):
        """Create a grade with nested target chemistries."""
        tc_data = validated_data.pop("grade_tc")
        grade = super().create(validated_data)

        for tc in tc_data:
            element = tc.get("element")
            min_rate = tc.get("min_rate", None)
            max_rate = tc.get("max_rate", None)

            relaxed_min, relaxed_max = calculate_tolerance(
                element.symbol, min_rate, max_rate
            )

            tc["grade"] = grade.pk
            tc["element"] = element.pk
            tc["relaxed_min_rate"] = relaxed_min
            tc["relaxed_max_rate"] = relaxed_max

            tc_ser = TargetChemistryCreateSerializer(data=tc)
            tc_ser.is_valid(raise_exception=True)
            tc_ser.save()
        return grade


class GradeUpdateSerializer(ModelSerializer):
    """Serializer for updating grades with nested target chemistry."""

    grade_tc = GradeTargetChemistrySerializer(many=True, required=False)

    class Meta:
        model = Grade
        fields = ["id", "name", "code", "grade_tc"]

    def validate(self, data):
        result = super().validate(data)
        custom_errors = [
            *GradeSerValidator(data, self.instance).validate(),
            *GradeTcSerValidator(data, self.instance).validate(),
        ]
        if custom_errors:
            raise ValidationError(custom_errors)
        return result

    @transaction.atomic
    def update(self, instance, validated_data):
        """Update a grade with nested target chemistries."""
        tc_data = validated_data.pop("grade_tc", [])
        grade = super().update(instance, validated_data)

        TargetChemistry.objects.filter(grade=grade).delete()

        for tc in tc_data:
            element = tc.get("element")
            min_rate = tc.get("min_rate", None)
            max_rate = tc.get("max_rate", None)

            relaxed_min, relaxed_max = calculate_tolerance(
                element.symbol, min_rate, max_rate
            )

            tc["grade"] = grade.pk
            tc["element"] = element.pk
            tc["relaxed_min_rate"] = relaxed_min
            tc["relaxed_max_rate"] = relaxed_max

            tc_ser = TargetChemistryCreateSerializer(data=tc)
            tc_ser.is_valid(raise_exception=True)
            tc_ser.save()
        return grade
