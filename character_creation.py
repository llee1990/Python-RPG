"""Module for functions relating to character creation."""
# Leon Lee
# BCIT
# A01062166
from character import Character
import dialogue_and_scripts
import save_and_load


def create_character():
    """Create a character.

    An instance of the class 'Character' will be created and returned.
    PARAM: N/A
    PRECONDITION: This function is only called when player decides to start a new game.
    POSTCONDITION: An instance of the class 'Character' will be returned.
    RETURN: If saved file corresponding to the chosen username is not found or the current saved file with the same
    username is overwritten return a new instance of the class 'Character'. If there is an existing saved file with
    the same name as the chosen username, return that character as the instance.
    """
    print('\n"Finally..a new soul dares to don the mask of Michael Myers. \nYou have big shoes to fill young'
          ' one..only those with a taste for blood \nare worthy of this mask...now tell '
          'me...what is your name?"\n')
    name = input("Enter your name:\n").title().strip()
    try:
        while True:
            with open(name + '.json'):
                answer = input("\nThere is already a saved file with this name, enter 'W' to overwrite the current "
                               "file or 'L' to load the saved game. (W / L)\n").title().strip()
                # Warns a player if a saved file under the same name already exists
                my_char = existing_character_detected(name, answer)
                # Overwrites existing character with a new character if "answer = 'W'"
                # Loads existing character if "answer = 'L'"
                return my_char
    except FileNotFoundError:
        # If no saved files were detected
        my_char = Character(name, 10, [1, 3], 0)
        save_and_load.save_game(my_char)
        # Create a new .json file for the new character.
        print("\n-------------------------------------------------------------------------------\n")
        print("My...my name is...")
        print(my_char.name + "...")
        dialogue_and_scripts.intro_script(my_char)
        # Prints the intro dialogue script for a new character.
        return my_char


def existing_character_detected(name: str, response: str):
    """Overwrite an existing character or load an existing character.

    PARAM: A string of the player's username
    PARAM: A string of the player's response whether they want to overwrite or load an existing character.
    PRECONDITION: This function is only called when the game detects an existing .json
    file with the same string as the 'name' value in the parameter.
    POSTCONDITION: An instance of the class 'Character' will be created.
    RETURN: An instance of the class 'Character' will be returned.
    """
    if response == 'W':
        my_char = Character(name, 10, [1, 3], 0)
        print("\nMy...my name is...")
        print(my_char.name + "...")
        dialogue_and_scripts.intro_script(my_char)
        # Print intro script for new character
        return my_char
    elif response == 'L':
        my_char = save_and_load.load_game(name)
        # Loads a saved character file
        return my_char
    else:
        print("That is not a valid command.\n")
