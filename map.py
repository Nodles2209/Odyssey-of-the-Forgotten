import random #This module is needed for creating psuedo randomness in the game/map

class Map:
    '''
        This class holds values for the map and creates the map on creation, useful values in this class are:

        - self.map_matrix  this returns a 5x5 matrix which holds the room locations as objects in the matrix and empty
          spaces are set as None
        - self.entrance has easy access for getting the room object for the entrance
        - self.rooms_in_map has all the room objects in the map in a list

        Any functions built into this class that begin with 'init' are labbled because they are used for the initialisation of the map

        The map is generated randomly by having a starting point (entrance at the center of the martix),
        Then the next room to be added is picked at random from the 2 room lists, 
        The rooms in the optional_room_list are picked in a random order as it is not import where they are accessed,
        The rooms in the required_room_list are picked in the order of the list, this is to prevent situations where the player could get stuck behind a locked door with the key unaccesable behind the door,
        Next a random room is picked from the rooms already placed in the map (repeated until a room is found with an exit not already taken and not out of bounds)-This room is often called the branch_from_room in the code,
        Next an exit is picked from the possible exits,
        After this the new room is added to the map and the correct exits and lists are updated,
        This is repeated until both the room lists are empty
    '''

    def __init__(self):
        '''This function is automatically called when a map object is created'''
        self.matrix_size = [5, 5]   # sets the size of the map matrix, the integers in the list need to be odd to have a center for the entrance room
        self.entrance = Room("ent0", 2, 2)    # sets the entrance room object into the map class
        self.rooms_in_map = [self.entrance]     #adds the entrance room to the rooms_in_map list
        self.map_matrix = self.init_gen_empty_map_matrix(self.matrix_size)  # this uses a function built into the Map class to create and set an empty matrix
        self.map_matrix[(self.matrix_size[0] - 1) // 2][(self.matrix_size[1] - 1) // 2] = self.entrance    # this puts the entrance object within the matrix at the center
        self.init_gen_map()   #This generates the map placing all the rooms within

    def init_gen_map(self):
        '''This function is called in the __init__ function of the class and holds the main system for adding the rooms to the map'''
        while required_room_list or optional_room_list:     #runs a while loop until both lists are empty
            chosen_room = self.init_choose_room()       #This function picks the next room (mostly) randomly to be next placed in the map
            branch_from_room, exit = self.init_find_branch_room()   #This function finds a random place for placing the room and finds a direction it can be placed from the room
            self.place_room(chosen_room, branch_from_room, exit)    #This function handles the system for adding the room to the game matrix and setting the correct exits in the exits dictionary of the room

    def init_choose_room(self):
        '''This function is used to return a room to next be placed in the map from the two lists: required_room_list and optional_room_list'''
        room_type_choice = random.random()      #This uses the random module to create a random float between 0-1
        if (room_type_choice <= 0.4 and required_room_list) or not optional_room_list:  #Here the float is used as a percentage change of picking a required room (40% chance of picking) or the if runs if the optional_room_list is empty
            chosen_room = required_room_list.pop(0) #this removes the room from the required_room_list and selects it to be returned at the end of the funtion, Rooms are picked in order to avoid the player being trapped
        elif optional_room_list:    #Here is the other 60% chance that is run if a required room wasnt picked
            chosen_room = optional_room_list.pop(random.randint(0, len(optional_room_list) - 1))    #Here the rooms are picked in a random order as the order is not important, and is selected to be returned

        return chosen_room  #chosen room is returned

    def init_check_exits_possible(self, branch_from_room):
        '''This function takes the room that the new room is being branched from as an argument, and returns a list of booleans of which exits are possible, in the order: North,East,South,West'''

        #These are temporary values which are used for returning at the end of the function
        north_possible = False
        east_possible = False
        south_possible = False
        west_possible = False

        #checks north exit is possible in the map matrix, and that a room is not already placed there
        if branch_from_room.y != 0 and self.map_matrix[branch_from_room.y - 1][branch_from_room.x] == None:
            north_possible = True
        #check east
        if branch_from_room.x != self.matrix_size[0] - 1 and self.map_matrix[branch_from_room.y][branch_from_room.x + 1] == None:
            east_possible = True
        #check south
        if branch_from_room.y != self.matrix_size[1] - 1 and self.map_matrix[branch_from_room.y + 1][branch_from_room.x] == None:
            south_possible = True
        #check west
        if branch_from_room.x != 0 and self.map_matrix[branch_from_room.y][branch_from_room.x - 1] == None:
            west_possible = True

        return [north_possible, east_possible, south_possible, west_possible]

    def init_find_branch_room(self):
        '''This function returns the branch_from_room (room which new room is branched from) and the possible exit chosen'''

        found_branch_room = False   #temporary variable

        while not found_branch_room:
            temp_index = random.randint(0, len(self.rooms_in_map) - 1)      #here it selects a random integer for selecting a random room to branch from
            branch_from_room = self.rooms_in_map[temp_index]

            possible_exits = self.init_check_exits_possible(branch_from_room)   #uses function that returns a list of booleans of possible directions the room can be placed in
            if True in possible_exits: 
                return branch_from_room, self.init_find_exit(branch_from_room, possible_exits)  #returns only if a room with a free exit has been found


    def place_room(self, chosen_room, branch_from_room, exit):
        '''This function takes the room being added to the map, the room it is being branched from, and the exit from the branched room that will lead to the new room as arguments,
           The function sets the room within the matrix and sets the exits for both the rooms'''

        branch_from_room.exits[exit] = chosen_room  #sets the exit for the branch room
        self.rooms_in_map.append(chosen_room)   #adds new room to the rooms_in_map list

        if exit == "North":                                 #This sets the exit for the chosen_room and sets the x,y and places the room within the map matrix
            chosen_room.exits["South"] = branch_from_room
            chosen_room.x = branch_from_room.x
            chosen_room.y = branch_from_room.y - 1
            self.map_matrix[chosen_room.y][chosen_room.x] = chosen_room 
        elif exit == "East":
            chosen_room.exits["West"] = branch_from_room
            chosen_room.x = branch_from_room.x + 1
            chosen_room.y = branch_from_room.y
            self.map_matrix[chosen_room.y][chosen_room.x] = chosen_room 
        elif exit == "South":
            chosen_room.exits["North"] = branch_from_room
            chosen_room.x = branch_from_room.x
            chosen_room.y = branch_from_room.y + 1
            self.map_matrix[chosen_room.y][chosen_room.x] = chosen_room 
        elif exit == "West":
            chosen_room.exits["East"] = branch_from_room
            chosen_room.x = branch_from_room.x - 1
            chosen_room.y = branch_from_room.y
            self.map_matrix[chosen_room.y][chosen_room.x] = chosen_room 
        
        


    def init_find_exit(self, branch_from_room, possible_exits):
        '''This function takes the branch room and the list of possible exits as arguments and returns a string of the direction of the exit'''
        exit_chosen = False
        while not exit_chosen:
            exit_index = random.randint(0, 3)       #selects the exit at random
            if possible_exits[exit_index] == True:
                if exit_index == 0:
                    return "North"
                elif exit_index == 1:
                    return "East"
                elif exit_index == 2:
                    return "South"
                elif exit_index == 3:
                    return "West"
                else:
                    print("Something went wrong at the init_find_exit function")


    def init_gen_empty_map_matrix(self, map_size = [5, 5]):
        '''This function takes a list of 2 integers as an arguments (size of the matrix wanted) and generates a matrix of the size specified in the argument (or the base case [5, 5]),
           The matrix is initialised with only None values and It returns the matrix at the end of the funtion'''
        map_matrix = []
        for y in range(map_size[1]):
            row_list = []
            for x in range(map_size[0]):
                row_list.append(None)
            map_matrix.append(row_list)

        return map_matrix

    def display_map(self):
        '''This function is used for displaying the map on a grid'''
        print("-" * 100)
        for i in range(len(self.map_matrix)):
            temp = ""
            for a in range(len(self.map_matrix[i])):
                if not self.map_matrix[i][a]:
                    temp += (" None")
                else:
                    temp += (" "+ self.map_matrix[i][a].name)

            print(temp)

        print("-" * 100)

        '''
        #This is for printing the exits of each room for debugging purposes
        for room in self.rooms_in_map:
            temp = f""
            for direction, exit_room in room.exits.items():
                if exit_room:
                    temp += f" {direction}: {exit_room.name}"
            print(f"Room: {room.name}, Exits:", temp)
        '''



class Room:
    '''This class is used for creating room objects, it takes in a string 'name' , and and x and y (starting index at 0) used for setting the place of the room in the matrix
       in the Map class, Although the x and y arguments have defualt values so they are not necessary when creating a room

       useful values in this class are:

       - self.name for a string of the rooms name
       - self.x for the x coordinate (starting at 0) for the rooms place in the map matrix
       - self.y for the y coordinate (starting at 0) for the rooms place in the map matrix (0 is the top row)
       - self.exits is a dictionary with the keys as the directions (eg "North") and either None or a room object for the value
       '''
    def __init__(self, name, x = None, y = None):
        '''This function is automatically called when a room object is created, it is used to set neccesary values in the room class'''
        self.name = name    #string name of room
        self.x = x     #sets x (indexing starts at 0)
        self.y = y     #sets y (indexing starts at 0)
        self.exits = {"North" : None,
                      "East" : None,
                      "South" : None,
                      "West" : None}   #This is setting a dictionary with each of the directions as keys, when rooms are added they are added to the values as room objects



#This is a list of Room objects used for creating the map, these rooms are the required ones for the game to function
required_room_list = [Room("Rom1"), Room("Rom2"), Room("Rom3"), Room("Rom4")]
#This is a list of Room objects used for creating the map, these rooms are optional rooms not neccesary for the core game
optional_room_list = [Room("opt1"), Room("opt2"), Room("opt3"), Room("opt4")]


game_map = Map()
game_map.display_map()
#entrance_room = Room("ent0", 2, 2)

