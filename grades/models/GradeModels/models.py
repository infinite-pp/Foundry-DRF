from django.db.models import (
    CASCADE,
    CharField,
    DecimalField,
    ForeignKey,
    Index,
    Model,
    UniqueConstraint,
)

from grades.models.modelconstants import MAX_GRADE_CODE_LEN, MAX_GRADE_NAME_LEN

from .modelvalidators import GradeCodeValidator


class Grade(Model):
    """
    Represents a grade in the system.

    Attributes:
        name (CharField): The name of the grade.
        code (CharField): The code associated with the grade, validated with grade_code_validator.
    """

    name = CharField(max_length=MAX_GRADE_NAME_LEN)
    code = CharField(max_length=MAX_GRADE_CODE_LEN, validators=[GradeCodeValidator])

    class Meta:
        """Meta attributes of Grade."""

        indexes = [Index(fields=["code"])]
        ordering = ["name"]
        constraints = [
            UniqueConstraint(fields=["code"], name="grade_code_unique"),
        ]

    def __str__(self):
        """String representation of the Grade."""

        return f"{self.name} - {self.code}"
