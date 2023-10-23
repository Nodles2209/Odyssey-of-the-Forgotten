import random  # This module is needed for creating pseudo randomness in the game/map
from rooms import Room
from player import Player

def init_choose_room(required_room_list, optional_room_list):
    """
    This function is used to return a room to next be placed in the map from the two lists: required_room_list and optional_room_list

    """
    room_type_choice = random.random()  # This uses the random module to create a random float between 0-1
    if (
            room_type_choice <= 0.4 and required_room_list) or not optional_room_list:  # Here the float is used as a percentage change of picking a required room (40% chance of picking) or the if runs if the optional_room_list is empty
        chosen_room = required_room_list.pop(
            0)  # this removes the room from the required_room_list and selects it to be returned at the end of the funtion, Rooms are picked in order to avoid the player being trapped
    elif optional_room_list:  # Here is the other 60% chance that is run if a required room wasn't picked
        chosen_room = optional_room_list.pop(random.randint(0,
                                                            len(optional_room_list) - 1))  # Here the rooms are picked in a random order as the order is not important, and is selected to be returned

    return chosen_room  # chosen room is returned


def init_find_exit(branch_from_room, possible_exits):
    """
    This function takes the branch room and the list of possible __exits as arguments and returns a string of the direction of the exit

    """

    exit_chosen = False
    while not exit_chosen:
        exit_index = random.randint(0, 3)  # selects the exit at random
        if possible_exits[exit_index]:
            if exit_index == 0:
                return "north"
            elif exit_index == 1:
                return "east"
            elif exit_index == 2:
                return "south"
            elif exit_index == 3:
                return "west"
            else:
                print("Something went wrong at the init_find_exit function")


def init_gen_empty_map_matrix(map_size=[5, 5]):
    """
    This function takes a list of 2 integers as an arguments (size of the matrix wanted) and generates a matrix of the size specified in the argument (or the base case [5, 5]),
    The matrix is initialised with only None values, and It returns the matrix at the end of the funtion

    """
    map_matrix = []
    for y in range(map_size[1]):
        row_list = []
        for x in range(map_size[0]):
            row_list.append(None)
        map_matrix.append(row_list)

    return map_matrix


class Map:
    """
    This class holds values for the map and creates the map on creation, useful values in this class are:

    - self.matrix_size this holds the size of the matrix [x, y]
    - self.map_matrix  this returns a 5x5 matrix which holds the room locations as objects in the matrix and empty
      spaces are set as None
    - self.rooms_objects has all the room objects in the map in a list
    - self.rooms is a dictionary used to access rooms by their str id

    Any functions built into this class that begin with 'init' are labeled because they are used for the initialisation of the map

    The map is generated randomly by having a starting point (entrance at the center of the matrix),
    Then the next room to be added is picked at random from the 2 room lists,
    The rooms in the optional_room_list are picked in a random order as it is not import where they are accessed,
    The rooms in the required_room_list are picked in the order of the list, this is to prevent situations where the player could get stuck behind a locked door with the key inaccessible behind the door,
    Next a random room is picked from the rooms already placed in the map (repeated until a room is found with an exit not already taken and not out of bounds)-This room is often called the branch_from_room in the code,
    Next an exit is picked from the possible __exits,
    After this the new room is added to the map and the correct __exits and lists are updated,
    This is repeated until both the room lists are empty
    """

    def __init__(self):
        """
        This function is automatically called when a map object is created

        """
        self.matrix_size = [5,5]  # sets the size of the map matrix, the integers in the list need to be odd to have a center for the entrance room
        self.rooms_objects = []  # has all the room objects in the map in a list
        self.map_matrix = init_gen_empty_map_matrix(self.matrix_size)  # this uses a function built into the Map class to create and set an empty matrix
        self.rooms = {} # used to access the rooms in the map by their str id

    def init_gen_map(self, required_room_list, optional_room_list):
        """
        This function is called in the __init__ function of the class and holds the main system for adding the rooms to
        the map

        """
        #Here it initliases the enterance (first room), so the map creation can work
        entrance = required_room_list.pop(0)
        entrance.set_x(2)
        entrance.set_y(2)
        self.map_matrix[entrance.get_y()][entrance.get_x()] = entrance  # places entrance in map matrix
        self.rooms_objects.append(entrance)  # places entrance in rooms list
        self.rooms[entrance.get_id()] = entrance # adds the entrance room to self.rooms dictionary


        while required_room_list or optional_room_list:  # runs a while loop until both lists are empty
            chosen_room = init_choose_room(required_room_list, optional_room_list)  # This function picks the next room (mostly) randomly to be next placed in the map
            branch_from_room, exits = self.init_find_branch_room()  # This function finds a random place for placing the room and finds a direction it can be placed from the room
            self.place_room(chosen_room, branch_from_room,
                            exits)  # This function handles the system for adding the room to the game matrix and setting the correct __exits in the __exits dictionary of the room

    def init_check_exits_possible(self, branch_from_room):
        """
        This function takes the room that the new room is being branched from as an argument, and returns a list of
        booleans of which __exits are possible, in the order: North, East, South, West

        """

        # These are temporary values which are used for returning at the end of the function
        north_possible = False
        east_possible = False
        south_possible = False
        west_possible = False

        # checks north exit is possible in the map matrix, and that a room is not already placed there
        if branch_from_room.get_y() != 0 and self.map_matrix[branch_from_room.get_y() - 1][branch_from_room.get_x()] is None:
            north_possible = True
        # check east
        if branch_from_room.get_x() != self.matrix_size[0] - 1 and self.map_matrix[branch_from_room.get_y()][branch_from_room.get_x() + 1] is None:
            east_possible = True
        # check south
        if branch_from_room.get_y() != self.matrix_size[1] - 1 and self.map_matrix[branch_from_room.get_y() + 1][branch_from_room.get_x()] is None:
            south_possible = True
        # check west
        if branch_from_room.get_x() != 0 and self.map_matrix[branch_from_room.get_y()][branch_from_room.get_x() - 1] is None:
            west_possible = True

        return [north_possible, east_possible, south_possible, west_possible]

    def init_find_branch_room(self):
        """
        This function returns the branch_from_room (room which new room is branched from) and the possible exit chosen

        """

        found_branch_room = False  # temporary variable

        while not found_branch_room:
            temp_index = random.randint(0,
                                        len(self.rooms_objects) - 1)  # here it selects a random integer for selecting a random room to branch from
            branch_from_room = self.rooms_objects[temp_index]

            possible_exits = self.init_check_exits_possible(
                branch_from_room)  # uses function that returns a list of booleans of possible directions the room can be placed in
            if True in possible_exits:
                return branch_from_room, init_find_exit(branch_from_room, possible_exits)  # returns only if a room with a free exit has been found

    def place_room(self, chosen_room, branch_from_room, current_exit):
        """
        This function takes the room being added to the map, the room it is being branched from, and the exit from the branched room that will lead to the new room as arguments,
        The function sets the room within the matrix and sets the __exits for both the rooms

        """

        branch_from_room.set_exit(current_exit, chosen_room)  # sets the exit for the branch room
        self.rooms_objects.append(chosen_room)  # adds new room to the rooms_objects list

        if current_exit == "north":  # This sets the exit for the chosen_room and sets the x,y and places the room within the map matrix
            chosen_room.set_exit("south", branch_from_room)
            chosen_room.set_x(branch_from_room.get_x())
            chosen_room.set_y(branch_from_room.get_y() - 1)
        elif current_exit == "east":
            chosen_room.set_exit("west", branch_from_room)
            chosen_room.set_x(branch_from_room.get_x() + 1)
            chosen_room.set_y(branch_from_room.get_y())
        elif current_exit == "south":
            chosen_room.set_exit("north", branch_from_room)
            chosen_room.set_x(branch_from_room.get_x())
            chosen_room.set_y(branch_from_room.get_y() + 1)
        elif current_exit == "west":
            chosen_room.set_exit("east", branch_from_room)
            chosen_room.set_x(branch_from_room.get_x() - 1)
            chosen_room.set_y(branch_from_room.get_y())

        self.map_matrix[chosen_room.get_y()][chosen_room.get_x()] = chosen_room #places room in the map matrix

        self.rooms[chosen_room.get_id()] = chosen_room  #adds room to the self.rooms dictionary

    def display_map(self, player):
        """
        This function is used for displaying the map on a grid, it takes in the player object.
        it uses a for loop that creates 5 lines to be printed, once the first for loop has completed, the whole map should be printed
        This may later be changed slightly to incorporate where the player is, and only display rooms that have been visited

        It prints rooms in the format, in a grid layout:

        *This shows room with all __exits
          __||__
         |      |
        =|      |=
         |______|
            ||

        *This shows room with no __exits
          ______
         |      |
         |      |
         |______|

        """

        print("-" * 100)  # print a line to make it easier to read

        for i in range(len(self.map_matrix)):
            line_1 = ""
            line_2 = ""
            line_3 = ""
            line_4 = ""
            line_5 = ""

            for a in range(len(self.map_matrix[i])):
                room = self.map_matrix[i][a]
                if not room or room.get_visited() == False:  # Here it prints empty space if no rooms are found in that position of the matrix
                    line_1 += " " * 10
                    line_2 += " " * 10
                    line_3 += " " * 10
                    line_4 += " " * 10
                    line_5 += " " * 10
                else:
                    if room.get_exit("north"):  #prints the north exit
                        line_1 += "  __||__  "
                    else:
                        line_1 += "  ______  "

                    if player.current_room == room: #prints the players location
                        line_2 += " |Player| "
                    else:
                        line_2 += " |      | "

                    if room.get_exit("west"):   #prints the west exit
                        line_3 += "=|  "
                    else:
                        line_3 += " |  "

                    line_3 += str(room.get_map_id())    #prints the name in the room

                    if room.get_exit("east"):   #prints the east exit
                        line_3 += "  |="
                    else:
                        line_3 += "  | "

                    line_4 += " |______| "

                    if room.get_exit("south"):  #prints the south exit
                        line_5 += "    ||    "
                    else:
                        line_5 += " " * 10

            combined_lines = f"{line_1}\n{line_2}\n{line_3}\n{line_4}\n{line_5}"  # This combines the lines to make it easier to print
            print(combined_lines)

        print("-" * 100)  # print a line to make it easier to read
