"""

This file is used to create and store all the room data in the following steps -
1. Import a list of the rooms stored as dictionaries of all the values from room_dicts
2. Iterate through the room dictionaries
3. Initialise an empty room
4. Set all the values from the dictionary to the empty room
5. Add the room to the required or optional room lists 
6. After iterated through all the dicitonaries, return the required and optional lists

To use this file:
1. First import it
2. call the create_rooms() function
3. set the function to return to three variables (required/optional lists and items_diction)

"""

from rooms import *
from room_dicts import *
from items_initialisation import *


def create_rooms():
    """
    This function is used to create all the rooms that are stated in the room_dicts.py file, set all the values within the room objects and return
    the required and the optional room list used for the map creation in map.py and the dictionary filled with the id and object of all the items {"id" : item_object}
    """
    # sets empty lists to append to later
    required_room_list = []
    optional_room_list = []

    items_dictionary = create_items() # initialises and returns a dictionary of all the items {"id" : item_object}, imported from items_initialisation

    for room_dict in room_dict_list:  # iterates over all the room dictionaries in the imported room_dict_list from the room_initialisation.py file

        #creates an event room if the type of the room is event, (Event room is a child class to the Room class)
        if room_dict["type"] == "event":
            room_object = Event()   #creates a blank event room template
        else:
            room_object = Room()  # creates a blank room template

        # Sets all the variables from the dictionary to the created blank room
        room_object.set_id(room_dict["id"])
        room_object.set_map_id(room_dict["map_id"])
        room_object.set_type(room_dict["type"])
        room_object.set_visited(room_dict["visited"])
        room_object.set_required(room_dict["required"])
        room_object.set_complete_score(room_dict["complete_room_score"])
        # Adds all the items needed to the room, using the "id" to find them
        for item in room_dict["item_list"]:
            room_object.add_item(items_dictionary[item])
        room_object.set_clear_condition(room_dict["clear_condition"])
        room_object.set_locked(room_dict["locked"])
        room_object.set_first_prompt(room_dict["first_prompt"])
        room_object.set_enter_prompt(room_dict["enter_prompt"])
        room_object.set_hint_prompt(room_dict["hint_prompt"])
        room_object.set_complete_prompt(room_dict["complete_prompt"])

        # here it splits the rooms into the two required and optional lists created at the start of the function
        if room_object.get_required() == 0:
            optional_room_list.append(room_object)
        else:
            required_room_list.append(room_object)

    return required_room_list, optional_room_list, items_dictionary  # returns the two lists optional/ required rooms and a dictionary of all the items {"id" : item_object}
