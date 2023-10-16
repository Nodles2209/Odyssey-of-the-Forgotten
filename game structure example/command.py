from parser import *
from map import *
from items import *
from game import backpack

def print_room_menu(current_room):

    print('\033[92m')
    textout(current_room['description'])
    
    print('\033[93m')
    for element in current_room['exits']:
        print('GO ' + element + ' to ' + current_room['exits'][element])
        
    print('\033[94m')  
    for element in current_room['items']:
        print('TAKE ' + element['name'] + ' Mass: ' + str(element['mass']))

    print("\n\033[91m[Type 'help' for help]")

class commands:
    
    def go (direction, current_room, Backpack):

        if direction in current_room['exits']: # check if the player can go in that direction 
            current_room = rooms[current_room['exits'][direction]]
            print('\n\033[36m[You are in ' + current_room['name'] + ']')
            print_room_menu(current_room)

        else:
            print('\033[91m')
            textout('You cannot go in that direction :/ ')

        return [current_room, Backpack]
    
    def take (item_take, current_room, Backpack):

        try:
            if items[item_take] in current_room['items']: # check if the item is in the room
                    player = backpack.add_items_backpack(items[item_take], Backpack, current_room)
                    current_room = player[0]
                    Backpack = player[1]
                    print('\033[36mYou took ' + items['id'] + ' :)')
                    
            else:
                print('\033[91m')
                textout('This item is not here :/')

        except KeyError:
            print('\033[91m')
            textout('You cannot take this :/')

        return [current_room, Backpack]

    def drop (item_drop, current_room, Backpack):

        try:
            if items[item_drop] in Backpack: # check if the item is in backpack
                Backpack = backpack.remove_items_backpack(items[item_drop], Backpack)
                current_room['items'].append(items[item_drop])

            else:
                print('\033[91m')
                textout('This item is not in your backpack :/')

        except KeyError:
            print('\033[91m')
            textout('You cannot drop this :/ ')

        return [current_room, Backpack]

    def check (item_check, current_room, Backpack):

        try:  # the item should be in either current_room or Backpack
            if (items[item_check] in current_room['items']) | (items[item_check] in Backpack):
                print('\033[36m')
                textout(items[item_check]['description'])
            else:
                print('\033[91m')
                textout('This item is not here :/ ')
        except KeyError:
            print('\033[91m')
            textout('What is that ?')

    def execute_commands (command, current_room, Backpack):
        try:

            if len(command) != 0: # no input

                if command[0] == 'go':
    
                    if len(command) > 1:
    
                        player = commands.go(command[1], current_room, Backpack)
                        current_room = player[0]
                        Backpack = player[1]
    
                    else:
                        textout('go where ?')
                    
                elif command[0] == 'take':
    
                    if len(command) > 1:
    
                        player = commands.take(command[1], current_room, Backpack)
                        current_room = player[0]
                        Backpack = player[1]
    
                    else:
                        textout('take what ?')
    
                elif command[0] == 'drop':
    
                    if len(command) > 1:
    
                        player = commands.drop(command[1], current_room, Backpack)
                        current_room = player[0]
                        Backpack = player[1]
    
                    else:
                        textout('drop what ?')
    
                elif command[0] == 'check':
                    
                    if len(command) > 1:
    
                        if command[1] == 'backpack':
                            backpack.backpack_menu(Backpack)
    
                        elif command[1] == 'room':
                            print_room_menu(current_room)
    
                        else:
                            commands.check(command[1], current_room, Backpack)
    
                elif command[0] == 'help':
                    print("\n\033[36mCHECK backpack, CHECK room\nType 'exit' to quit the game :) ")
    
                elif command[0] == 'exit':
                    print('\033[91m')
                    print('\033[5mYOU ARE OUT !\n')
                    exit()
    
                else:
                    print('\033[91m')
                    textout('This does not make any sense [O.o]?')

            else:
                textout('Ah what do you want ?')
        except TypeError:
            textout('WELL...')

        return [current_room, Backpack] # return current room and backpack to the main loop
