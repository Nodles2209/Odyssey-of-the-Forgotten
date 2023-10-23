from random import randint
from random import seed

class puzzles:

    def p1(current_room, running):

        while running:
            user_input = input('\n type "1" to get the items, type "pass" to skip')
            if user_input == '1':
                print('Passed')
                print('You can take ' + str(current_room['object']) + ' now ;)')

                current_room['items'].append(current_room['object']) # the object is now added to the list of items
                current_room['score'] = 1   # add the player's socre for this puzzle [1]

                running = False

            elif user_input == 'pass':
                print('Bye')
                break
            else:
                print('try again')

        return current_room

    def p2(current_room, running):
    
        while running:
            user_input = input('\n type "2" to get the items, type "pass" to skip')
            if user_input == '2':
                print('Passed')
                print('You can take ' +  str(current_room['object']) + ' now ;)')

                current_room['items'].append(current_room['object'])
                current_room['score'] = 1

                running = False
            elif user_input == 'pass':
                print('Bye')
                break
            else:
                print('try again')
    
        return current_room
    
    
    def p3(current_room, running):
    
        while running:
            user_input = input('\n type "3" to get the items, type "pass" to skip')
            if user_input == '3':
                print('Passed')
                print('You can take ' +  str(current_room['object']) + ' now ;)')

                current_room['items'].append(current_room['object'])
                current_room['score'] = 1

                running = False
            elif user_input == 'pass':
                print('Bye')
                break
            else:
                print('try again')
    
        return current_room
    
    def p4(current_room, running):
    
        while running:
            user_input = input('\n type "4" to get the items, type "pass" to skip')
            if user_input == '4':
                print('Passed')
                print('You can take ' +  str(current_room['object']) + ' now ;)')

                current_room['items'].append(current_room['object'])
                current_room['score'] = 1

                running = False
            elif user_input == 'pass':
                print('Bye')
                break
            else:
                print('try again')
    
        return current_room
    
    def p5(current_room, running):
    
        while running:
            user_input = input('\n type "5" to get the items, type "pass" to skip')
            if user_input == '5':
                print('Passed')
                print('You can take ' +  str(current_room['object']) + ' now ;)')

                current_room['items'].append(current_room['object'])
                current_room['score'] = 1

                running = False
            elif user_input == 'pass':
                print('Bye')
                break
            else:
                print('try again')
    
        return current_room
    
    def p6(current_room, running):
    
        while running:
            user_input = input('\n type "6" to get the items, type "pass" to skip')
            if user_input == '6':
                print('Passed')
                print('You can take ' +  str(current_room['object']) + ' now ;)')

                current_room['items'].append(current_room['object'])
                current_room['score'] = 1

                running = False
            elif user_input == 'pass':
                print('Bye')
                break
            else:
                print('try again')
    
        return current_room
    
    def p7(current_room, running):
    
        while running:
            user_input = input('\n type "7" to get the items, type "pass" if you to skip')
            if user_input == '7':
                print('Passed')
                print('You can take ' +  str(current_room['object']) + ' now ;)')

                current_room['items'].append(current_room['object'])
                current_room['score'] = 1

                running = False
            elif user_input == 'pass':
                print('Bye')
                break
            else:
                print('try again')
    
        return current_room
    
    def p8(current_room, running):
    
        while running:
            user_input = input('\n type "8" to get the items, type "pass" to skip')
            if user_input == '8':
                print('Passed')
                print('You can take ' +  str(current_room['object']) + ' now ;)')

                current_room['items'].append(current_room['object'])
                current_room['score'] = 1

                running = False
            elif user_input == 'pass':
                print('Bye')
                break
            else:
                print('try again')
    
        return current_room
    
    def p9(current_room, running):
    
        while running:
            user_input = input('\n type "9" to get the items, type "pass" to skip')
            if user_input == '9':
                print('Passed')
                print('You can take ' +  str(current_room['object']) + ' now ;)')

                current_room['items'].append(current_room['object'])
                current_room['score'] = 1

                running = False
            elif user_input == 'pass':
                print('Bye')
                break
            else:
                print('try again')
    
        return current_room

def select_puzzles(current_room, score): # needs to be changed [score]

    seed(None, version=1)

    p = randint(1,9)

    if p == 1:
        current_room = puzzles.p1(current_room, score)

    elif p == 2:
        current_room = puzzles.p2(current_room, score)

    elif p == 3:
        current_room = puzzles.p3(current_room, score)

    elif p == 4:
        current_room = puzzles.p4(current_room, score)

    elif p == 5:
        current_room  = puzzles.p5(current_room, score)

    elif p == 6:
        current_room = puzzles.p6(current_room, score)

    elif p == 7:
        current_room = puzzles.p7(current_room, score)

    elif p == 8:
        current_room = puzzles.p8(current_room, score)

    elif p == 9:
        current_room = puzzles.p6(current_room, score)

    else:
        print('error')

    return current_room

