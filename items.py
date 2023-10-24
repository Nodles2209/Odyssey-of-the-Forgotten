class Item:
	"""
	This class is used to make items in the game

	"""

	def __init__(self):
		self.__id = None
		self.__description = None  # type str = holds item text that can be displayed when the item is inspected
		self.__score = 0  # type int = some items may directly boost/decrease your score
		self.__title = None  # type str, some items may grant a descriptor to the player to be displayed at the final room

	#Getters and Setters for all the objects values (because the objects values are private)
	def get_id(self):
		return self.__id

	def set_id(self, new_id):
		self.__id = new_id

	def get_description(self):
		return self.__description

	def set_description(self, description):
		self.__description = description

	def get_score(self):
		return self.__score

	def set_score(self, score):
		self.__score = score

	def get_title(self):
		return self.__title

	def set_title(self, title):
		self.__title = title



	def inspect(self, game_map, player):
		'''takes in the games map objects and player object
		   Inspect the item, this will print a description to the player most of the time, 
		   but may also do other things like print the map when neccesary'''
		if self.__id == "map":
			print(game_map.display_map(player))
		else:
			print(self.__description)