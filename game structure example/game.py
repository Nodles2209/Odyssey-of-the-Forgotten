from command import *
from map import *
from items import *
from parser import *

Pack_MAX = 10

class backpack:

    def backpack_mass(Backpack):
        mass = 0
        return sum([mass + element['mass'] for element in Backpack]) # totoal mass of the items in backpack
    
    def backpack_menu(Backpack): # list everything in backpack
        print('\033[94m')
        for element in Backpack:
            textout(element['name'] + ' ' + str(element['mass']))

        print('\033[93mMass:' + str(backpack.backpack_mass(Backpack)))

    def add_items_backpack(items, Backpack, current_room):
        if (backpack.backpack_mass(Backpack) + items['mass']) <= Pack_MAX:
            Backpack.append(items)
            current_room['items'].remove(items)

        else:
            print('\033[91m')
            textout('You cannot take this, your backpack is full !')

        return [current_room, Backpack]
    
    def remove_items_backpack(items, Backpack):

        Backpack.remove(items) # remove item
        print('\033[36mYou dropped ' + items['id'] + ' :)')

        return Backpack

def main():

    current_room = room_reception
    Backpack = [item_id, item_laptop, item_money]

    print_room_menu(current_room)

    while True:
        print('\033[92m')
        user_input = input('>>> ')

        command = input_filter(user_input)
        player = commands.execute_commands(command, current_room, Backpack)
        current_room = player[0]
        Backpack = player[1]     # pass data for next 

if __name__ == "__main__":
    main()

