"""Module for functions related to combat mechanics."""
# Leon Lee
# BCIT
# A01062166

import character
import die
import enemy
import save_and_load


def combat(char):
    """Simulate an entire combat round between the player and enemy.

    Combat will continue until either the player's HP reaches 0 or enemy's HP reaches 0. The player's kill count will
    increase by one when the enemy is killed. If a player is killed they will be asked if they want to restart or quit.
    PARAM: An instance belonging to the class 'Character'.
    PRECONDITION: The parameter must be an instance belonging to the class 'Character'.
    POSTCONDITION: If the enemy is killed, kill count increases by one. If player is killed,
    ask if they want to restart or quit.
    RETURN: N/A
    """
    victim = enemy.Child(5)
    print("\n" + char.get_name() + "'s HP = " + str(char.get_health()))
    print("Child's HP = " + str(victim.get_health()))
    char.attack(victim)
    print('\nYou stab the screaming child and do ' + str(char.get_damage()) + ' damage.')
    if victim.get_health() <= 0:
        victim.set_zero_health()
        # Resets enemy HP to 0 if player damage > remaining enemy HP
        print('She has ' + str(victim.get_health()) + ' health points left...')
        print("You find the scent of fresh blood oddly aromatic")
        print("-------------------------------------------------------------------------------")
        char.add_kill()
        # Adds one to player kill count
        return
    else:
        print('She has ' + str(victim.get_health()) + ' health points left...')
        victim.attack(char)
        print('The child shoots you with a nail gun and does ' + str(victim.get_damage()) + ' damage.')
        if char.get_health() <= 0:
            char.set_zero_health()
            # Resets player HP to 0 if enemy damage > remaining human HP
            print('You have ' + str(char.get_health()) + ' health points left')
            print("You have been killed by a child. What kind of serial killer are you? Game Over.\n")
            print("-------------------------------------------------------------------------------")
            while True:
                save_and_load.restart_or_quit()
                # Asks if player wants to play again or quit
        while char.get_health() > 0 and victim.get_health() > 0:
            print('You have ' + str(char.get_health()) + ' health points left')
            char.attack(victim)
            print('You stab the screaming child again and do ' + str(char.get_damage()) + ' damage.')
            if victim.get_health() <= 0:
                victim.set_zero_health()
                print('The child has ' + str(victim.get_health()) + " health points left...")
                print("You find the scent of fresh blood oddly aromatic")
                print("-------------------------------------------------------------------------------")
                char.add_kill()
                return
            else:
                print('The child has ' + str(victim.get_health()) + " health points left...")
                victim.attack(char)
                print('The child is persistent! She continues to shoot you with the '
                      'nail gun and does ' + str(victim.get_damage()) + ' damage.')
                if char.get_health() <= 0:
                    char.set_zero_health()
                    print('You have ' + str(char.get_health()) + ' health points left')
                    print("You have been killed by a child. You are not worthy to don the mask of Michael"
                          " Myers. Game Over\n")
                    print("-------------------------------------------------------------------------------")
                    while True:
                        save_and_load.restart_or_quit()


def chance_of_engagement(char):
    """Decide if an enemy encounter will take place.

    A die is rolled to decide chance of encounter, the higher the number of sides the lower the chance of encounter.
    The default chance of battle is 1 in 10 or 10%. If a one is rolled an enemy engagement will occur. If there is no
    enemy, regenerate health by one.
    PARAM: An instance belonging to the class 'Character'.
    PRECONDITION: The parameter must be an instance belonging to the class 'Character'.
    POSTCONDITION: An enemy encounter will take place or player health regenerates by one.
    RETURN: N/A
    """
    engagement_die = die.Die(10)
    engagement_chance = engagement_die.roll_die()
    if engagement_chance == 1:
        fight_or_run(char)
        # Enemy engages and player gets to choose
    else:
        char.regenerate_one_health()


def fight_or_run(char):
    """Let player choose to fight the enemy or run.

    Combat will take place if player input 'Fight'. Player will run if input is 'run'
    PARAM: An instance belonging to the class 'Character'.
    PRECONDITION: The parameter must be an instance belonging to the class 'Character'.
    POSTCONDITION: A battle will take place if player decides to fight or the player runs away.
    RETURN: N/A
    """
    victim = enemy.Child(5)
    print("-------------------------------------------------------------------------------\n")
    print('You encounter a scared child. She is armed. Will you run or fight?\n'
          'You currently have ' + str(char.get_health()) + ' health points.\n'
          'If you want to be a coward and run, this is your only chance.')
    while True:
        fight_or_ignore = input('(Enter "Fight" or "Run")\n').title()
        if fight_or_ignore == 'Fight':
            combat(char)
            break
        elif fight_or_ignore == 'Run':
            run_away(char, victim)
            break
        else:
            print("You have not entered a valid command.")


def run_away(char: character.Character, victim: enemy.Child):
    """Decide if the player will take damage when running away.

    A die is rolled to decide chance of damage, the higher the number of sides the lower the chance of damage.
    Default chance of damage is 1 in 4 or 25%. If a one is rolled the player will take 1 to 4 points of damage.
    PARAM: An instance belonging to the class 'Character' and an instance belonging the the class 'Child'.
    PRECONDITION: The parameters must be an instance belonging to the class 'Character' and the class 'Child'.
    POSTCONDITION: Either the player escapes unharmed or the player will take 1 to 4 points of damage.
    RETURN: N/A
    """
    print('\nYou walk away, the thought of killing a child was too much for you. But in her fear the child attempts to '
          'attack you!')
    damage_die = die.Die(10)
    chance_of_damage = damage_die.roll_die()
    if chance_of_damage == 1:
        victim.escape_attack(char)
        # Enemy attacks character. Escape damage range from 1 - 4
        print("You have escaped, but have taken " + str(victim.get_escape_damage()) +
              " points of damage in the process. You now have " + str(char.get_health()) + " health points remaining.")
    else:
        print("You have escaped unscathed, the child runs off into the darkness.")
