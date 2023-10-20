class Player:
    """
    This class holds values for the player such as the players name, inventory and current room
    """

    def __init__(self, name, entrance):  # run when a player object is created
        self.name = name  # string
        self.current_room = entrance  # room object
        self.inventory = []  # list of item objects
        self.score = None  # int
