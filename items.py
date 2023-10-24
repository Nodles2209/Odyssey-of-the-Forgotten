class Item:
	"""
	This class is used to make items in the game

	"""

	def __init__(self, item_id):
		self.id = item_id
		self.description = None  # type str = holds item text that can be displayed when the item is inspected
		self.score = 0  # type int = some items may directly boost/decrease your score
		self.title = None  # type str, some items may grant a descriptor to the player to be displayed at the final room
