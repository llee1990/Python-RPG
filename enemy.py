""".py file for class Child"""
# Leon Lee
# BCIT
# A01062166

from random import randint


class Child:

    def __init__(self, health_points):
        """Create an instance of the class 'Child'.

        Default health_points must be set to 5.
        Default strength value is set to 6.
        Default damage value is set to 0.
        Default escape_damage value is set to 0
        PARAM: Number of HP.
        PRECONDITION: The 'health_points' value must be a positive integer - default is 5
        POSTCONDITION: N/A
        RETURN: N/A
        """
        self.health_points = health_points
        self.strength = 6
        self.damage = 0
        self.escape_damage = 0

    def get_health(self) -> int:
        """Retrieve the value of the 'health_points' attribute of an instance from this class.

        PARAM: N/A
        PRECONDITION: N/A
        POSTCONDITION: N/A
        RETURN: Integer value of the 'health_points' attribute of an instance from this class.
        """
        return self.health_points

    def set_zero_health(self):
        """Set the value of the 'health_points' attribute to 0.

        PARAM: N/A
        PRECONDITION: N/A
        POSTCONDITION: The HP of the character will become 0.
        RETURN: N/A
        """
        self.health_points = 0

    def get_damage(self) -> int:
        """Retrieve the value of the 'damage' attribute of an instance from this class.

        The damage value is the amount of damage the enemy can deal to the character.
        PARAM: N/A
        PRECONDITION: N/A
        POSTCONDITION: N/A
        RETURN: Integer value of the 'damage' attribute of an instance from this class.
        """
        return self.damage

    def get_escape_damage(self):
        """Retrieve the value of the 'escape_damage' attribute of an instance from this class.

        The escape damage value is the amount of damage the enemy can deal to the character when the character is
        escaping.
        PARAM: N/A
        PRECONDITION: N/A
        POSTCONDITION: N/A
        RETURN: Integer value of the 'escape_damage' attribute of an instance from this class.
        """
        return self.escape_damage

    def set_health(self, new_health: int):
        """Replace the value in the 'health_points' attribute with the value in the parameter.

        PARAM: The value the user wants to change the 'health_points' value to.
        PRECONDITION: The parameter must be an integer >= 0.
        POSTCONDITION: The value in the original 'health_points' attribute
        will be replaced with value of 'new_health'
        RETURN: N/A
        """
        self.health_points = new_health

    def attack(self, char):
        """Simulate one round of attack on an instance of class Character.

        The 'damage' is equal to the value of a random integer between 1 and the enemy's 'strength', which is set to 6.
        PARAM: An instance of the class Character.
        PRECONDITION: N/A
        POSTCONDITION: The Character instance's health points will subtract the value of 'damage' generated.
        RETURN: N/A
        """
        damage = randint(1, self.strength)
        self.damage = damage
        char.decrease_health(damage)

    def escape_attack(self, char):
        """Attack an instance of the class Character.

        This function runs when a character is trying to escape and gets damaged. The 'escape_damage' is equal to the
        value of a random integer between 1 and 4.
        PARAM: An instance of the class Character.
        PRECONDITION: N/A
        POSTCONDITION: The Character instance's health points will subtract the value of 'escape_damage' generated.
        RETURN: N/A
        """
        escape_damage = randint(1, 4)
        self.escape_damage = escape_damage
        char.decrease_health(escape_damage)

    def decrease_health(self, hp: int):
        """Decrease value of the 'health_points' attribute within an instance of this class.

        Decreases current health_points by the value in the parameter.
        PARAM: Value that will be subtracted by the current 'health_points' value.
        PRECONDITION: Parameter value must be a positive integer.
        POSTCONDITION: The 'health_points' attribute of the instance will be updated to the decreased amount.
        RETURN: N/A
        """
        self.health_points -= hp
