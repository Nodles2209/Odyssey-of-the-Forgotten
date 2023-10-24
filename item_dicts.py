
map_item = {
	# type str, id of the item
	"id" : "map",
	# type str, item description, run when the item is inspected (unless unqiue case like map where the map itself is displayed)
	"description" : None,
	# type int, score you gain or loose when picking this item up
	"score" : 20,
	# type str, some items may grant a descriptor to the player to be displayed at the final room
	"title" : None
	  }

key_item = {
	# type str, id of the item
	"id" : "key",
	# type str, item description, run when the item is inspected (unless unqiue case like map where the map itself is displayed)
	"description" : "A key, maybe i can use this to open something, better hang on to it",
	# type int, score you gain or loose when picking this item up
	"score" : 0,
	# type str, some items may grant a descriptor to the player to be displayed at the final room
	"title" : None
	  }


# A list of all the items in the map that is imported in item_initialisation.py to create the item objects
# please add any items you make here so this works
item_dict_list = [map_item, key_item]