from random import seed                                                                
from random import choice

init_map = [[0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0 ,0, 0]]

def printmap(testmap):                                                                 
    print('\n\n')
 
    for row in range(5):
        for col in range(7):
 
            if row % 2 == 0:
                if testmap[row][col] != 1 and testmap[row][col] != 0:
                    if testmap[row][col] == 2:
                        print('[START]', end='')
 
                    else:
                        print('[ROOM' + str(testmap[row][col] - 1) + ']', end='')
 
                else:
                    if testmap[row][col] == 1:
                        print('----', end='')
                    else:
                        if col % 2 == 0:
                            print('       ', end='')
                        else:
                            print('    ', end='')
 
            else:
                if testmap[row][col] == 1:
                    print('  |||  ', end='')
 
                if testmap[row][col] == 0:
                    if col % 2 == 0:
                        print('       ', end='')
 
                    else:
                        print('    ', end='')
 
 
        print('\n')
    print('='*80)

def random_direction():
 
    seed(None, version=2)
    i = 0
    final = []
 
    while i < 4:
        direction = choice(['north', 'south', 'east', 'west'])
 
        if direction not in final:
            final.append(direction)
            i += 1
        
    return final # return the direction in random order

def direction_map(row, col, direction):
    
    if direction == 'north' and (row - 2) > -1:
        init_map[row - 1][col] = 1
        init_map[row - 2][col] = 3
    
    elif direction == 'south' and (row + 1) < 5:
        init_map[row + 1][col] = 1
        init_map[row + 2][col] = 4
    
    elif direction == 'east' and (col + 1) < 7:
        init_map[row][col + 1] = 1
        init_map[row][col + 2] = 5
    
    elif direction == 'west' and (col - 1) > -1:
        init_map[row][col - 1] = 1
        init_map[row][col - 2] = 6
    
    else:
        print('direction error :/')
    
    return init_map

def map_generator():
    seed(None, version=1)
    row = choice([0, 2, 4])
    col = choice([0, 2, 4, 6])

    init_map[row][col] = 2 # START

    directions = random_direction() # list of random directions

    for element in directions:
        final_map = direction_map(row, col, element)

    printmap(final_map)


map_generator()
