"""
This program will only store the various classes and their subsequent methods;
This program is to be imported into room_creation to help create each room object

"""


class Room:
    """
    Room's init function contains data for all the basic attributes present for each room;
    This class should also contain individual get and set methods for each attribute where;
        - The get methods should return the value stored in the relevant attribute
        - The set methods should take in the corresponding value to be set as a parameter and then change the value of
          the relevant attribute according to the value parsed through the parameter

    """

    def __init__(self):
        self.__id = None  # type str - used for easy reference to a room object
        self.__map_id = None  # type str - used for a shorted name for printing the map
        self.__x = None  # type int
        self.__y = None  # type int
        self.__exits = {'north': None,
                        'east': None,
                        'south': None,
                        'west': None
                        }
        self.__type = None  # type str - used to store type of room ('riddle', 'puzzle', 'event')
        self.__first_prompt = None  # type str - used to store the text for when the player first enters a room
        self.__enter_prompt = None  # type str - used to store the text for when a player enters a room that have visited previously
        self.__hint_prompt = None   # type str - used to store the text for when a player needs a hint
        self.__complete_prompt = None    # type str - used to store the text for when a player has completed the room
        self.__complete_score = None   # type int - used to hold the score the player gets when completing the room
        self.__clear_condition = None  # type stored in this attribute depends on room type
        self.__isClear = False  # type bool - checks if the room is cleared or not; False until True
        self.__visited = False  # type bool - checks if player has already visited the room; False until True
        self.__required = None  # type int -
        # 0 : not necessary,
        # 1+ : order of importance
        self.__items = []  # array of type item - stores all the items currently in the room

    def get_id(self):  # gets id of room
        return self.__id

    def set_id(self, new_id):  # sets id of the room (string)
        self.__id = new_id

    def get_map_id(self):  # gets id of room
        return self.__map_id

    def set_map_id(self, new_map_id):  # sets id of the room (string)
        self.__map_id = new_map_id

    def get_x(self):  # gets x of room
        return self.__x

    def set_x(self, x):  # sets x coordinate of the room (int)
        self.__x = x

    def get_y(self):  # gets id of room
        return self.__y

    def set_y(self, y):  # sets id y coordinate the room (int)
        self.__y = y

    def get_exit(self, direction):  # gets an exit of the room taking in a direction as a string
        return self.__exits[direction]

    def set_exit(self, current_exit, room):  # sets an exit for the room taking in an exit direction (string) and
        # room that it leads to (room object)
        self.__exits[current_exit] = room

    def get_visited(self):  # returns the boolean of whether the room has been visited
        return self.__visited

    def set_visited(self, visited):  # takes in a boolean to set if the room has been visited
        self.__visited = visited

    def get_type(self):  # returns a string containing the type of the room object
        return self.__type

    def set_type(self, room_type):  # takes in a string to set the room type
        self.__type = room_type

    def get_first_prompt(self):  # returns the string containing the room's first prompt
        return self.__first_prompt

    def set_first_prompt(self, prompt):  # sets the room's first prompt
        self.__first_prompt = prompt

    def get_enter_prompt(self):  # returns the string containing the room's enter prompt (described above)
        return self.__enter_prompt

    def set_enter_prompt(self, prompt):  # sets the room's hint prompt (described above)
        self.__enter_prompt = prompt

    def get_hint_prompt(self):  # returns the string containing the room's hint prompt
        return self.__hint_prompt

    def set_hint_prompt(self, prompt):  # sets the room's text based on a single, fully formatted string
        self.__hint_prompt = prompt

    def get_complete_prompt(self):  # returns the string containing the room's complete prompt
        return self.__complete_prompt

    def set_complete_prompt(self, prompt):  # sets the room's complete prompt
        self.__complete_prompt = prompt

    def get_complete_score(self):  # returns the int of the score the room gives to the player
        return self.__complete_score

    def set_complete_score(self, score):  # sets the room's complete score
        self.__complete_score = score

    def get_clear_condition(self):  # returns the clear condition of the room - type undetermined/any
        return self.__clear_condition

    def set_clear_condition(self, clear_condition):  # sets the clear condition based on the argument parsed
        self.__clear_condition = clear_condition

    def get_is_clear(self):  # returns a boolean that determines the clear state of the room
        return self.__isClear

    def set_is_clear(self, user_input):  # sets whether the room is cleared based on the user input by checking
        # whether the clear condition is the same as the user input
        clear_condition = self.get_clear_condition()

        if user_input == clear_condition:
            self.__isClear = True

    def get_required(self):  # returns the integer determining how required a room is (for the room lists)
        return self.__required

    def set_required(self, required_int):  # sets the required attr based on the int parsed through
        self.__required = required_int

    def get_items(self):  # returns an array that contains the items the room currently has
        return self.__items

    def add_item(self, item):  # adds the item parsed through to the rooms items list
        self.__items.append(item)

    def remove_item(self, item):  # removes the item parsed if it exists in inventory
        if item in self.__items:
            self.__items.remove(item)


    def inspect(self):
        """This function will handle when a player inspects a room, most of the time it will return the type of puzzle it needs to print"""
        if self.__id == "Entrance":
            print("This is the room where you woke up")
        else:
            print("This is where the game will print the puzzle when the player inspects it")


class Event(Room):
    """
    Since Event is inheriting from parent class - Room, it will use the same attributes as Room;
    if you want to add more attributes that are specific to the Event class, add the attributes (set them to private
    using the __ prefix) after the super() call in the __init__ function
    The get and set methods will be the same as its parent class, however if extra attributes are added, new get and set
    methods will need to be created for these added attributes

    Additionally, the Event class will have its own unique methods to determine whether it's cleared or not using the
    stored value in self.__clear_condition

    """

    def __init__(self):
        super().__init__()
        self.__luck = True  # type bool, if a room generated is ever set to False, immediately end the run and trigger
        # the bad/unlucky ending

    def get_luck(self):
        return self.__luck

    def set_luck(self, luck):  # only used if creating an "unlucky room", which will be a single room
        self.__luck = luck

