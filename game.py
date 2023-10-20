"""
This file holds the main game code and is the file that is run to start playing the game, It also holds functions useful for running
in the main codes for loop
"""

from map import Map  # imports the class used for the map/map creation
from rooms import Room  # imports the class used for creating room objects and functions for setting and getting variables
from player import Player  # imports the player class used for holding data on the player


def check_win():
    """
    This function will return True or False on whether the player has completed the game or not.
    The function itself will hold the conditions on how the player can win

    """

    return False


def print_room(current_room):
    """
    This function prints the id of the current room, and takes in the current room the player is in

    """

    print(current_room.get_id())


def print_player_options(current_room, player):
    """
    This function takes in the current_room object and the player object and will print the options the player has in this room

    """

    print("This is where the players options he can choose will be printed")


def normalise_input(player_action):
    """
    This function takes in the players input and returns a normalised list of the important words the player entered,
    This function may later be moved to its own folder

    """

    input_list = player_action.split(" ")
    # This splits the players input into a list, by using a space character to split by

    return input_list  # returns a list of important words from the players input


def execute_action(game_map, player, player_action):
    """
    This function takes in the game_map object, the player object and the input from the player after it has been
    normalised.
    The function expects the first word to be the action eg "go" and the second word to be things like direction eg
    "North\"
    """
    if player_action[0] == "go":  # if the first word in the input is "go"
        player.current_room = player.current_room.get_exit(player_action[1])  # update the players current room to the desired room


def main():
    """
    this function handles the main part of the code and is the first function to be done when the  file is run,
    it also holds the initialisation of the entrance room (temporary) and  while loop for the main game
    """

    print("-" * 100)  # prints a long line across the screen just to make it easier to read for thr player
    print("Welcome to the game!!!!")

    game_map = Map()  # creates a map object
    entrance = Room()  # creates the entrance room object, then sets initial values in the next lines
    entrance.set_id("en")
    entrance.set_x(2)
    entrance.set_y(2)
    game_map.map_matrix[entrance.get_y()][entrance.get_x()] = entrance  # places entrance in map matrix
    game_map.rooms_in_map.append(entrance)  # places entrance in rooms list

    game_map.init_gen_map()  # This function runs the randomisation process of entering the rooms, may later need to take in a list of the rooms in future versions
    game_map.display_map()  # prints the map for the player, may need to be removed later

    player_name = input("Please enter your name: ")  # gets the player to input their name
    player = Player(player_name, entrance)  # creates a player object with the name, and the entrance room object

    while True:  # This is the main while loop for the game that will run until the game is complete
        if check_win():  # This is where the game checks if the game has been completed at the start of each turn
            print("You Win! wooohoo!!")
            break  # breaks out of while loop

        print_room(player.current_room)  # prints the id of the current room

        print_player_options(player.current_room, player)  # prints the options has in the room

        player_action = input("You choose to: ")  # Gets the player to input their choice of the options

        player_action = normalise_input(player_action)  # this normalises the players input to make it ready for the execute_action function

        execute_action(game_map, player, player_action)  # executes the players action, eg 'go north'


if __name__ == "__main__":  # checks this file is being run itself, and is not being imported elsewhere
    main()
