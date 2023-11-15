from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator


class EleNameValidator(BaseValidator):
    """
    Validator for checking if an element name contains only alphabetic characters and starts with an uppercase character.

    Parameters:
        limit_value (int): The maximum length of the element name.

    Raises:
        ValidationError: If the element name does not meet the specified criteria.
    """

    def __call__(self, value):
        """
        Validate the element name.

        Parameters:
            value (str): The element name to be validated.

        Raises:
            ValidationError: If the element name does not meet the specified criteria.
        """
        if not value.isalpha():
            raise ValidationError(
                f"Element name {value} must contain alphabetic characters only."
            )
        if not value[0].isupper():
            raise ValidationError(
                f"Element name {value} must start with an uppercase character."
            )


class EleSymbolValidator(BaseValidator):
    """
    Validator for checking if an element symbol contains only alphabetic characters and starts with an uppercase character.

    Parameters:
        limit_value (int): The maximum length of the element symbol.

    Raises:
        ValidationError: If the element symbol does not meet the specified criteria.
    """

    def __call__(self, value):
        """
        Validate the element symbol.

        Parameters:
            value (str): The element symbol to be validated.

        Raises:
            ValidationError: If the element symbol does not meet the specified criteria.
        """
        if not value.isalpha():
            raise ValidationError(
                f"Element symbol {value} must contain alphabetic characters only."
            )
        if not value[0].isupper():
            raise ValidationError(
                f"Element symbol {value} must start with an uppercase character."
            )
