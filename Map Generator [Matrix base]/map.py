from random import seed
    
from random import randint

from map1 import *

def direction_map(row, col, direction, room_number, mmap):

     if direction == 'north' and (row - 2) > -1:
         if mmap[row - 2][col] == 1 or mmap[row - 2][col] == 0: # if there is a room there, connect it
             mmap[row - 2][col] = room_number
             mmap[row - 1][col] = 1
             room_number += 1

         else:
             mmap[row - 1][col] = 1

     elif direction == 'south' and (row + 1) < 9:
         if mmap[row + 2][col] == 1 or mmap[row + 2][col] == 0:
             mmap[row + 2][col] = room_number
             mmap[row + 1][col] = 1
             room_number += 1

         else:
             mmap[row + 1][col] = 1

     elif direction == 'east' and (col + 1) < 9:
         if mmap[row][col + 2] == 1 or mmap[row][col + 2] == 0:
             mmap[row][col + 2] = room_number
             mmap[row][col + 1] = 1
             room_number += 1

         else:
             mmap[row][col + 1] = 1

     elif direction == 'west' and (col - 1) > -1:
         if mmap[row][col - 2] == 1 or mmap[row][col - 2] == 0:
             mmap[row][col - 2] = room_number
             mmap[row][col - 1] = 1
             room_number += 1

         else:
             mmap[row][col - 1] = 1

     else:
         pass
     return [mmap, room_number]

def final_map_gen(first_map,room_number):

    seed(None, version=1)
    
    random_room = randint(2, room_number)
    exits = randint(1, 3)
    
    room = map_map(first_map)
    
    row = room[str(room_number - 2)][0]
    col = room[str(room_number - 2)][1]
    
    while exits > (12 - room_number):
        exits -= 1

    directions = random_direction()

    i =  0
    while i < exits:
    
        direction = directions[i]
    
        collection = direction_map(row, col, direction, room_number, first_map)
    
        first_map = collection[0]
        room_number = collection[1]
    
        i += 1
    return [first_map, room_number]

def main():

    collection = first_map_gen()
    first_map = collection[0]
    room_number = collection[1]
    collection = final_map_gen(first_map, room_number)
    first_map = collection[0]
    room_number = collection[1]
    while room_number < 12:
        collection = final_map_gen(first_map, room_number)
        first_map = collection[0]
        room_number = collection[1]
    final_map = collection[0]
    return final_map

final_map = main()
printmap(final_map)
