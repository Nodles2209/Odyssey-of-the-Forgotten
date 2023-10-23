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
        self.__x = None  # type int
        self.__y = None  # type int
        self.__exits = {'north': None,
                        'east': None,
                        'south': None,
                        'west': None
                        }
        self.__type = None  # type str - used to store type of room
        self.__description = None  # stores str but type undetermined; can be arr, dict or its own object -
        # used to store room text
        self.__clear_condition = None  # type stored in this attribute depends on room type
        self.__isClear = False  # type bool - checks if the room is cleared or not; False until True
        self.__visited = False  # type bool - checks if player has already visited the room; False until True
        self.__necessary = None  # type int -
        # 0 : not necessary,
        # 1+ : order of importance

        self.__items = []  # array of type item - stores all the items currently in the room

    def get_id(self):  # gets id of room
        return self.__id

    def set_id(self, new_id):  # sets id of the room (string)
        self.__id = new_id

    def get_x(self):  # gets x of room
        return self.__x

    def set_x(self, x):  # sets x coordinate of the room (int)
        self.__x = x

    def get_y(self):  # gets id of room
        return self.__y

    def set_y(self, y):  # sets id y coordinate the room (int)
        self.__y = y

    def get_exit(self, current_exit):  # gets an exit of the room taking in a direction as a string
        return self.__exits[current_exit]

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

    def get_desc(self):  # returns the string containing the room's text
        return self.__description

    def set_desc(self, desc):  # sets the room's text based on a single, fully formatted string
        self.__description = desc

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

    def get_necessary(self):  # returns the integer determining how necessary a room is (for the room lists)
        return self.__necessary

    def set_necessary(self, necessary_int):  # sets the necessary attr based on the int parsed through
        self.__necessary = necessary_int

    def get_inventory(self):  # returns an array that contains the items the user currently has
        return self.__items

    def add_to_inventory(self, item):  # adds the item parsed through to the inventory
        self.__items.append(item)

    def remove_from_inventory(self, item):  # removes the item parsed if it exists in inventory
        if item in self.__items:
            self.__items.remove(item)
            return True  # returns True if operation is completed as expected
        return False  # returns False if item is not in the inventory


class Riddle(Room):
    """
    Since Riddle is inheriting from parent class - Room, it will use the same attributes as Room;
    if you want to add more attributes that are specific to the Riddle class, add the attributes (set them to private
    using the __ prefix) after the super() call in the __init__ function
    The get and set methods will be the same as its parent class, however if extra attributes are added, new get and set
    methods will need to be created for these added attributes

    Additionally, the Riddle class will have its own unique methods to determine whether it's cleared or not using the
    stored value in self.__clear_condition

    """

    def __init__(self):
        super().__init__()


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


class Puzzle(Room):
    """
    Since Puzzle is inheriting from parent class - Room, it will use the same attributes as Room;
    if you want to add more attributes that are specific to the Puzzle class, add the attributes (set them to private
    using the __ prefix) after the super() call in the __init__ function
    The get and set methods will be the same as its parent class, however if extra attributes are added, new get and set
    methods will need to be created for these added attributes

    Additionally, the Puzzle class will have its own unique methods to determine whether it's cleared or not using the
    stored value in self.__clear_condition

    """

    def __init__(self):
        super().__init__()
