from rest_framework.serializers import ModelSerializer, ValidationError

from grades.models import Element

from .serializervalidators import ElementSerValidator


class ElementListSerializer(ModelSerializer):
    """Serializer for listing elements."""

    class Meta:
        model = Element
        fields = ["id", "name", "symbol"]


class ElementDetailSerializer(ModelSerializer):
    """Serializer for detailing elements."""

    class Meta:
        model = Element
        fields = ["id", "name", "symbol"]


class ElementCreateSerializer(ModelSerializer):
    """Serializer for creating elements."""

    class Meta:
        model = Element
        fields = ["id", "name", "symbol"]

    def validate(self, data):
        result = super().validate(data)
        custom_errors = ElementSerValidator(data).validate()
        if custom_errors:
            raise ValidationError(custom_errors)
        return result


class ElementUpdateSerializer(ModelSerializer):
    """Serializer for updating elements."""

    class Meta:
        model = Element
        fields = ["id", "name", "symbol"]

    def validate(self, data):
        result = super().validate(data)
        custom_errors = ElementSerValidator(data, self.instance).validate()
        if custom_errors:
            raise ValidationError(custom_errors)
        return result
