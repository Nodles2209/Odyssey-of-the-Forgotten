"""
https://stackoverflow.com/questions/30379228/how-to-define-a-list-of-file-objects-in-python for help, but still write
documentation for the code written for easier code maintenance

"""

import os


def return_other_files(path):
    """
    This function, given the path directory of the other_rooms folder as a parameter, should return an array of all the
    files within the other_rooms folder

    """

    pass


def return_puzzle_files(path):
    """
    This function, given the path directory of the puzzle folder as a parameter, should return an array of all the files
    within the puzzle folder

    """

    pass


def return_riddle_files(path):
    """
    This function, given the path directory of the riddle folder as a parameter, should return an array of all the files
    within the riddle folder

    """

    pass


def return_event_files(path):
    """
    This function, given the path directory of the event folder as a parameter, should return an array of all the files
    within the event folder

    """

    pass


def initialise_array(room_type):
    """
    This function will take in a room type as a parameter and RETURN an array of text files that correspond to the room
    type parsed through the function.
    **This will be achieved using the relevant file handling methods for each room type that have been defined above**

    As a buffer, let the function print ('Initialising <room_type> rooms...') and have the program sleep for an amount
    of time before returning the array
    This buffer can also ensure that the right command is being executed

     **THIS DOCTEST IS SUBJECT TO CHANGE**

    For example:
    >>> initialise_array('puzzle')
    Initialising puzzle rooms...
    [<_io.TextIOWrapper name='sudokuPuzzle1.txt' mode='r' encoding='cp1252'>, <_io.TextIOWrapper name='sudokuPuzzle2.txt' mode='r' encoding='cp1252'>]
    >>> initialise_array('riddle')
    Initialising riddle rooms...
    [<_io.TextIOWrapper name='riddle1.txt' mode='r' encoding='cp1252'>, <_io.TextIOWrapper name='riddle2.txt' mode='r' encoding='cp1252'>]
    >>> initialise_array('event')
    Initialising event rooms...
    [<_io.TextIOWrapper name='event1.txt' mode='r' encoding='cp1252'>, <_io.TextIOWrapper name='event2.txt' mode='r' encoding='cp1252'>]
    >>> initialise_array('other')
    Initialising beginning and final rooms...
    [<_io.TextIOWrapper name='beginning_room.txt' mode='r' encoding='cp1252'>, <_io.TextIOWrapper name='final_room.txt' mode='r' encoding='cp1252'>]

    **NOTE FOR DOCTEST**
    This doctest is only here for help into writing the logic for this method
    This doctest should only be used with specific text files 'sudokuPuzzle1.txt', 'sudokuPuzzle2.txt', 'riddle1.txt',
    'riddle2.txt', 'event1.txt' and 'event2.txt'
    These test files have not yet been created so when you are writing the logic for this function, create this test
    files first
    THIS DOCTEST IS NOT INDICATIVE OF WHAT THE FINAL VERSION OF THIS FUNCTION WILL OUTPUT, IT IS JUST HERE TO SERVE AS
    A GENERAL PLAN ON WHAT ARGUMENTS ARE EXPECTED AND WHAT AN OUTPUT CAN LOOK LIKE

    **NOTES FOR THE FINAL VERSION OF THIS FUNCTION**
    The final version of this function will return an array with more elements than what this doctest can account for,
    therefore, once the basic logic of this function has been written and tested with the doctest, THE DOCTEST MUST BE
    REMOVED AND THE TEST FILES MUST NOT BE HARDCODED INTO THIS PROGRAM

    """

    pass
