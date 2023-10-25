from puzzle_data import *
from chess_boards import *
import random

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

event1 = {
    # Name of room (String)
    "id": "Event room 1",
    # Shortened name for displaying map, might add a map legend to the display map function later (String) (2 letters
    # or digits long)
    "map_id": "E1",
    # Type of room (eg "basic", "riddle", "puzzle", "event") (String)
    "type": "event",
    # visited (Only the rooms you want to appear immediately should this be set to True) (Boolean)
    "visited": False,
    # required room. 0 if optional room. 1-2-3-4.. for the order after that for required rooms (entrance begins as
    # 1), necessary for map creation (Int)
    "required": 2,
    # score given to player upon completion of room (Int)
    "complete_room_score": -300,
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
    "first_prompt": "You enter into the room and notice something wedged in the wall,\n do you want to try and yank at it?",
    # The prompt that appears when the player enters the room for all times after the first time (String)
    "enter_prompt": None,
    # Hint (doesnt always apply) (String)
    "hint_prompt": None,
    # prompt for when the player completes the room (String)
    "complete_prompt": "You pull at it and find... A SMELLY SOCK! YUCK!",
    #luck, only set to false if is the bad room
    "luck": None
}

event2 = {
    # Name of room (String)
    "id": "Event room 2",
    # Shortened name for displaying map, might add a map legend to the display map function later (String) (2 letters
    # or digits long)
    "map_id": "E2",
    # Type of room (eg "basic", "riddle", "puzzle", "event") (String)
    "type": "event",
    # visited (Only the rooms you want to appear immediately should this be set to True) (Boolean)
    "visited": False,
    # required room. 0 if optional room. 1-2-3-4.. for the order after that for required rooms (entrance begins as
    # 1), necessary for map creation (Int)
    "required": 0,
    # score given to player upon completion of room (Int)
    "complete_room_score": 500,
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
    "first_prompt": "You enter the room and see a mouse trapped under a rock,\n do you want to help it?",
    # The prompt that appears when the player enters the room for all times after the first time (String)
    "enter_prompt": None,
    # Hint (doesnt always apply) (String)
    "hint_prompt": None,
    # prompt for when the player completes the room (String)
    "complete_prompt": "The mouse leaps free and leads you to a little hole, inside you find GOLD!",
    #luck, only set to false if is the bad room
    "luck": None
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
    "first_prompt": "You enter a room, there are some weird markings on the wall, you take a closer look and it looks like a riddle\nIt says 'The more you take the more you leave behind'",
    # The prompt that appears when the player enters the room for all times after the first time (String)
    "enter_prompt": "You enter a room, there are some weird markings on the wall, you take a closer look and it looks like a riddle\nIt says 'The more you take the more you leave behind'",
    # Hint (doesnt always apply) (String)
    "hint_prompt": "This riddle is all about your journey, and what you do as you move forward.",
    # prompt for when the player completes the room (String)
    "complete_prompt": "You completed the riddle, Great Job"
}

riddle2 = {
    # Name of room (String)
    "id": "Riddle room 2",
    # Shortened name for displaying map, might add a map legend to the display map function later (String) (2 letters
    # or digits long)
    "map_id": "R2",
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
    "clear_condition": "river",
    # If the room is locked or not to the player, None if not locked, if locked put the id of the item to unlock it
    "locked" : None,
    # item given to you if you complete the puzzle, None if there isnt one
    "complete_item": None,
    # The first prompt that appears when the player enters the room for the first time, things like what the room is
    # and what it looks like (String)
    "first_prompt": "You enter a room, there are some weird markings on the wall, you take a closer look and it looks like a riddle\nIt says 'I'm often running, but I don't have legs.\nI have a bed, but never sleep.\nI can have banks, but no money.\nWhat am I?'",
    # The prompt that appears when the player enters the room for all times after the first time (String)
    "enter_prompt": "You enter a room, there are some weird markings on the wall, you take a closer look and it looks like a riddle\nIt says 'I'm often running, but I don't have legs.\nI have a bed, but never sleep.\nI can have banks, but no money.\nWhat am I?'",
    # Hint (doesnt always apply) (String)
    "hint_prompt": "This bed doesn't need sheets or pillows, but can be deep or shallow.",
    # prompt for when the player completes the room (String)
    "complete_prompt": "You completed the riddle, Great Job"
}

riddle3 = {
    # Name of room (String)
    "id": "Riddle room 3",
    # Shortened name for displaying map, might add a map legend to the display map function later (String) (2 letters
    # or digits long)
    "map_id": "R3",
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
    "clear_condition": "penny",
    # If the room is locked or not to the player, None if not locked, if locked put the id of the item to unlock it
    "locked" : None,
    # item given to you if you complete the puzzle, None if there isnt one
    "complete_item": None,
    # The first prompt that appears when the player enters the room for the first time, things like what the room is
    # and what it looks like (String)
    "first_prompt": "You enter a room, there are some weird markings on the wall, you take a closer look and it looks like a riddle\nIt says 'What has a head and a tail but has no legs?'",
    # The prompt that appears when the player enters the room for all times after the first time (String)
    "enter_prompt": "You enter a room, there are some weird markings on the wall, you take a closer look and it looks like a riddle\nIt says 'What has a head and a tail but has no legs?'",
    # Hint (doesnt always apply) (String)
    "hint_prompt": "Whatever this is, it is often associated with good luck.",
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
    "cutscenes": [chess_1_p0_cutscene, chess_1_p1_cutscene, chess_1_p2_cutscene]
}

bad_room = {
    # Name of room (String)
    "id": "Bad room",
    # Shortened name for displaying map, might add a map legend to the display map function later (String) (2 letters
    # or digits long)
    "map_id": "BR",
    # Type of room (eg "basic", "riddle", "puzzle", "event") (String)
    "type": "event",
    # visited (Only the rooms you want to appear immediately should this be set to True) (Boolean)
    "visited": False,
    # required room. 0 if optional room. 1-2-3-4.. for the order after that for required rooms (entrance begins as
    # 1), necessary for map creation (Int)
    "required": 8,
    # score given to player upon completion of room (Int)
    "complete_room_score": 0,
    # List of items in room as "id" of the item (List[item_id])
    "item_list": [],
    # Clear condition that is checked with the user input to see if rooms task is complete, set to True if checking completion in own function
    "clear_condition": None,
    # If the room is locked or not to the player, None if not locked, if locked put the id of the item to unlock it
    "locked" : None,
    # item given to you if you complete the puzzle, None if there isnt one
    "complete_item": None,
    # The first prompt that appears when the player enters the room for the first time, things like what the room is
    # and what it looks like (String)
    "first_prompt": None,
    # The prompt that appears when the player enters the room for all times after the first time (String)
    "enter_prompt": None,
    # Hint (doesnt always apply) (String)
    "hint_prompt": None,
    # prompt for when the player completes the room (String)
    "complete_prompt": None,
    #luck for if the room is a bad room
    "luck": False
}

# A list used for holding all the room dictionaries in this file to be iterated through in the room_initialisation file
room_dict_list = [entrance, riddle1, riddle2, riddle3, event1, event2, sudoku, chess1]
#   !!!PLEASE MAKE SURE THE REQUIRED ROOMS IN THIS LIST ARE SORTED IN ORDER FROM SMALLEST TO LARGEST!!!

bad_room_chance = random.random()
if bad_room_chance < 0.001:
    room_dict_list.append(bad_room)
