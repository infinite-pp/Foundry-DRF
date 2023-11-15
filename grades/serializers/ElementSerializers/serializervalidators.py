from grades.models import Element


class ElementSerValidator:
    """
    Validator class for validating Element data before serialization.
    """

    def __init__(self, element, instance=None):
        """
        Initialize the ElementSerValidator.

        Args:
            element (dict): A dictionary containing Element data.
        """
        self.element = element
        self.instance = instance
        self.errors = []

    def _validate_ele_name_alphabetic(self, value):
        """
        Validate if the name contains only alphabetical characters.

        Args:
            value (str): The name to be validated.
        """
        if value and not value.isalpha():
            self.errors.append({"name": f"Name {value} can be alphabetic only"})

    def _validate_ele_name_statswith_uppercase(self, value):
        """
        Validate if the name starts with an uppercase letter.

        Args:
            value (str): The name to be validated.
        """
        if value and value.isalpha() and not value[0].isupper():
            self.errors.append({"name": f"Name {value} should start with uppercase"})

    def _validate_ele_symbol_alphabetic(self, value):
        """
        Validate if the symbol contains only alphabetical characters.

        Args:
            value (str): The symbol to be validated.
        """
        if value and not value.isalpha():
            self.errors.append({"symbol": f"Symbol {value} can be alphabetic only"})

    def _validate_ele_symbol_statswith_uppercase(self, value):
        """
        Validate if the symbol starts with an uppercase letter.

        Args:
            value (str): The symbol to be validated.
        """
        if value and value.isalpha() and not value[0].isupper():
            self.errors.append(
                {"symbol": f"Symbol {value} should start with uppercase"}
            )

    def _validate_ele_symbol_not_duplicate(self, symbol, id):
        """
        Validate if the symbol is not already in use by an existing Element.

        Args:
            symbol (str): The symbol to be validated.
        """
        if Element.objects.filter(symbol=symbol).exclude(id=id).exists():
            self.errors.append({"symbol": f"Symbol {symbol} already exists"})

    def validate(self):
        """
        Perform overall validation for both name and symbol.

        Returns:
            list: A list of error messages resulting from the validation.
        """
        name, symbol = self.element.get("name"), self.element.get("symbol")
        id = self.instance.id if self.instance else None
        if name:
            self._validate_ele_name_alphabetic(name)
            self._validate_ele_name_statswith_uppercase(name)
        if symbol:
            self._validate_ele_symbol_alphabetic(symbol)
            self._validate_ele_symbol_statswith_uppercase(symbol)
            self._validate_ele_symbol_not_duplicate(symbol, id)
        return self.errors
