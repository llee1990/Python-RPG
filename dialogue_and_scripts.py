"""Module for functions related to game dialogue and scripts."""
# Leon Lee
# BCIT
# A01062166
import character


def game_graphic():
    """Print intro graphic when starting game.

    PARAM: N/A
    PRECONDITION: N/A
    POSTCONDITION: N/A
    RETURN: N/A
    """
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@@@@@@@@&@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@&@@@@&@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&((*,...,,,,,,,,,,,**#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@&@&/,.........,,,,,,,,,,,*///#&@@@@@@&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@&/...........,,,,,,,,,,,,*/////(&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@&&,............,,,,,,,,,,,,,,//////(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@&*..............,,,,,,,,,,,,////////(&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@&*.................,,,,,,,,*//////////(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@&....................,,,,,/////////////(&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@&..................,,,,,,*//////////////(&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@.........,,**,,.,///////////////////////(&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@.....,,,,******/(/,,**/(/((((////////////(@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@#/////((*,,,,*/*.....,*/////(((////////////(%#%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@/**(##/,,,,,,////&@@@@@@@@#*///////////////(#%%%(%@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@/@@@@@@,,,,,///*/(@@@@@@@@@@,*/////////////(#%#(/#&@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@/%@@@#*,,,,////////%@@@@@@@%////////////////#(///(%@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@#,*(*,,,,,///////////(###///////////////////%%%#//%@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@%,,,,,,,,,////#%((////*****/////////////////%&%%(/%@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@%,,,,,***/////,*%%%(///////////////////////(&&%%((%@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@,,,*/#&&(((/////#%%%(/////////////////////(####/#&@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@/**/(%&&/&&%((%%#/////////(((///////(//(#(//(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@%*/(,...,##*///////(%%(/////((/////////(/(%#(((%@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@%*.........*//////////(((((///////////(/#%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@&............////////////////////////((//((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@../%%%/(%%%((#(((///////////////////(////(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@./@@@@@@@@@@@@@@@@#///////////////((//////%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@...,*(%#%#%%%%%%%%#/////////////((%%%(////(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@.,**/(%%#(((*//////////////////(#%%#(//////@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@/****/****/((/////////////////#%%#/////////%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@%**,,,,,,,,,*////////(((/((#%%%(//////////(&@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@%/,,,,,,**///////(%%%%%%%%%%%#////////////#@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%/****//////((%%%%%%%%%%%%%(////////////(@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%/#%%%%%%%%%%##%%%%%%%%%%%%///////////#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*///(%%%%%%%%%%%%%%%%%%%%%(///////(#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%**////(%%%%%%%%%%%%%%%%%%%%%%%%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#//////(#%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%%%%%%%%%%%%&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print("\n---------------------------------------------------------------------------------------------------")


def intro_script(player: character.Character):
    """Print introduction dialogue for new game.

    The script will refer to player by their username.
    PARAM: An instance belonging to the class 'Character'.
    PRECONDITION: The parameter must be an instance belonging to the class 'Character'.
    POSTCONDITION: N/A
    RETURN: N/A
    """
    print("\n\"Good...listen to me..." + player.get_name() + ". This is the voice of the mask. \nI was the voice "
          "that guided Michael Myers and I will be the voice that guides you.\nThis Halloween has been fruitful for "
          "us.I have lured many children with candy and \nthey are trapped in this house. Kill them to show your "
          "worth.\n")
    print(input('Press "Enter" to continue\n'))
    print("-------------------------------------------------------------------------------\n")
    print('Just say "N for North", "S for South", "E for East", or "W for West" '
          'and I will guide you to that direction...\n')
    print(input('Press "Enter" to continue'))


def intro_script_load_game(player: character.Character):
    """Print introduction dialogue for loaded game.

    The script will refer to player by their username.
    PARAM: An instance belonging to the class 'Character'.
    PRECONDITION: The parameter must be an instance belonging to the class 'Character'.
    POSTCONDITION: N/A
    RETURN: N/A
    """
    print("-------------------------------------------------------------------------------\n")
    print("\nWelcome back " + player.get_name() + ". I see you could not resist your lust for blood. That's "
                                                  "right...\nonce you wear this mask you become trapped in its curse..."
                                                  "there are still \nchildren hiding in this house. Kill them. "
                                                  "Killing children is fun, isn't it? \n\nJust say \"N for North\", "
                                                  "\"S for South\", \"E for East\", or \"W for West\" and I "
                                                  "will guide you to that direction...\n")


def map_description(char: character.Character):
    """Print map description for the coordinate the player is currently on.

    PARAM: An instance belonging to the class 'Character'.
    PRECONDITION: The parameter must be an instance belonging to the class 'Character'.
    POSTCONDITION: N/A
    RETURN: N/A
    """
    print('')
    map_script = {(1, 1): "You are at the northwest corner of the house. You feel weird facing a corner.",
                  (1, 2): "You enter the living room, looks like a cozy home...",
                  (1, 3): "This is the entrance to the house. Through the shadows you can "
                          "see the living room to your west and a small bedroom to your east.",
                  (1, 4): "This is a bedroom, it is small. Perhaps it belonged to a child.",
                  (2, 1): "Snacks and tea are on the living room table, the tea is still steaming...",
                  (2, 2): "There is a big TV in this living room. You stop and stare into the reflection.\n"
                          "A masked figure mask stares back.",
                  (2, 3): "You are near the center of the house, a photo of a family hangs on the wall. "
                          "Where can they be hiding...",
                  (2, 4): "This bedroom is small, there is a bunk bed against the wall littered with stuffed animals.",
                  (3, 1): "You are between the living room and the kitchen. A small window overlooks the garden.",
                  (3, 2): "You are between the living room and the kitchen. The living room is to your north"
                          " and to the south is the kitchen.",
                  (3, 3): "You look around the house, to the south is the master bedroom.",
                  (3, 4): "You look outside the window, there is a full moon tonight.",
                  (4, 1): "You enter the kitchen and opened one of the cabinets, "
                          "considering to choose another weapon.\n"
                          "You decided to stick with the kitchen knife.",
                  (4, 2): "You look around and open the refrigerator, there are some leftover spaghetti and meatloaf.",
                  (4, 3): "This is the master bedroom. There is a king-sized bed with maroon bedsheets."
                          "They smelled like they had just been changed.",
                  (4, 4): "You open the walk-in closet in the master bedroom. Perhaps they are hiding here..."}
    for position, dialogue in map_script.items():
        if char.get_coordinate()[0] == position[0] and char.get_coordinate()[1] == position[1]:
            print(dialogue)


def display_stats(char: character.Character):
    """Display current health points and how many enemies the player has killed.

    PARAM: An instance belonging to the class 'Character'.
    PRECONDITION: The parameter must be an instance belonging to the class 'Character'.
    POSTCONDITION: The current HP of the player and the number of enemies the player has killed will be printed.
    RETURN: N/A.
    """
    counter_kills = char.get_kill_count()
    if counter_kills == 1:
        return '\nYour current HP is ' + str(char.get_health()) + \
               '.\nYou have killed ' + str(counter_kills) + ' child.'
    else:
        return '\nYour current HP is ' + str(char.get_health()) + \
               '.\nYou have killed ' + str(counter_kills) + ' children.'
