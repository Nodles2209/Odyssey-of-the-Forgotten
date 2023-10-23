"""
This file holds the main game code and is the file that is run to start playing the game, It also holds functions useful for running
in the main codes for loop
"""

from map import Map  # imports the class used for the map/map creation
from rooms import Room  # imports the class used for creating room objects and functions for setting and getting variables
from player import Player  # imports the player class used for holding data on the player
from normalise_function import normalise_input, whitelist #imports the function used for normalising the players input, and the whitelist for removing words
from room_initialisation import create_rooms


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


def execute_action(game_map, player, player_action):
    """
    This function takes in the game_map object, the player object and the input from the player after it has been
    normalised.
    The function expects the first word to be the action eg "go" and the second word to be things like direction eg
    "North\"
    """
    if player_action[0] == "go":  # if the first word in the input is "go"
        player.current_room = player.current_room.get_exit(player_action[1])  # update the players current room to the desired room
        player.current_room.set_visited(True)   #sets the status of the room as visited when the player enters


def main():
    """
    this function handles the main part of the code and is the first function to be done when the  file is run,
    it also holds the initialisation of the entrance room (temporary) and  while loop for the main game
    """

    print("-" * 100)  # prints a long line across the screen just to make it easier to read for thr player
    print("Welcome to the game!!!!")

    game_map = Map()  # creates a map object

    required_room_list, optional_room_list = create_rooms() #gets the required and optional room list from the create_rooms function located in rooms_initialisation.py
    game_map.init_gen_map(required_room_list, optional_room_list)  # This function runs the randomisation process of entering the rooms, may later need to take in a list of the rooms in future versions

    player_name = input("Please enter your name: ")  # gets the player to input their name
    print(game_map.rooms)
    player = Player(player_name, game_map.rooms["Entrance"])  # creates a player object with the name, and the entrance room object

    while True:  # This is the main while loop for the game that will run until the game is complete
        if check_win():  # This is where the game checks if the game has been completed at the start of each turn
            print("You Win! wooohoo!!")
            break  # breaks out of while loop

        game_map.display_map(player)    #Displays the map at the start of every turn (use the player object as the argument)

        print_room(player.current_room)  # prints the id of the current room

        print_player_options(player.current_room, player)  # prints the options has in the room

        player_action = input("You choose to: ")  # Gets the player to input their choice of the options

        player_action = normalise_input(player_action, whitelist)  # this normalises the players input to make it ready for the execute_action function

        execute_action(game_map, player, player_action)  # executes the players action, eg 'go north'


if __name__ == "__main__":  # checks this file is being run itself, and is not being imported elsewhere
    main()
