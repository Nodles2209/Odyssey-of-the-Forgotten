"""
This file holds the main game code and is the file that is run to start playing the game, It also holds functions useful for running
in the main codes for loop
"""

from map import Map  # imports the class used for the map/map creation
from player import Player  # imports the player class used for holding data on the player
from normalise_function import normalise_input, whitelist  # imports the function used for normalising the players input, and the whitelist for removing words
from room_initialisation import create_rooms


def check_win():
    """
    This function will return True or False on whether the player has completed the game or not.
    The function itself will hold the conditions on how the player can win

    """

    return False


def print_room(current_room):
    """
    This function prints the id of the current room and prints the items too,
    takes in the current room the player is in

    """

    print(current_room.get_id())    #prints the name of the room

    # prints the items in the room if there are any
    if current_room.get_items() != []:
        print("The items in the room are:")
        for item in current_room.get_items():
            print("-",item.get_id())


def print_player_options(current_room, player):
    """
    This function takes in the current_room object and the player object and will print the options the player has in this room

    """
    pass

def execute_go(game_map, player, player_action):
    """
    This function takes in the game_map, player, and player_action,
    it changes the players location if the exit inputed exists
    """

    direction = player_action[1]

    if player.current_room.get_exit(direction) is None: #checks if the exit exists
        print('There is no room in that direction')
        return None

    player.current_room = player.current_room.get_exit(
        player_action[1])  # update the players current room to the desired room

    player.current_room.set_visited(True)  # sets the status of the room as visited when the player enters

def execute_take(game_map, player, player_action):
    """
    This function takes in the game_map, player, and player_action,
    it adds items from the current room to the players inventory if exists
    """
    
    item = game_map.items[player_action[1]] #sets the players inputted item to variable

    # is the item exists in the current room, take it and remove it from the room
    if item in player.current_room.get_items():
        player.inventory.append(item)
        player.current_room.remove_item(item)
    else:
        print("Item not in this room, please pick another")

def execute_drop(game_map, player, player_action):
    """
    This function takes in the game_map, player, and player_action,
    it drops items in the players inventory
    """

    item = game_map.items[player_action[1]] #sets the players inputted item to variable

    # if the item exists in the players inventory, drop it in the room
    if item in player.inventory:
        player.inventory.remove(item)
        player.current_room.add_item(item)
    else:
        print("This object is not found in your inventory")

def execute_inspect(game_map, player, player_action):
    """
    This function takes in the game_map, player, and player_action,
    it inspects and item or room the player specified
    """

    inspect_object = player_action[1]   #sets the players inputted item to variable

    # if the item is found in the maps item list and in the players inventory
    if inspect_object in game_map.items:
        item = game_map.items[inspect_object]
        if item in player.inventory:
            item.inspect(game_map, player)  # use the inspect command from the items.py file
        else:
            print("This item is not found in your inventory")
    elif inspect_object == "room":
        player.current_room.inspect()
    else:
        print("This is not a valid command")

def execute_action(game_map, player, player_action):
    """
    This function takes in the game_map object, the player object and the input from the player after it has been
    normalised.
    The function expects the first word to be the action eg "go" and the second word to be things like direction eg
    "North"
    """

    try:
        if player_action[0] == "go":  # if the first word in the input is "go"
            execute_go(game_map, player, player_action)
        elif player_action[0] == "take":
            execute_take(game_map, player, player_action)
        elif player_action[0] == "drop":
            execute_drop(game_map, player, player_action)
        elif player_action[0] == "inspect":
            execute_inspect(game_map, player, player_action)
        else:
            print('Please enter a keyword [go|take|drop] before your action')

    except IndexError:
        print('This is not a valid command')


def main():
    """
    this function handles the main part of the code and is the first function to be done when the  file is run,
    it also holds the initialisation of the entrance room (temporary) and  while loop for the main game
    """

    print("-" * 100)  # prints a long line across the screen just to make it easier to read for thr player
    print("Welcome to the game!!!!")

    game_map = Map()  # creates a map object

    required_room_list, optional_room_list, items_dictionary = create_rooms()  # gets the required and optional room list from the create_rooms function located in rooms_initialisation.py

    # Adds all the items in the game to the whitelist for normalising the input
    for item in items_dictionary:
        whitelist.append(item)

    game_map.init_gen_map(required_room_list, optional_room_list)  # This function runs the randomisation process to put all the room objects in place
    game_map.items = items_dictionary   #sets the items variable in the map object as a dictionary of all items {"id" : item_object}

    player_name = input("Please enter your name: ")  # gets the player to input their name
    player = Player(player_name, game_map.rooms["Entrance"])  # creates a player object with the name, and the entrance room object

    while True:  # This is the main while loop for the game that will run until the game is complete
        if check_win():  # This is where the game checks if the game has been completed at the start of each turn
            """
            Instead of printing a message here, a function can be called to determine which ending to print (importing
            the function from another file called endings.py; the player's final score can be parsed into the function)
            
            """

            print("You Win! wooohoo!!")
            break  # breaks out of while loop

        print('You are currently in the ', end='')
        print_room(player.current_room)  # prints the id of the current room

        print_player_options(player.current_room, player)  # prints the options has in the room

        player_action = input("You choose to: ")  # Gets the player to input their choice of the options

        print("-" * 100, "\n")  # prints a line and empty line for easier readablity

        player_action = normalise_input(player_action, whitelist)  # this normalises the players input to make it ready for the execute_action function

        execute_action(game_map, player, player_action)  # executes the players action, eg 'go north'


if __name__ == "__main__":  # checks this file is being run itself, and is not being imported elsewhere
    main()
