""".py file for class Character"""
# Leon Lee
# BCIT
# A01062166

import random


class Character:

    def __init__(self, name: str, health_points: int, coordinates: list, kill_count: int):
        """Create an instance of the class 'Character'.

        Default health_points must be set to 10.
        Default coordinates must be set to [1, 3],
        Default kill_count must be set to 0.
        Default strength value is set to 6.
        Default damage value is set to 0.
        PARAM: The name of the character.
        PARAM: Number of HP.
        PARAM: A list of size 2 that shows player location.
        PARAM: Number of enemies the player has killed.
        PRECONDITION: The 'name' must be a non-empty string
        PRECONDITION: The 'health_points' value must be a positive integer - default is 10
        PRECONDITION: The two integer values in the 'coodinates' list must be > 0 and < 5. - default is [1, 3]
        PRECONDITION: The 'kill_count' value must be a positive integer - default is 0
        POSTCONDITION: N/A
        RETURN: N/A
        """
        self.name = name
        self.health_points = health_points
        self.strength = 6
        self.damage = 0
        self.kill_count = kill_count
        self.coordinates = coordinates

    def get_name(self) -> str:
        """Retrieve the value of the 'name' attribute of an instance from this class.

        PARAM: N/A
        PRECONDITION: N/A
        POSTCONDITION: N/A
        RETURN: String value of the 'name' attribute of an instance from this class.
        """
        return self.name

    def get_coordinate(self):
        """Retrieve the list of the 'coordinate' attribute of an instance from this class.

        PARAM: N/A
        PRECONDITION: N/A
        POSTCONDITION: N/A
        RETURN: List containing the 'coordinate' attribute of an instance from this class.
        """
        return self.coordinates

    def get_health(self) -> int:
        """Retrieve the value of the 'health_points' attribute of an instance from this class.

        PARAM: N/A
        PRECONDITION: N/A
        POSTCONDITION: N/A
        RETURN: Integer value of the 'health_points' attribute of an instance from this class.
        """
        return self.health_points

    def get_damage(self) -> int:
        """Retrieve the value of the 'damage' attribute of an instance from this class.

        The damage value is the amount of damage the character can deal to the enemy.
        PARAM: N/A
        PRECONDITION: N/A
        POSTCONDITION: N/A
        RETURN: Integer value of the 'damage' attribute of an instance from this class.
        """
        return self.damage

    def get_kill_count(self):
        """Retrieve the value of the 'kill_count' attribute of an instance from this class.

        PARAM: N/A
        PRECONDITION: N/A
        POSTCONDITION: N/A
        RETURN: Integer value of the 'kill_count' attribute of an instance from this class.
        """
        return self.kill_count

    def set_zero_health(self):
        """Set the value of the 'health_points' attribute to 0.

        PARAM: N/A
        PRECONDITION: N/A
        POSTCONDITION: The HP of the character will become 0.
        RETURN: N/A
        """
        self.health_points = 0

    def add_kill(self):
        """Increase the value of the 'kill_count' by one.

        PARAM: N/A
        PRECONDITION: N/A
        POSTCONDITION: The 'kill_count' value of an instance from this class will increase by one.
        RETURN: N/A
        """
        self.kill_count += 1

    def regenerate_one_health(self):
        """Increase value of the 'health_points' attribute by one if player's HP is below 10.

        PARAM: N/A
        PRECONDITION: N/A
        POSTCONDITION: N/A
        RETURN: N/A
        """
        if self.health_points < 10:
            self.health_points += 1

    def set_coordinate(self, new_coordinate):
        """Replace the list in the 'coordinates' attribute with one with new values.

        PARAM: A list of size 2 that shows new player location.
        PRECONDITION: The two integer values in the 'new_coordinate' list must be > 0 and < 5
        POSTCONDITION: The list in the original 'coordinates' attribute
        will be replaced with the one in 'new_coordinate'
        RETURN: N/A
        """
        self.coordinates = new_coordinate

    def set_health(self, new_health: int):
        """Replace the value in the 'health_points' attribute with the value in the parameter.

        PARAM: The value the user wants to change the 'health_points' value to.
        PRECONDITION: The parameter must be an integer >= 0.
        POSTCONDITION: The value in the original 'health_points' attribute
        will be replaced with value of 'new_health'
        RETURN: N/A
        """
        self.health_points = new_health

    def move(self, directions):
        """Move the character one position to either north, east, south, or west.

        When a character moves, the list that saves their coordinates will be updated. The zero index will decrease by 1
        if the player moves North. The zero index will increase by 1 if the player moves South. The first index will
        decrease by 1 if the player moves West. The first index will increase by 1 if the player moves East.
        PARAM: A string that shows the direction the character will move.
        PRECONDITION: The string can only be one of four options - 'N' for North, 'E' for East, 'S' for South,
        or '.W' for West.
        POSTCONDITION: The player's 'coordinate' list values will be updated.
        RETURN: N/A
        """
        if directions == "N":
            self.coordinates[0] -= 1
        if directions == "E":
            self.coordinates[1] += 1
        if directions == "S":
            self.coordinates[0] += 1
        if directions == "W":
            self.coordinates[1] -= 1

    def attack(self, victim):
        """Simulate one round of attack on an instance of class Child.

        If character's HP <= 0, return nothing and exit function. Else do damage to the Child instance. The damage
        is equal to the value of a random integer between 1 and the player's 'strength', which is set to 6.
        PARAM: An instance of the class Child.
        PRECONDITION: N/A
        POSTCONDITION: The Child instance's health points will subtract the amount of damage generated.
        RETURN: N/A
        """
        if self.health_points <= 0:
            return
        else:
            damage = random.randint(1, self.strength)
            self.damage = damage
            victim.decrease_health(damage)

    def decrease_health(self, hp: int):
        """Decrease value of the 'health_points' attribute within an instance of this class.

        Decreases current health_points by the value in the parameter.
        PARAM: Value that will be subtracted by current health points value.
        PRECONDITION: Parameter value must be a positive integer.
        POSTCONDITION: The 'health_points' attribute of the instance will be updated to the decreased amount.
        RETURN: N/A
        """
        self.health_points -= hp


