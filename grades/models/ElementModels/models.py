from django.db.models import CharField, Index, Model, UniqueConstraint

from grades.models.modelconstants import MAX_ELEMENT_NAME_NAME, MAX_ELEMENT_SYMBOL_LEN

from .modelvalidators import EleNameValidator, EleSymbolValidator


class Element(Model):
    """
    Represents an element in the system.

    Attributes:
        name (CharField): The name of the element, validated with ele_name_validator.
        symbol (CharField): The symbol associated with the element, validated with ele_symbol_validator.
    """

    name = CharField(max_length=MAX_ELEMENT_NAME_NAME, validators=[EleNameValidator])
    symbol = CharField(
        max_length=MAX_ELEMENT_SYMBOL_LEN, validators=[EleSymbolValidator]
    )

    class Meta:
        """Meta attributes of Element."""

        indexes = [Index(fields=["symbol"])]
        ordering = ["name"]
        constraints = [
            UniqueConstraint(fields=["symbol"], name="ele_symbol_unique"),
        ]

    def __str__(self):
        """String representation of the Element."""

        return f"{self.name} - {self.symbol}"
