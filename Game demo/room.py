from map1 import *
from map2 import *


init_room = {'1': { 'name': 'start',
        
        'description': 'This is enterence',

        'object': '',   # what the player will get after the puzzle
        
        'items': [],
        
        'exits': {},

        'score': 0

},

 '2': { 'name': 'room1',

        'description': '',

        'object': '',

        'items': [],

        'exits': {},

        'score': 0

},

 '3': { 'name': 'room2',

        'description': '',

        'object': '',

        'items': [],

        'exits': {},

        'score': 0

},

 '4': { 'name': 'room3', 

        'description': '',

        'object': '',

        'items': [],

        'exits': {},

        'score': 0

},

 '5': { 'name': 'room4',

        'description': '',

        'object': '',

        'items': [],

        'exits': {},

        'score': 0

},

 '6': { 'name': 'room5',

        'description': '',

        'object': '',
        
        'items': [],

        'exits': {},

        'score': 0

},

 '7': { 'name': 'room6', 

        'description': '',

        'object': '',

        'items': [],

        'exits': {},

        'score': 0

},

 '8': { 'name': 'room7',

        'description': '',

        'object': '',

        'items': [],

        'exits': {},

        'score': 0

},

 '9': { 'name': 'room8',

        'description': '',

        'object': '',

        'items': [],

        'exits': {},

        'score': 0

},

'10': { 'name': 'room9',

        'description': '',

        'object': '',

        'items': [],

        'exits': {},

        'score': 0

},}

def room_dict(room_gen, game_map): # setting up room exits

    for element in room_gen:
    
        north = True
        south = True
        east = True
        west = True
    
        row = room_gen[element][0]
        col = room_gen[element][1]

        for e in range(4):

            if (game_map[row - 1][col] == 1) and north:

                init_room[element]['exits'].update({ 'north': str((game_map[row - 2][col]) - 1) })
                north = False

            elif (game_map[row + 1][col] == 1) and south:

                init_room[element]['exits'].update({ 'south': str((game_map[row + 2][col]) - 1) })
                south = False

            elif (game_map[row][col + 1] == 1) and east:

                init_room[element]['exits'].update({ 'east': str((game_map[row][col + 2]) - 1) })
                east = False

            elif (game_map[row][col - 1] == 1) and west:

                init_room[element]['exits'].update({ 'west': str((game_map[row][col - 2]) - 1) })
                west = False

            else:
                pass

    return init_room

def random_room(game_room):  # setting up random rooms

    list_of_main_item = ['object1', 'object2', 'object3', 'object4', 'object5', 'object6', 'tool1', 'tool2', 'tool3']

    from random import seed
    from random import randint

    seed(None, version=1)

    i = 2
    final = []
    
    while i < 11:

        objects = choice(list_of_main_item)

        if objects not in final:
            final.append(objects)
            if objects[0] == 'o':
                game_room[str(i)]['description'] = 'This is main room'
                game_room[str(i)]['object'] = objects
            else:
                game_room[str(i)]['description'] = 'This is optional room'
                game_room[str(i)]['object'] = objects

            i += 1
    
    return game_room

def print_room(game_room):  # for testing

    for element in game_room:
        print('NAME : ' + game_room[element]['name'])
        print((game_room[element]['description']).upper())
        print('OBJECT : ' + str(game_room[element]['object']))
        print('EXITS : ' + str(game_room[element]['exits']))

        print('\n')
