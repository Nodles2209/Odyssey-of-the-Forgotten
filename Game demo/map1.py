from random import seed                                                                
from random import choice

init_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0 ,0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

init_room = {'1': [0, 0], '2': [0, 0], '3': [0, 0],
             '4': [0, 0], '5': [0, 0], '6': [0, 0],
             '7': [0, 0], '8': [0, 0], '9': [0, 0],
             '10': [0, 0]}

def printmap(testmap):                                                                 
    print('\n')
 
    for row in range(9):
        for col in range(9):
 
            if row % 2 == 0:
                if testmap[row][col] != 1 and testmap[row][col] != 0:
                    if testmap[row][col] == 2:
                        print('\033[92m[START]', end='')
 
                    else:
                        print('\033[94m[ROOM' + str(testmap[row][col] - 2) + ']', end='')
 
                else:
                    if testmap[row][col] == 1:
                        print('\033[93m----', end='')
                    else:
                        if col % 2 == 0:
                            print('\033[90m[     ]', end='')
                        else:
                            print('    ', end='')
 
            else:
                if testmap[row][col] == 1:
                    print('\033[93m  |||  ', end='')
 
                if testmap[row][col] == 0:
                    if col % 2 == 0:
                        print('       ', end='')
 
                    else:
                        print('    ', end='')
 
        print('\033[95m\n')

def random_direction():
 
    seed(None, version=1)
    i = 0
    final = []
 
    while i < 4:
        direction = choice(['north', 'south', 'east', 'west'])
 
        if direction not in final:
            final.append(direction)
            i += 1
        
    return final # return the direction in random order

def direction_firstmap(row, col, direction, room_number):
    
    if direction == 'north' and (row - 2) > -1:
        init_map[row - 1][col] = 1
        init_map[row - 2][col] = room_number

        room_number += 1
    
    elif direction == 'south' and (row + 1) < 9:
        init_map[row + 1][col] = 1
        init_map[row + 2][col] = room_number

        room_number += 1

    elif direction == 'east' and (col + 1) < 9:
        init_map[row][col + 1] = 1
        init_map[row][col + 2] = room_number

        room_number += 1

    elif direction == 'west' and (col - 1) > -1:
        init_map[row][col - 1] = 1
        init_map[row][col - 2] = room_number

        room_number += 1

    else:
        pass
    
    return [init_map, room_number]

def map_map(first_map):
    for row in range(9):
        for col in range(9):
            if first_map[row][col] != 1 and first_map[row][col] != 0:

                init_room[str(first_map[row][col] - 1)][0] = row
                init_room[str(first_map[row][col] - 1)][1] = col

    return init_room

def first_map_gen():
    seed(None, version=1)
    row = choice([0, 2, 4, 6, 8])
    col = choice([0, 2, 4, 6, 8])

    init_map[row][col] = 2

    directions = random_direction()

    room_number = 3

    for element in directions:

        collection = direction_firstmap(row, col, element, room_number)

        first_map = collection[0]

        room_number = collection[1]

    #printmap(first_map)
    #map_map(first_map)

    return collection

