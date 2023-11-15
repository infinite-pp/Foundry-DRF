from grades.models import Grade


class GradeSerValidator:
    """
    Validator class for Grade serialization.
    """

    def __init__(self, grade, instance=None):
        self.grade = grade
        self.instance = instance
        self.errors = []

    def _validate_grade_code_alphanumeric(self, value):
        """
        Validates that the Grade code is alphanumeric.

        Args:
            value (str): The Grade code to be validated.
        """
        if value and not value.isalnum():
            self.errors.append({"Grade code": f"{value} can be alphanumeric only"})

    def _validate_grade_code_not_duplicate(self, code, id):
        """
        Validates that the Grade code is not a duplicate.

        Args:
            code (str): The Grade code to be validated.
        """
        if Grade.objects.filter(code=code).exclude(id=id).exists():
            self.errors.append({"Grade code": f"Grade code {code} already exists"})

    def validate(self):
        """
        Performs overall validation for the Grade data.

        Returns:
            list: A list containing validation errors, if any.
        """
        code = self.grade.get("code")
        id = self.instance.id if self.instance else None
        if code:
            self._validate_grade_code_alphanumeric(code)
            self._validate_grade_code_not_duplicate(code, id)
        return self.errors


class GradeTcSerValidator:
    """
    Validator class for Grade Target Chemistry serialization.
    """

    def __init__(self, grade, instance=None):
        self.grade = grade
        self.instance = instance
        self.errors = []

    def _validate_tc_min_max(self, element, min, max):
        """
        Validates that Min <= Max for a GradeTC element.

        Args:
            element (str): The GradeTC element.
            min (float): The minimum rate for the element.
            max (float): The maximum rate for the element.
        """
        if min and max and not (min <= max):
            self.errors.append({"grade_tc": f"Min > Max for element {element}"})

    def _validate_duplicate_element(self, tc):
        """
        Validates that there are no duplicate elements in GradeTC.

        Args:
            tc (list): List of GradeTC objects.
        """
        ele_list = [tc_object.get("element") for tc_object in tc]
        for ele in set(ele_list):
            if ele_list.count(ele) > 1:
                self.errors.append({"grade_tc": f"Duplicate element {ele}"})

    def validate(self):
        """
        Performs overall validation for the GradeTC data.

        Returns:
            list: A list containing validation errors, if any.
        """
        tc = self.grade.get("grade_tc")
        if tc:
            for tc_object in tc:
                element, min, max = (
                    tc_object.get("element"),
                    tc_object.get("min_rate"),
                    tc_object.get("max_rate"),
                )
                self._validate_tc_min_max(element, min, max)
            self._validate_duplicate_element(tc)
        return self.errors
