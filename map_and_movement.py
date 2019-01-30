"""Module of functions related to map and movement."""
# Leon Lee
# BCIT
# A01062166
import doctest
import character


def draw_map(char: character.Character):
    """Print a map of the game with the position of the character as a 'X'.

    A map of the game with all the borders will be printed. The character will be marked as an 'X' on the map.
    PARAM: An instance belonging to the class 'Character'.
    PRECONDITION: The parameter must be an instance belonging to the class 'Character'.
    POSTCONDITION: A map of the game layout will be printed along with where the character is on the map.
    The movable area will be a 4 by 4 area.
    RETURN: N/A.
    """
    print('')
    for y in range(6):
        for x in range(6):
            if y == 0 and x == 0:
                print('o' + ' ', end='')
            elif y == 0 and x == 5:
                print('o' + ' ', end='')
            elif y == 5 and x == 0:
                print('o' + ' ', end='')
            elif y == 5 and x == 5:
                print('o' + ' ', end='')
            elif y == char.get_coordinate()[0] and x == char.get_coordinate()[1]:
                print('X' + ' ', end='')
            elif y == 0 or y == 5:
                print('-' + ' ', end='')
            elif y == 0 and x == 5:
                print('+' + ' ', end='')
            elif x == 0 or x == 5:
                print('|' + ' ', end='')
            else:
                print(' ' + ' ', end='')
        print('')


def move_character(char: character.Character, direction: str):
    """Move the player to a new position on the map.

    The player can only move to a position that is within the values of 'lower_boundary' and 'upper_boundary'. A
    warning message will appear if a player moves to a position that is a border. Once a player moves,
    PARAM: An instance belonging to the class 'Character'.
    PRECONDITION: The parameter must be an instance belonging to the class 'Character'.
    POSTCONDITION: A character can only move to a position that is not a physical boundary. If a player chooses to
    quit, they can choose to save the game or quit without saving.
    RETURN: N/A.
    >>> my_char = character.Character('test_char', 10, [1, 2], 0)
    >>> move_character(my_char, 'S')
    True
    >>> my_char_2 = character.Character('test_char_2', 10, [1, 2], 0)
    >>> move_character(my_char_2, 'N')
    <BLANKLINE>
    You cannot move in that direction...
    <BLANKLINE>
    False
    """
    lower_boundary = 1
    upper_boundary = 4
    original_position_x = char.get_coordinate()[0]
    original_position_y = char.get_coordinate()[1]
    char.move(direction)
    if char.coordinates[0] < lower_boundary or \
            char.coordinates[1] < lower_boundary or \
            char.coordinates[0] > upper_boundary or \
            char.coordinates[1] > upper_boundary:
        char.set_coordinate([original_position_x, original_position_y])
        print('\nYou cannot move in that direction...\n')
        return False
    else:
        return True


if __name__ == "__main__":
    doctest.testmod()
