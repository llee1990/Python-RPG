"""Module for functions related to saving and loading game."""
# Leon Lee
# BCIT
# A01062166

import character
import comp_1510_a1
import dialogue_and_scripts
import json
import os
import sys


def load_game(name: str):
    """Load a character file.

    Will load a character if there is a .json file with the same name string as the parameter.
    PARAM: A string with the player's username.
    PRECONDITION: The parameter must be a string.
    POSTCONDITION: Saves a character's name, health points, coordinates, and number of kills as an instance of the
    class "Character" and return it.
    RETURN: If there is an existing .json file, return that character instance. If file is not found,
    return boolean False.
    """
    file_name = name + ".json"
    try:
        with open(file_name) as file_object:
            saved_data = json.load(file_object)
            my_char = character.Character(saved_data['name'], saved_data['health'], saved_data['coordinates'],
                                          saved_data['kills'])
            # Creates an instance of the character class using the saved dictionary in the .json file
            dialogue_and_scripts.intro_script_load_game(my_char)
            # Prints the dialogue for a loaded game
            return my_char
    except FileNotFoundError:
        print('\nSorry, you do not have a saved file.')
        return False


def save_game(char: character.Character):
    """Save a character file.

    Will save a character into a .json file using the value of the 'name' attribute instance in the parameter.
    PARAM: An instance of the class "Character".
    PRECONDITION: The parameter must be an instance from the class "Character".
    POSTCONDITION: Saves a character's name, health points, coordinates, and number of kills into a .json file
    RETURN: N/A
    """
    file_name = char.get_name() + ".json"
    saved_data = {'name': char.get_name(),
                  'health': char.get_health(),
                  'coordinates': char.get_coordinate(),
                  'kills': char.get_kill_count()}
    with open(file_name, 'w') as file_object:
        json.dump(saved_data, file_object)


def choose_to_save(char):
    """Let player choose to save or not.

    The game will save if input is 'Y' and not save if input is 'N'.
    PARAM: An instance belonging to the class 'Character'.
    PRECONDITION: The parameter must be an instance belonging to the class 'Character'.
    POSTCONDITION: Either the game saves or does not save.
    RETURN: N/A.
    """
    print('\nQuitting so soon..? I am disappointed at your lack of bloodlust.\n'
          'You are not fit to wear this mask...\n')
    while True:
        save = input('Would you like to save your game? If you choose no, \nany older saved files under the same user '
                     'name will also be deleted. (Y / N)\n').title()
        if save == 'Y':
            save_game(char)
            return
        elif save == 'N':
            do_not_save(char)
            return
        else:
            print('That is not a valid command.')


def do_not_save(char: character.Character):
    """Do not save a character file.

    Will delete a .json file with the same 'name' value as the instance in the parameter.
    PARAM: An instance of the class "Character".
    PRECONDITION: The parameter must be an instance from the class "Character".
    POSTCONDITION: Removes the .json file associated with the name of a character.
    """
    file_name = char.get_name() + '.json'
    os.remove(file_name)
    # Removes .json file associated with current character


def restart_or_quit():
    """Let the player choose between playing again or exiting the game.

    PARAM: N/A
    PRECONDITION: This function is only called when an user dies or quits the game.
    POSTCONDITION: Either the main() game function is called again to restart the game or the game exits.
    RETURN: N/A.
    """
    choice_to_play_again = input("\nWould you like to play again? (Y / N)\n").title()
    if choice_to_play_again == 'Y':
        comp_1510_a1.start_game()
        # Restarts game
    elif choice_to_play_again == 'N':
        sys.exit()
        # Exits game
    else:
        print('That is not a valid command.')