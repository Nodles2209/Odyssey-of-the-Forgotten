from map1 import *
from map2 import *
from room import *
from parser import *

from puzzle import select_puzzles

class commands:

    def go (direction, current_room, game_room, Backpack):

        if direction in current_room['exits']:
            current_room = game_room[current_room['exits'][direction]]
            print('\nYou are in  ' + current_room['name'])

            if current_room['name'] != 'start':

                if current_room['score'] == 0:  # if the player didn't get the score

                    current_room = select_puzzles(current_room, True)

                    game_room.update(current_room)

                else:
                    pass

            else:
                textout('You are back :]')

        else:
            print('you cannot go in that direction')

        return [current_room, game_room, Backpack]

    def take (item_take, current_room, game_room, Backpack):

        try:
            if item_take in current_room['items']:

                current_room['items'].remove(item_take)
                game_room.update(current_room)
                Backpack.append(item_take)
                print('You took ' + item_take)

            else:
                print('This item is not here')

        except KeyError:
            print('You cannot take that !')

        return [current_room, game_room, Backpack]
    
    def drop (item_drop, current_room, game_room, Backpack):

        try:
            if item_drop in Backpack:

                Backpack.remove(item_drop)
                current_room['items'].append(item_drop)
                game_room.update(current_room)
                print('You droped ' + item_drop)

            else:
                print('This item is not even in your backpack')

        except KeyError:
            print('You cannot drop that !')

        return [current_room, game_room, Backpack]

def execute_commands(command, player):

    try:
        if len(command) != 0:

            if command[0] == 'go':

                if len(command) > 1:

                    player = commands.go(command[1], player[0], player[1], player[2])

                else:
                    textout('go where ?')


            elif command[0] == 'take':

                if len(command) > 1:

                    player = commands.take(command[1], player[0], player[1], player[2])

                else:
                    textout('take what ?')

            elif command[0] == 'drop':

                if len(command) > 1:

                    player = commands.drop(command[1], player[0], player[1], player[2])

            elif command[0] == 'exit':

                textout('YOU ARE OUT')
                exit()

            else:
                textout('This does not make amy sense !')
        else:
            textout('What do you want ?')

    except TypeError:
        pass

    return player

def mission_check(current_room, Backpack):

    if len(Backpack) == 9 and current_room['name'] == 'start':
        textout('The main story completed')

def main():

    game_map = map_gen()

    printmap(game_map)

    room_gen = map_map(game_map)

    game_room = room_dict(room_gen, game_map) # set up exits

    game_room = random_room(game_room) # set up items

   #print_room(game_room)

    current_room = game_room['1']
    Backpack = []

    player = [current_room, game_room, Backpack]

    while True:

        print('\033[92m')
        user_input = input('>>> ')

        command = input_filter(user_input)
        player = execute_commands(command, player)

        print('Backpack ' + str(player[2]))

        mission_check(player[0], player[2])

if __name__ == '__main__':

    main()

