class Item:
	"""
	This class is used to make items in the game

	"""

	def __init__(self):
		self.__id = None	#type str - name of the item
		self.__description = None  # type str - holds item text that can be displayed when the item is inspected
		self.__score = 0  # type int - some items may directly boost/decrease your score
		self.__title = None  # type str - some items may grant a descriptor to the player to be displayed at the final room

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
		   and prints the description of the item to the player'''

		key_used = False

		if player.current_room.get_exit("north"):
			if self.get_id() == player.current_room.get_exit("north").get_locked():
				print("You have unlocked the north exit")
				player.current_room.get_exit("north").set_locked(None)
				player.inventory.remove(self)
				key_used = True
		if player.current_room.get_exit("east"):
			if self.get_id() == player.current_room.get_exit("east").get_locked():
				print("You have unlocked the east exit")
				player.current_room.get_exit("east").set_locked(None)
				player.inventory.remove(self)
				key_used = True
		if player.current_room.get_exit("south"):
			if self.get_id() == player.current_room.get_exit("south").get_locked():
				print("You have unlocked the south exit")
				player.current_room.get_exit("south").set_locked(None)
				player.inventory.remove(self)
				key_used = True
		if player.current_room.get_exit("west"):
			if self.get_id() == player.current_room.get_exit("west").get_locked():
				print("You have unlocked the west exit")
				player.current_room.get_exit("west").set_locked(None)
				player.inventory.remove(self)
				key_used = True

		if not key_used:
			print(self.__description)	#prints the description of the item