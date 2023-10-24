
"""
This file creates all the Item() objects using the item_dicts.py file,
it uses the same system found in the room_initialisation.py file
however here it returns a dictionary with the {"id" : item_object} which the room_initialisation uses to place the 
right objects in the right rooms

To use this class:
1. First import it
2. call the create_items() function in the room_initialisation file
3. set the function to return a dictionary with the {"id" : item_object}
"""

from items import *
from item_dicts import *

def create_items():
	"""
	This fucntion handles all the initalisation with taking the item dictionaries and transfering the data into empty
	item objects

	it returns a dicitonary of all the items, {"id" : item_object}
	"""
	items_dictionary = {}  #creates an empty dictionary to append the items {"id" : item_object} after creation

	for item_dict in item_dict_list:
		item_object = Item()

		item_object.set_id(item_dict["id"])
		item_object.set_description(item_dict["description"])
		item_object.set_score(item_dict["score"])
		item_object.set_title(item_dict["title"])

		items_dictionary[item_object.get_id()] = item_object

	return items_dictionary