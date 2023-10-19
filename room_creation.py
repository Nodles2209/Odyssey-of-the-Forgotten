"""

This file is used to create and store all the room data in the following steps -
1. Import all relevant text files into separate variables depending on the room the text file contains data for
2. Put these variables into each corresponding array for easy classification
3. Using a method, create objects using the data in the text files and replace each variable with this newly created
   object's ID (for easy reference)

**NOTE FOR TEXT FILES**
It is possible to lookup file directories by path, so we can store all data pertaining to a certain room type within its
own folder and simply reference and process the folder instead; this can be done through other programs which can then
be imported into this program

In this situation, a separate program can handle the files for each room type and return an array of all the relevant
files for each room
This program will then import this program, call the functions and store the value returned by the functions within
its own variables
These variables will then be used to process all files within it and replace each file with the object ID of the room
created through the data within the file

**By the end of the program, the puzzle_rooms, riddle_rooms and random_event_rooms variables should store an array of
all the room IDs which can then be used for map generation**

**IMPORTANT**
The class definitions will be stored in a separate file dedicated to only the classes and the relevant class methods

**HELP ON HOW TO USE THIS FILE FOR MAP GENERATION**
1. Import the module
2. Call the initialise_rooms function

This will set up the puzzle_rooms, riddle_rooms and random_event_rooms variables to store an array of all the room IDs
for each subsequent room type, which can then be used to generate the map.

IF THE INITIALISE_ROOMS FUNCTION IS NOT CALLED, IT WILL RESULT IN AN ERROR BECAUSE EACH VARIABLE WILL NOT BE UPDATED
PROPERLY

"""


from file_handling import initialise_array
from rooms import *

puzzle_rooms = initialise_array('puzzle')
riddle_rooms = initialise_array('riddle')
random_event_rooms = initialise_array('event')
# each of the functions called should return an array of text files


def create_riddle_rooms(riddle_room_var):
    """
    This function, given the variable that stores the RIDDLE files as a parameter, should process this variable by:
        1. iterating through the array stored within the variable
        2. creating the rooms based on the data within each file
        3. subsequently replacing each file in the array with the newly created room's ID.

    The format of riddle_files for reference are as follows:
    <undecided at the moment>

    Use the following file format as a reference on how to read each file and set each room's attributes

    As a buffer, let the function print ('Creating riddle rooms...') and have the program sleep for an amount of time
    This buffer can also ensure that the right function is being called

    """

    pass


def create_event_rooms(event_room_var):
    """
    This function, given the variable that stores the EVENT files as a parameter, should process this variable by:
        1. iterating through the array stored within the variable
        2. creating the rooms based on the data within each file
        3. subsequently replacing each file in the array with the newly created room's ID.

    The format of event_files for reference are as follows:
    <undecided at the moment>

    Use the following file format as a reference on how to read each file and set each room's attributes

    As a buffer, let the function print ('Creating event rooms...') and have the program sleep for an amount of time
    This buffer can also ensure that the right function is being called

    """

    pass


def create_puzzle_rooms(puzzle_room_var):
    """
    This function, given the variable that stores the PUZZLE files as a parameter, should process this variable by:
        1. iterating through the array stored within the variable
        2. creating the rooms based on the data within each file
        3. subsequently replacing each file in the array with the newly created room's ID.

    The format of puzzle_files for reference are as follows:
    <undecided at the moment>

    Use the following file format as a reference on how to read each file and set each room's attributes

    As a buffer, let the function print ('Creating puzzle rooms...') and have the program sleep for an amount of time
    This buffer can also ensure that the right function is being called

    """

    pass


def initialise_rooms():
    """
    This function should only be used to help initialise the variables riddle_rooms, random_event_rooms and puzzle_rooms
    to contain the array of room IDs of each subsequent room type to be used in map generation

    """

    create_riddle_rooms(riddle_rooms)
    create_event_rooms(random_event_rooms)
    create_puzzle_rooms(puzzle_rooms)
