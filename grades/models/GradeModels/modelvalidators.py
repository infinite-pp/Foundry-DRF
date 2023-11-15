from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator


class GradeCodeValidator(BaseValidator):
    """
    Validator for checking if a grade code contains only alphanumeric characters.

    Parameters:
        limit_value (int): The maximum length of the grade code.

    Raises:
        ValidationError: If the grade code contains non-alphanumeric characters.
    """

    def __call__(self, value):
        """
        Validate the grade code.

        Parameters:
            value (str): The grade code to be validated.

        Raises:
            ValidationError: If the grade code contains non-alphanumeric characters.
        """
        if not value.isalnum():
            raise ValidationError(
                f"Grade name {value} must contain alphanumeric characters only."
            )
