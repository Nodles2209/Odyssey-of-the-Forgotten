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
2. Call the initialise_rooms function

This will set up the all_rooms, required_room_list and optional_room_list variables required for map generation

IF THE INITIALISE_ROOMS FUNCTION IS NOT CALLED, IT WILL RESULT IN AN ERROR BECAUSE EACH VARIABLE WILL NOT BE UPDATED
PROPERLY

"""

from rooms import *

all_rooms = {}

required_room_list = []
optional_room_list = []


def create_rooms(room_dict, all_rooms_dict):
    """
    This function takes room_dict and all_room_dict as parameters where
        - room_dict is the dictionary that stores the values of the room to be created
        - all_rooms_dict is the dictionary that stores all the room objects created by the room's IDs,

    The purpose of this function is to create room objects from the values given in the room_dict dictionary, and add
    these newly created rooms to the all_rooms_dict

    Each room will be added to the all_rooms_dict according to their room_id, which should look like-
        {<room_id>: <room object>}

    """

    pass


def initialise_rooms():
    """
    This function is used to initialise the required variables used in map generation

    Basic logic:
        - The function first iterates through all the dictionaries that store the initial values
        - Call the create_rooms function and parse each dictionary and all_rooms through it to create a room for each
        dictionary and storing that room in all_rooms
        - Getting the value stored in each room's necessary attribute and storing each room in the required_room_list
        or optional_room_list depending on that value

    """

    global required_room_list
    global optional_room_list

    pass
