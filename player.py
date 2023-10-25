class Player:
    """
    This class holds values for the player such as the players name, inventory and current room
    """

    def __init__(self, name, entrance):  # run when a player object is created
        self.name = name  # string
        self.current_room = entrance  # room object
        self.inventory = []  # list of item objects
        self.score = 0  # int
        self.title = []  # array of str, where titles are only to be used in the final room
        self.won_game = False

    def print_inventory(self):
        # this function is used for printing the items in the players inventory
        if self.inventory == []:
            print("You have nothing in your inventory")
        else:
            print("You inventory contains:")
            for item in self.inventory:
                print(" >", item.get_id())
