""".py file for class 'Die'"""
# Leon Lee
# BCIT
# A01062166

import random


class Die:

    def __init__(self, number_of_sides: int):
        """Create an instance of the class 'Die'.

        The instance will simulate a die object.
        Default 'number_of_sides' is 6.
        Default 'face_value' is 1.
        PARAM: Number of sides the user wants on the die, as an integer.
        PRECONDITION: The parameter must be >= 2.
        POSTCONDITION: N/A
        RETURN: N/A
        """
        self.number_of_sides = number_of_sides
        self.face_value = 1

    def get_face_value(self) -> int:
        """Retrieve the value of the 'face_value' attribute of an instance from this class.

        PARAM: N/A
        PRECONDITION: N/A
        POSTCONDITION: N/A
        RETURN: Integer value of the 'face_value' attribute of an instance from this class.
        """
        return self.face_value

    def change_face_value(self, new_face_value: int):
        """Replace the value in the 'face_value' attribute with a new integer value.

        PARAM: A new face value that the user wants to replace the current 'face_value' with.
        PRECONDITION: The parameter must be a positive integer that is lower than the value of the current
        'number_of_sides' of the instance.
        POSTCONDITION: The current value of 'face_value' will be replaced with the value of 'new_face_value'. An
        error message will be printed if value of 'new_face_value' > the value of 'number_of_sides' or < 1.
        RETURN: N/A
        """
        if new_face_value > self.number_of_sides:
            return 'New face value cannot exceed number of sides.'
        elif new_face_value < 1:
            return 'New face value cannot be less than 1.'
        else:
            self.face_value = new_face_value

    def get_number_of_sides(self) -> int:
        """Retrieve the value of the 'number_of_sides' attribute of an instance from this class.

        PARAM: N/A
        PRECONDITION: N/A
        POSTCONDITION: N/A
        RETURN: Integer value of the 'number_of_sides' attribute of an instance from this class.
        """
        return self.number_of_sides

    def change_number_of_sides(self, new_number_of_sides: int):
        """Replace the value in the 'number_of_sides' attribute with a new integer value.

        PARAM: The number of sides that the user wants to replace the current 'face_value' with.
        PRECONDITION: The parameter must be a positive integer that is lower that is >= 2.
        POSTCONDITION: The current value of 'number_of_sides' will be replaced with the value of 'new_number_of_sides'.
        An error message will be printed if value of 'face_value' <= value of 'new_number_of_sides'.
        RETURN: N/A
        """
        if new_number_of_sides <= 2:
            return 'Number of sides cannot be less than 2.'
        else:
            self.number_of_sides = new_number_of_sides

    def roll_die(self) -> int:
        """Roll a die and return the face value.

        The face value is a random integer between 1 and the number of sides the die has.
        PARAM: N/A
        PRECONDITION: N/A
        POSTCONDITION: N/A
        RETURN: An integer between 1 and the number of sides of the die.
        """
        self.face_value = random.randint(1, self.number_of_sides)
        return self.face_value
