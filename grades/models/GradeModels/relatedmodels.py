from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import (
    CASCADE,
    DecimalField,
    ForeignKey,
    Index,
    Model,
    UniqueConstraint,
)

from grades.models.ElementModels.models import Element
from grades.models.modelconstants import (
    FK_ELE_TO_TC,
    FK_GRADE_TO_TC,
    TC_MAX_ELE_RATE,
    TC_MIN_ELE_RATE,
    TC_RATE_DECIMAL_PLACES,
    TC_RATE_DIGITS,
)

from .models import Grade


class TargetChemistry(Model):
    """
    Represents a target chemistry in the system.

    Attributes:
        grade (ForeignKey): The grade associated with the target chemistry.
        element (ForeignKey): The element associated with the target chemistry.
        min_rate (DecimalField): The minimum rate for the target chemistry.
        max_rate (DecimalField): The maximum rate for the target chemistry.
        relaxed_min_rate (DecimalField): The relaxed minimum rate for the target chemistry.
        relaxed_max_rate (DecimalField): The relaxed maximum rate for the target chemistry.
    """

    grade = ForeignKey(Grade, on_delete=CASCADE, related_name=FK_GRADE_TO_TC)
    element = ForeignKey(Element, on_delete=CASCADE, related_name=FK_ELE_TO_TC)
    min_rate = DecimalField(
        max_digits=TC_RATE_DIGITS,
        decimal_places=TC_RATE_DECIMAL_PLACES,
        null=True,
        blank=True,
        validators=[
            MinValueValidator(TC_MIN_ELE_RATE),
            MaxValueValidator(TC_MAX_ELE_RATE),
        ],
    )
    max_rate = DecimalField(
        max_digits=TC_RATE_DIGITS,
        decimal_places=TC_RATE_DECIMAL_PLACES,
        null=True,
        blank=True,
        validators=[
            MinValueValidator(TC_MIN_ELE_RATE),
            MaxValueValidator(TC_MAX_ELE_RATE),
        ],
    )
    relaxed_min_rate = DecimalField(
        max_digits=TC_RATE_DIGITS,
        decimal_places=TC_RATE_DECIMAL_PLACES,
        null=True,
        blank=True,
        validators=[
            MinValueValidator(TC_MIN_ELE_RATE),
            MaxValueValidator(TC_MAX_ELE_RATE),
        ],
    )
    relaxed_max_rate = DecimalField(
        max_digits=TC_RATE_DIGITS,
        decimal_places=TC_RATE_DECIMAL_PLACES,
        null=True,
        blank=True,
        validators=[
            MinValueValidator(TC_MIN_ELE_RATE),
            MaxValueValidator(TC_MAX_ELE_RATE),
        ],
    )

    class Meta:
        """Meta attributes of TargetChemistry."""

        indexes = [Index(fields=["grade"]), Index(fields=["element"])]
        constraints = [
            UniqueConstraint(
                fields=["grade", "element"], name="grade_ele_unique_in_tc"
            ),
        ]

    def __str__(self):
        """String representation of the TargetChemistry."""

        return f"{self.grade.name} - {self.element.name}"
