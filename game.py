"""
This file holds the main game code and is the file that is run to start playing the game, It also holds functions useful for running
in the main codes for loop
"""

from map import Map  # imports the class used for the map/map creation
from player import Player  # imports the player class used for holding data on the player
from normalise_function import normalise_input, whitelist  # imports the function used for normalising the players input, and the whitelist for removing words
from room_initialisation import create_rooms


def check_win_items(win_objects, game_map, player):
    """
    This function will return True or False on whether the player can build the plane.
    The function takes the objects needed to win, the game map and the player

    """
    win_possible = True

    for item in win_objects:
        if game_map.items[item] not in player.inventory:
            win_possible = False

    if win_possible:
        if player.current_room.get_id() == "Entrance":
            return True
        else:
            print("You have all the parts for the plane now! Get back to the entrance to build it")

    return False




def print_room(current_room, player):
    """
    This function prints the id of the current room and prints the items too,
    takes in the current room the player is in

    """
    print(current_room.get_id())    #prints the name of the room


def print_player_options(game_map, current_room, player, win_possible):
    """
    This function takes in the game_map, current_room object and the player object and will print the options the player has in this room

    """
    print("\nHere are your options:")

    #Print option to build the plane
    if win_possible == True:
        print("Use 'BUILD plane' - to build the plane and leave the island (This completes the game)")
    # Printing the options for the directions the player can take
    if current_room.get_exit("north"):
        print("Use 'GO north' - to continue through the north exit")
    if current_room.get_exit("east"):
        print("Use 'GO east' - to continue through the east exit")
    if current_room.get_exit("south"):
        print("Use 'GO south' - to continue through the south exit")
    if current_room.get_exit("west"):
        print("Use 'GO west' - to continue through the west exit")

    # prints how to answer the riddle if in riddle room
    if current_room.get_type() == "riddle" and current_room.get_is_clear() == False:
        print("Use 'RIDDLE *answer' to enter your answer to the rooms riddle")
        print("Use 'RIDDLE hint' to get a hint for the riddle")

    # option for checking inventory
    print("Use 'INSPECT I' - to see your inventory")
    # option for inspecting room to see information or initaiate the task within
    print("Use 'INSPECT room' - to initiate a rooms task")
    #checks if the player has the map item and then prints the option of checking the map if he does
    map_item = game_map.items["map"]
    if map_item in player.inventory:
        print("Use 'INSPECT map' - to use your map to see visited rooms")
    # option for checking the players score
    print("Use 'CHECK score' - to see your current score")

    # prints the items in the room if there are any
    if current_room.get_items() != []:
        print("Use 'TAKE *name' to take these items from the room:")
        for item in current_room.get_items():
            print("  > 'TAKE",item.get_id() + "'")
    # option for dropping items
    print("Use 'DROP *name' to drop items from your inventory")


def execute_go(game_map, player, player_action):
    """
    This function takes in the game_map, player, and player_action,
    it changes the players location if the exit inputed exists
    """

    direction = player_action[1]

    if player.current_room.get_exit(direction) is None: #checks if the exit exists
        print('There is no room in that direction')
        return None

    if player.current_room.get_exit(player_action[1]).get_locked(): # checks if the room is locked
        print("This room is locked, go find the key and INSPECT it here")
    else:
        player.current_room = player.current_room.get_exit(player_action[1])  # update the players current room to the desired room
        player.current_room.set_visited(True)  # sets the status of the room as visited when the player enters

        if player.current_room.get_first_prompt():
            print(player.current_room.get_first_prompt(), "(" + player.current_room.get_id() + ")")
            player.current_room.set_first_prompt(None)
        else:
            print(player.current_room.get_enter_prompt())

def execute_take(game_map, player, player_action):
    """
    This function takes in the game_map, player, and player_action,
    it adds items from the current room to the players inventory if exists
    """
    
    item = game_map.items[player_action[1]] #sets the players inputted item to variable

    # is the item exists in the current room, take it and remove it from the room
    if item in player.current_room.get_items():
        player.inventory.append(item)
        player.score += item.get_score()
        player.current_room.remove_item(item)
        item.set_score(0)   #sets the score to 0 so the player wont get more points by picking up the item again
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
    current_room = player.current_room  #sets the current room the player is in

    # Checks if the player wants to print their inventory
    if inspect_object == "i" or inspect_object == "inventory":
        player.print_inventory()
    # if the item is found in the maps item list and in the players inventory
    elif inspect_object in game_map.items:
        item = game_map.items[inspect_object]
        if item in player.inventory:
            if item.get_id() == "map":  # if inspecting the map, the display_map() function is run
                game_map.display_map(player)
            else:
                item.inspect(game_map, player)  # use the inspect command from the items.py file
        else:
            print("This item is not found in your inventory")

    # checks if the player is trying to inspect a room
    elif inspect_object == "room":
        room_type = current_room.get_type()
        if current_room.get_is_clear(): #checks if the room has already been completed
            print("You have already completed this room")
        elif room_type == "riddle": # this will handle the code for riddle rooms
            pass
        elif room_type == "event":  # this will handle the code for event rooms
            pass
        elif room_type == "sudoku": # this handles the code for the sudoku room
            current_room.set_is_clear(current_room.run_sudoku())
        else:
            print("This room does not have a task")
        
        # checks if the room has been completed and gets the player his score if they have
        if current_room.get_is_clear():
            player.score += current_room.get_complete_score()
            current_room.set_complete_score(0)  # sets the score of the room to 0 so they cannot get the same reward twice
            print(current_room.get_complete_prompt())
            if current_room.get_complete_item():
                item_id = current_room.get_complete_item()
                player.inventory.append(game_map.items[item_id])
                print("You won a", item_id, "for completing the puzzle")
                current_room.set_complete_item(None)

    else:
        print("This is not a valid command")


def execute_check(player, player_action):
    # This function takes a player and plaayer_action, it handles any checks like checking score the player wants to complete 
    if player_action[1] == "score":
        print("Your score is currently:",player.score, "\n")
    else:
        print("This is not a valid command")

def execute_riddle(game_map, player, player_action):
    #This function holds the checks to complete the riddle
    if player.current_room.get_is_clear():  #checks if the riddle is complete
        print("You have already completed this riddle!")
        return

    players_answer = player_action[1]   #gets the players second word entered

    if players_answer == "hint":    #checks if a player wants a hint
        print(player.current_room.get_hint_prompt())
    #checks if the players answer is correct
    elif players_answer == player.current_room.get_clear_condition():   
        player.current_room.set_is_clear(True)
        print(player.current_room.get_complete_prompt())
        player.score += player.current_room.get_complete_score()
        player.current_room.set_complete_score(0)  # sets the score of the room to 0 so they cannot get the same reward twice
        # checks if the room has an object for completing the puzzle
        if player.current_room.get_complete_item():
            item_id = player.current_room.get_complete_item()
            player.inventory.append(game_map.items[item_id])
            print("You won a", item_id, "for completing the puzzle")
            player.current_room.set_complete_item(None)
    else:   #if the player gets the answer wrong
        print("This answer was wrong, try again or get a hint")


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
        elif player_action[0] == "check":
            execute_check(player, player_action)
        elif player_action[0] == "riddle":
            execute_riddle(game_map, player, player_action)
        elif player_action[0] == "build":
            execute_win(player)
        else:
            print('Please enter a keyword [go|take|drop|inspect|check] before your action')

    except IndexError:
        print('This is not a valid command or your answer is wrong')


def execute_win(player):
    """
    This function is holding the code that is run when the game is completed, takes in the player object
    """
    print("Congratulations", player.name, "!, You are preparing to take off on your new makeshift plane\n")

    if player.score >= 5000:
        print("You were just about to take off when you notice something shiny in the bushes beside you")
        print("You found a DIAMOND, the largest one the world has ever seen!")
        print("You stuff your riches into your pocket and fly off into the sunset :)\n")
        print("You achieved the LUCKY ending! Congratulations!!!!!")
    else:
        print("You take a big run up and fly off in your makeshift plane")
        print("Finally escaping and returning home")
        print("But where is home? Can you even remember?...")
        print("Anyway you are free!!!!\n")
        print("You achieved the REGULAR ending")

    print("\nYour score was:", player.score)
    player.won_game = True




def main():
    """
    this function handles the main part of the code and is the first function to be done when the  file is run,
    it also holds the initialisation of the entrance room (temporary) and  while loop for the main game
    """

    print("-" * 100)  # prints a long line across the screen just to make it easier to read for thr player
    print("Welcome to the game!!!!")

    game_map = Map()  # creates a map object

    win_objects = ["wing"]  #the items the player needs in their inventory to build the plane

    required_room_list, optional_room_list, items_dictionary = create_rooms()  # gets the required and optional room list from the create_rooms function located in rooms_initialisation.py

    # Adds all the items in the game to the whitelist for normalising the input
    for item in items_dictionary:
        whitelist.append(item)

    game_map.init_gen_map(required_room_list, optional_room_list)  # This function runs the randomisation process to put all the room objects in place
    game_map.items = items_dictionary   #sets the items variable in the map object as a dictionary of all items {"id" : item_object}

    player_name = input("Please enter your name: ")  # gets the player to input their name
    player = Player(player_name, game_map.rooms["Entrance"])  # creates a player object with the name, and the entrance room object

    while player.won_game == False:  # This is the main while loop for the game that will run until the game is complete
        win_possible = check_win_items(win_objects, game_map, player)  # This is where the game checks if the player has the objects to build the plane, returns true if the player can get the option to build plane

        print_player_options(game_map, player.current_room, player, win_possible)  # prints the options has in the room

        player_action = input("You choose to: ")  # Gets the player to input their choice of the options

        print("-" * 100, "\n")  # prints a line and empty line for easier readablity

        player_action = normalise_input(player_action, whitelist)  # this normalises the players input to make it ready for the execute_action function

        execute_action(game_map, player, player_action)  # executes the players action, eg 'go north'


if __name__ == "__main__":  # checks this file is being run itself, and is not being imported elsewhere
    while True:
        print("-" * 100)
        print("\nplease type 'START' to start the game")
        print("Or type 'EXIT' to exit the game")
        start_input = input("Decide here: ").strip().lower()
        if start_input == "start":
            main()
        elif start_input == "exit":
            break
        else:
            print("Please type a valid command")
