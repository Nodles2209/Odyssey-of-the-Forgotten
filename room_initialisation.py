"""

This file is used to create and store all the room data in the following steps -
1. Import all relevant dicts
2. Process each dictionary and create room objects based on the attributes in each dictionary
3. Store each room in the dictionary all_rooms with the format:
        {<room_id>: room object}

**IMPORTANT**
The class definitions will be stored in a separate file dedicated to only the classes and the relevant class methods

**HELP ON HOW TO USE THIS FILE FOR MAP GENERATION**
1. Import the module
2. Call the create_rooms function

This will set up the all_rooms, required_room_list and optional_room_list variables required for map generation

IF THE INITIALISE_ROOMS FUNCTION IS NOT CALLED, IT WILL RESULT IN AN ERROR BECAUSE EACH VARIABLE WILL NOT BE UPDATED
PROPERLY

"""

from rooms import *
from room_dicts import *


def create_rooms():
    """
    This function is used to create all the rooms that are stated in the room_dicts.py file, set all the values within the room objects and return
    the required and the optional room list used for the map creation in map.py
    """
    # sets empty lists to append to later
    required_room_list = []
    optional_room_list = []

    for room_dict in room_dict_list:  # iterates over all the room dictionaries in the imported room_dict_list from the room_initialisation.py file
        room_object = Room()  # creates a blank room template

        # Sets all the variables from the dictionary to the created blank room
        room_object.set_id(room_dict["id"])
        room_object.set_map_id(room_dict["map_id"])
        room_object.set_type(room_dict["type"])
        room_object.set_visited(room_dict["visited"])
        room_object.set_required(room_dict["required"])
        room_object.set_complete_score(room_dict["complete_room_score"])
        for item in room_dict["item_list"]:
            room_object.add_item(item)
        room_object.set_first_prompt(room_dict["first_prompt"])
        room_object.set_enter_prompt(room_dict["enter_prompt"])
        room_object.set_hint_prompt(room_dict["hint_prompt"])
        room_object.set_complete_prompt(room_dict["complete_prompt"])

        # here it splits the rooms into the two required and optional lists created at the start of the function
        if room_object.get_required() == 0:
            optional_room_list.append(room_object)
        else:
            required_room_list.append(room_object)

    return required_room_list, optional_room_list  # returns the two lists
