from puzzle_data import *
from chess_boards import *

entrance = {
    # Name of room (String)
    "id": "Entrance",
    # Shortened name for displaying map, might add a map legend to the display map function later (String) (2 letters
    # or digits long)
    "map_id": "En",
    # Type of room (eg "basic", "riddle", "puzzle", "event") (String)
    "type": "basic",
    # visited (Only the rooms you want to appear immediately should this be set to True) (Boolean)
    "visited": True,
    # required room. 0 if optional room. 1-2-3-4.. for the order after that for required rooms (entrance begins as
    # 1), necessary for map creation (Int)
    "required": 1,
    # score given to player upon completion of room (Int)
    "complete_room_score": 1000,
    # List of items in room as "id" of the item (List[item_id])
    "item_list": ["map"],
    # Clear condition that is checked with the user input to see if rooms task is complete, set to True if checking completion in own function
    "clear_condition": True,
    # If the room is locked or not to the player, None if not locked, if locked put the id of the item to unlock it
    "locked" : None,
    # item given to you if you complete the puzzle, None if there isnt one
    "complete_item": None,
    # The first prompt that appears when the player enters the room for the first time, things like what the room is
    # and what it looks like (String)
    "first_prompt": None,
    # The prompt that appears when the player enters the room for all times after the first time (String)
    "enter_prompt": "You are back in the room you woke up in",
    # Hint (doesnt always apply) (String)
    "hint_prompt": "Find all the parts for the plane in other places around the map",
    # prompt for when the player completes the room (String)
    "complete_prompt": "You completed this room...."
}

key_room = {
    # Name of room (String)
    "id": "Key room",
    # Shortened name for displaying map, might add a map legend to the display map function later (String) (2 letters
    # or digits long)
    "map_id": "K1",
    # Type of room (eg "basic", "riddle", "puzzle", "event") (String)
    "type": "basic",
    # visited (Only the rooms you want to appear immediately should this be set to True) (Boolean)
    "visited": False,
    # required room. 0 if optional room. 1-2-3-4.. for the order after that for required rooms (entrance begins as
    # 1), necessary for map creation (Int)
    "required": 2,
    # score given to player upon completion of room (Int)
    "complete_room_score": 0,
    # List of items in room as "id" of the item (List[item_id])
    "item_list": ["key"],
    # Clear condition that is checked with the user input to see if rooms task is complete, set to True if checking completion in own function
    "clear_condition": True,
    # If the room is locked or not to the player, None if not locked, if locked put the id of the item to unlock it
    "locked" : None,
    # item given to you if you complete the puzzle, None if there isnt one
    "complete_item": None,
    # The first prompt that appears when the player enters the room for the first time, things like what the room is
    # and what it looks like (String)
    "first_prompt": "You enter a room, i wonder if something useful is here",
    # The prompt that appears when the player enters the room for all times after the first time (String)
    "enter_prompt": "You are back the room you found that key",
    # Hint (doesnt always apply) (String)
    "hint_prompt": None,
    # prompt for when the player completes the room (String)
    "complete_prompt": None
}

riddle1 = {
    # Name of room (String)
    "id": "Riddle room 1",
    # Shortened name for displaying map, might add a map legend to the display map function later (String) (2 letters
    # or digits long)
    "map_id": "R1",
    # Type of room (eg "basic", "riddle", "puzzle", "event") (String)
    "type": "riddle",
    # visited (Only the rooms you want to appear immediately should this be set to True) (Boolean)
    "visited": False,
    # required room. 0 if optional room. 1-2-3-4.. for the order after that for required rooms (entrance begins as
    # 1), necessary for map creation (Int)
    "required": 0,
    # score given to player upon completion of room (Int)
    "complete_room_score": 1000,
    # List of items in room as "id" of the item (List[item_id])
    "item_list": [],
    # Clear condition that is checked with the user input to see if rooms task is complete, set to True if checking completion in own function
    "clear_condition": "footsteps",
    # If the room is locked or not to the player, None if not locked, if locked put the id of the item to unlock it
    "locked" : None,
    # item given to you if you complete the puzzle, None if there isnt one
    "complete_item": None,
    # The first prompt that appears when the player enters the room for the first time, things like what the room is
    # and what it looks like (String)
    "first_prompt": "You enter a room, there are some weird markings on the wall, you take a closer look and it looks like a riddle\nIt says 'The more you take the more you leave behind'\nEnter your answer to complete the room",
    # The prompt that appears when the player enters the room for all times after the first time (String)
    "enter_prompt": "You enter back into the room with the riddle",
    # Hint (doesnt always apply) (String)
    "hint_prompt": "This riddle is all about your journey, and what you do as you move forward.",
    # prompt for when the player completes the room (String)
    "complete_prompt": "You completed the riddle, Great Job"
}

sudoku = {
    # Name of room (String)
    "id": "Sudoku Room",
    # Shortened name for displaying map, might add a map legend to the display map function later (String) (2 letters
    # or digits long)
    "map_id": "S1",
    # Type of room (eg "basic", "riddle", "puzzle", "event", "sudoku" ect) (String)
    "type": "sudoku",
    # visited (Only the rooms you want to appear immediately should this be set to True) (Boolean)
    "visited": False,
    # required room. 0 if optional room. 1-2-3-4.. for the order after that for required rooms (entrance begins as
    # 1), necessary for map creation (Int)
    "required": 3,
    # score given to player upon completion of room (Int)
    "complete_room_score": 1000,
    # List of items in room as "id" of the item (List[item_id])
    "item_list": [],
    # Clear condition that is checked with the user input to see if rooms task is complete, set to True if checking completion in own function
    "clear_condition": sudoku1_complete,
    # If the room is locked or not to the player, None if not locked, if locked put the id of the item to unlock it
    "locked" : "key",
    # item given to you if you complete the puzzle, None if there isnt one
    "complete_item": "wing",
    # The first prompt that appears when the player enters the room for the first time, things like what the room is
    # and what it looks like (String)
    "first_prompt": "You enter the room and behind some vines you find a weird puzzle on the wall,\nWeird, it looks just like sudoku",
    # The prompt that appears when the player enters the room for all times after the first time (String)
    "enter_prompt": "You are back in the room with the sudoku puzzle",
    # Hint (doesnt always apply) (String)
    "hint_prompt": "Find all the parts for the plane in other places around the map",
    # prompt for when the player completes the room (String)
    "complete_prompt": "You completed the puzzle, a small hatch opens and inside is an old wing for a plane",
    # stores incomplete puzzle data from puzzle data file
    "incomplete": sudoku1_incomplete
}

chess1 = {
    # Name of room (String)
    "id": "Chess Room",
    # Shortened name for displaying map, might add a map legend to the display map function later (String) (2 letters
    # or digits long)
    "map_id": "C1",
    # Type of room (eg "basic", "riddle", "puzzle", "event", "sudoku" ect) (String)
    "type": "chess",
    # visited (Only the rooms you want to appear immediately should this be set to True) (Boolean)
    "visited": False,
    # required room. 0 if optional room. 1-2-3-4.. for the order after that for required rooms (entrance begins as
    # 1), necessary for map creation (Int)
    "required": 4,
    # score given to player upon completion of room (Int)
    "complete_room_score": 2000,
    # List of items in room as "id" of the item (List[item_id])
    "item_list": [],
    # Clear condition that is checked with the user input to see if rooms task is complete, set to True if checking completion in own function
    "clear_condition": ['qe4e8', 're1xe8'],
    # If the room is locked or not to the player, None if not locked, if locked put the id of the item to unlock it
    "locked": None,
    # item given to you if you complete the puzzle, None if there isnt one
    "complete_item": None,
    # The first prompt that appears when the player enters the room for the first time, things like what the room is
    # and what it looks like (String)
    "first_prompt": "You enter the room and find strange glyphs,\nThe glyphs come together on a grid to resemble a chess board...",
    # The prompt that appears when the player enters the room for all times after the first time (String)
    "enter_prompt": "You are back in the room with the chess puzzle",
    # Hint (doesnt always apply) (String)
    "hint_prompt": "Find all the parts for the plane in other places around the map",
    # prompt for when the player completes the room (String)
    "complete_prompt": "You completed the puzzle....",
    # stores incomplete puzzle data from puzzle data file
    "board_turn": [chess_1_p1, chess_1_p2],
    "cutscenes": [chess_1_p1_cutscene, chess_1_p2_cutscene]
}


# A list used for holding all the room dictionaries in this file to be iterated through in the room_initialisation file
room_dict_list = [entrance, riddle1, key_room, sudoku, chess1]
#   !!!PLEASE MAKE SURE THE REQUIRED ROOMS IN THIS LIST ARE SORTED IN ORDER FROM SMALLEST TO LARGEST!!!
