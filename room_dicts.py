# from items import Item

entrance = {
    # Name of room (String)
    "id": "Entrance",
    # Shortened name for displaying map, might add a map legend to the display map function later (String) (2 letters
    # or digits long)
    "map_id": "En",
    # Type of room (eg "riddle", "puzzle", "event") (String)
    "type": "event",
    # visited (Only the rooms you want to appear immediately should this be set to True) (Boolean)
    "visited": True,
    # required room. 0 if optional room. 1-2-3-4.. for the order after that for required rooms (entrance begins as
    # 1), necessary for map creation (Int)
    "required": 1,
    # score given to player upon completion of room (Int)
    "complete_room_score": 1000,
    # List of items in room as "id" of the item (List[item_id])
    "item_list": ["map"],
    # The first prompt that appears when the player enters the room for the first time, things like what the room is
    # and what it looks like (String)
    "first_prompt": "You wake up and you are in an unfamiliar place....",
    # The prompt that appears when the player enters the room for all times after the first time (String)
    "enter_prompt": "You are back in the first room....",
    # Hint (doesnt always apply) (String)
    "hint_prompt": "Find all the parts for the plane in other places around the map",
    # prompt for when the player completes the room (String)
    "complete_prompt": "You completed this room...."
}

room1 = {
    # Name of room (String)
    "id": "Room 1",
    # Shortened name for displaying map, might add a map legend to the display map function later (String) (2 letters
    # or digits long)
    "map_id": "R1",
    # Type of room (eg "riddle", "puzzle", "event") (String)
    "type": "event",
    # visited (Only the rooms you want to appear immediately should this be set to True) (Boolean)
    "visited": False,
    # required room. 0 if optional room. 1-2-3-4.. for the order after that for required rooms (entrance begins as
    # 1), necessary for map creation (Int)
    "required": 0,
    # score given to player upon completion of room (Int)
    "complete_room_score": 1000,
    # List of items in room as "id" of the item (List[item_id])
    "item_list": ["key"],
    # The first prompt that appears when the player enters the room for the first time, things like what the room is
    # and what it looks like (String)
    "first_prompt": "You wake up and you are in an unfamiliar place....",
    # The prompt that appears when the player enters the room for all times after the first time (String)
    "enter_prompt": "You are back in the first room....",
    # Hint (doesnt always apply) (String)
    "hint_prompt": "Find all the parts for the plane in other places around the map",
    # prompt for when the player completes the room (String)
    "complete_prompt": "You completed this room...."
}

# A list used for holding all the room dictionaries in this file to be iterated through in the room_initialisation file
room_dict_list = [entrance, room1]  
#   !!!PLEASE MAKE SURE THE REQUIRED ROOMS IN THIS LIST ARE SORTED IN ORDER FROM SMALLEST TO LARGEST!!!
