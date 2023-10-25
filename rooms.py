"""
This program will only store the various classes and their subsequent methods;
This program is to be imported into room_creation to help create each room object

"""
from puzzle_data import alpha_2_num
import re
from time import sleep


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
        self.__hint_prompt = None  # type str - used to store the text for when a player needs a hint
        self.__complete_prompt = None  # type str - used to store the text for when a player has completed the room
        self.__complete_score = None  # type int - used to hold the score the player gets when completing the room
        self.__clear_condition = None  # type stored in this attribute depends on room type
        self.__isClear = False  # type bool - checks if the room is cleared or not; False until True
        self.__locked = None  # type str - None if the room isnt locked, else item id to unlock it
        self.__complete_item = None  # type str - item gained when completing puzzle, if item use item id, else None
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

    def set_is_clear(self, clear):  # sets a bool to determine whether the room is cleared
        self.__isClear = clear

    def get_locked(self):  # get whether the room is locked
        return self.__locked

    def set_locked(self, key):  # sets if the room is locked
        self.__locked = key

    def get_complete_item(self):  # gets the item id of the item you win if you complete the puzzle
        return self.__complete_item

    def set_complete_item(self, item_id):  # sets the complete item
        self.__complete_item = item_id

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


class Sudoku(Room):

    def __init__(self):
        super().__init__()
        self.__incomplete = None

    def get_incomplete(self):
        return self.__incomplete

    def set_incomplete(self, puzzle):
        self.__incomplete = puzzle

    def run_sudoku(self):
        """
        This function handles the sudoku puzzle, it takes in the current_room,
        it enters a while loop that is only broken when the player decides to leave (return False),
        or complete the puzzle (return True)

        Please see the puzzle_setup_info to see the format this sudoku is printed
        """

        original_incomplete_map = self.get_incomplete()
        incomplete_map = [list(row) for row in original_incomplete_map]  # Create a deep copy
        complete_map = self.get_clear_condition() # sets which complete sudoku to use

        while True:
            # Start print sudoku grid
            print("   " + "-" * 36)
            for y, y_val in enumerate(incomplete_map):
                line = ""  # empty string for appending to
                line += (str(9 - y) + " |")  # add the numbers for coordinates down the side
                for x, x_val in enumerate(y_val):  # enumerate returns the index and the value of list
                    if x_val == 0:
                        line += ("-?-")  # prints this symbol if empty space in grid
                    else:
                        line += (" " + str(x_val) + " ")  # prints the value of the square if not 0
                    if x == 2 or x == 5:
                        line += "|"  # used for formatting grid
                    else:
                        line += " "  # used for formatting grid
                line += "|"  # used for formatting grid
                print(line)  # prints the line that had information appended to
                if y == 2 or y == 5:
                    print("  |" + "-" * 36 + "|")  # used for formatting grid
                elif y == 8:
                    print("   " + "-" * 36)  # used for formatting grid
                else:
                    print("  |           |           |            |")  # used for formatting grid

            print("    A   B   C   D   E   F   G   H   I\n")  # gives the x coordinates
            # End print sudoku print

            # Check if sudoku is completed, return True if complete
            if complete_map == incomplete_map:
                return True

            # Here is the main code for the sudoku
            print("Access the grid one location at a time, using this format -> A1 = 5")
            print("Or exit the puzzle by entering EXIT")
            sudoku_input = input("Enter answers here: ")  # get input from player
            sudoku_input = sudoku_input.lower().split(" ")  # normalises input
            try:
                if sudoku_input[0] == "exit":  # checks if player wants to exit the puzzle
                    return False
                elif len(sudoku_input[2]) == 1 and sudoku_input[
                    2].isnumeric():  # checks for players input is formatted right
                    x = int(alpha_2_num[sudoku_input[0][
                        0]])  # gets x coordinate by using input into alpha to numeric dictionary found in puzzle data
                    y = 9 - int(sudoku_input[0][1])  # gets y coordinate
                    num = int(sudoku_input[2])  # gets the number the player wants to add

                    if incomplete_map[y][x] == 0:
                        if complete_map[y][x] == num:
                            incomplete_map[y][x] = num  # sets the new number in grid if correct
                        else:
                            print("Incorrect number!")
                    else:
                        print("Please choose coordinates labelled '-?-'")
                else:
                    print("Please retry checking your formatting, coordinates and answer")


            except IndexError:  # checks for formatted wrong
                print("Please enter in format explained")
            except KeyError:  # checks for formatted wrong
                print("Please enter in format explained")


class Chess(Room):

    def __init__(self):
        super().__init__()
        self.__board_turn = None
        self.__cutscenes = None

    def get_board_turn(self):
        return self.__board_turn

    def set_board_turn(self, boards):  # only used if creating an "unlucky room", which will be a single room
        self.__board_turn = boards

    def get_cutscenes(self):
        return self.__cutscenes

    def set_cutscenes(self, boards):
        self.__cutscenes = boards

    def answer_check(self, answer, user_answer):

        format_pattern = r'^(k|q|n|b|r|p)[a-h][1-8][a-h|x]{1,2}[1-8]$'
        format_check = re.match(format_pattern, user_answer)

        if user_answer == answer:
            return None
        elif format_check is None:
            print('Incorrect format, please try again')
        else:
            print('Incorrect answer, please try again')

        print("It's white's turn to play: ")

        user_input = input('Enter your input here: ')
        normalised_input = user_input.lower().strip()
        self.answer_check(answer, normalised_input)

    def run_chess(self):
        black_turns_display = self.__board_turn
        board_cutscenes = self.__cutscenes
        clear_conditions = self.get_clear_condition()

        number_of_steps = len(clear_conditions)

        print('Printing board...')
        sleep(0.5)
        print(board_cutscenes[0])
        sleep(0.5)

        print('For this puzzle, you must enter your move in the particular format: \n'
              '<chess piece>+<grid coordinate it currently is in>+<grid coordinate you want to move '
              'to> \n'
              'For example, if you want to move a king at c4 to c5, you would type "kc4c5"\n'
              'If you want to capture a piece, add a "x" between the coordinates you are at at the '
              'ones you want to move to\n'
              'For example, if a bishop at e8 captures a pawn at d6, you would type "be8xd6"\n'
              'The notation letter for each piece is as follows:\n'
              'king = k,\n'
              'queen = q,\n'
              'knight = n,\n'
              'bishop = b,\n'
              'rook = r,\n'
              'pawn = p,\n'
              'All of the terms must be typed together as a single input\n')
        print('If you want to complete the puzzle later, type "EXIT" to leave the puzzle')
        sleep(5)

        for index in range(number_of_steps):
            print("Black's turn: ")
            sleep(0.5)
            print(black_turns_display[index])
            sleep(0.5)

            print("It's now white's turn to play: ")

            user_input = input('Enter your input here: ')
            normalised_input = user_input.lower().strip()

            if normalised_input == 'exit':
                return False

            current_clear_condition = clear_conditions[index]
            white_turn_display = board_cutscenes[index+1]

            self.answer_check(current_clear_condition, normalised_input)
            print(white_turn_display)
            sleep(2)

        return True
