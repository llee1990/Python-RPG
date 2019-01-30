"""Halloween - The Mask of Michael Myers"""
# Leon Lee
# BCIT
# A01062166

import character
import combat
import character_creation
import dialogue_and_scripts
import map_and_movement
import save_and_load
import sys


def start_game():
    """Display title image and start game options.

    Lets user choose to start a new game or load a saved file.
    PARAM: N/A
    PRECONDITION: N/A
    POSTCONDITION: Whether a player starts a new game or loads a saved file, an instance of the class 'Character'
    will be returned. Game will exit if player enters 'N' when the game asks if the user is over 18.
    RETURN: An instance of the class 'Character' will be returned.
    """
    dialogue_and_scripts.game_graphic()
    # Displays intro graphic
    while True:
        age = input("DISCLAIMER: This game is rated 'M' for MATURE, are you over 18? (Y / N)\n").upper().strip()
        if age == 'Y':
            while True:
                start_input = input("\nWelcome to Halloween - The Mask of Michael Myers. "
                                    "\nEnter 'N' to start a new game or 'L' to load a saved file. "
                                    "(N / L)\n").upper().strip()
                if start_input == 'L':
                    name = input('\nWhat is your user name?:\n').title().strip()
                    my_char = save_and_load.load_game(name)
                    # Loads a saved character .json file
                    if my_char is False:
                        continue
                        # Goes back to beginning of game if there is no saved file
                    else:
                        return my_char
                elif start_input == 'N':
                    while True:
                        my_char = character_creation.create_character()
                        # Creates a new character
                        return my_char
                else:
                    print('\nThat is not a valid command.')
        elif age == 'N':
            sys.exit()
            # Exits program if player confirms they are under 18 years old.
        else:
            print('\nThat is not a valid command.')


def game_loop(char: character.Character):
    """The main loop of the game.

    For each non-combat turn, this loop draws the game map, display map description for the coordinates the player
    is on, display player HP and number of kills, and asks which direction the player wants to move to.
    PARAM: An instance belonging to the class 'Character'.
    PRECONDITION: The parameter must be an instance belonging to the class 'Character'.
    POSTCONDITION: A character can only move to a position that is not a physical boundary. If a player chooses to
    quit, they can choose to save the game or quit without saving.
    RETURN: N/A.
    """
    print("-------------------------------------------------------------------------------\n")
    print("You find yourself in a dark house, the children are near...which way do you go?")
    while True:
        map_and_movement.draw_map(char)
        # Draws game map and character position
        dialogue_and_scripts.map_description(char)
        # Prints map dialogue
        print(dialogue_and_scripts.display_stats(char))
        # Prints player HP and number of kills
        directions = ['N', 'S', 'E', 'W']
        move_input = input("\nWhich direction would you like to go? (Enter 'Q' or 'Quit' to quit)\n").title().strip()
        print("-------------------------------------------------------------------------------")
        if move_input == 'Q' or move_input == 'Quit':
            save_and_load.choose_to_save(char)
            # Lets player decide if they want to save or not.
            sys.exit()
        elif move_input not in directions:
            print('\nThat is not a valid command.\n'
                  'Enter "N", "S", "E", or "W"')
        elif move_input in directions:
            character_move = map_and_movement.move_character(char, move_input)
            # Moves character to a new position on the map if True
            # Keeps character in the same position on the map if False
            if character_move is True:
                combat.chance_of_engagement(char)
                # Decides if an enemy will appear and engage the character
            if character_move is False:
                pass


def main():
    my_char = start_game()
    game_loop(my_char)


if __name__ == "__main__":
    main()
