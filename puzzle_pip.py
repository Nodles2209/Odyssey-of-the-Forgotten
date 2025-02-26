from string import punctuation


def puzzle_pip():
    def input_filter(text):
        user_input = ''

        for element in text:
            if not (element in punctuation):
                user_input = user_input + element

        user_input = (user_input.lower().split())

        return user_input

    # N1 W2 E3 S4
    t1 = ['--***--', '| *** |', '| *** |', '--***--', 'NS']
    t2 = ['--***--', '| *****', '| *****', '-------', 'NE']
    t3 = ['--***--', '***** |', '***** |', '-------', 'NW']
    t4 = ['-------', '| *****', '| *****', '--***--', 'ES']
    t5 = ['-------', '***** |', '***** |', '--***--', 'WS']
    t6 = ['-------', '*******', '*******', '-------', 'WE']
    t7 = ['-------', '|?????|', '|?????|', '-------', '00']
    t8 = ['       ', '<<<<<< ', '<<<<<< ', '       ', 'E1']
    t9 = ['       ', '       ', '       ', '       ', '00']
    
    init_map = [[t8, t7, t7, t7, t7, t7, t7, t9],
                [t9, t7, t7, t7, t7, t7, t7, t9],
                [t9, t7, t7, t7, t7, t7, t4, t8],
                [t9, t7, t7, t7, t7, t7, t1, t9],
                [t9, t7, t7, t7, t7, t7, t2, t9],
                [t9, t7, t7, t7, t7, t7, t7, t9]]
    
    whole_map = [[t8, t1, t6, t2, t1, t5, t1, t9],
                [t9, t5, t2, t3, t3, t6, t2, t9],
                [t9, t2, t4, t5, t6, t3, t4, t8],
                [t9, t3, t6, t4, t2, t6, t1, t9],
                [t9, t1, t1, t6, t2, t4, t2, t9],
                [t9, t2, t5, t6, t2, t5, t3, t9]]
    
    def print_map(p_map):
        print('\033[95m            1       2       3       4       5       6')
    
        for row in range(6):
    
            for element in range(4):
    
                for col in range(8):
                    if col == 1:
                        if element == 1 or element == 2:
    
                            print('\033[95m' + str(row), end='')
                        else:
                            print(' ', end='')
        
                    block = p_map[row][col]
    
                    for e in block[element]:
                    
                        if e == '-' or e == '|':
                            print('\033[36m' + e, end='')
    
                        elif e == ' ' or e == '?':
                            print('\033[94m' + e, end='')
    
                        else:
                            print('\033[92m' + e, end='')
    
                    print(' ', end='')
    
                print()
    
    def check_puzzle(map_map):
        row = 2
        col = 7
    
        if 'E' in map_map[row][col - 1][4]:
    
            col -= 1
    
            running = True
            record = 'E'
    
            while running:
                
                for element in map_map[row][col][4]:
    
                    if element != record:
    
                        if element == 'N' and ('S' in map_map[row - 1][col][4]):
                            row -= 1
                            record = 'S'
                            break
        
                        elif element == 'W' and ('E' in map_map[row][col - 1][4]):
                            col -= 1
                            record = 'E'
                            break
        
                        elif element == 'E' and ('W' in map_map[row][col + 1][4]):
                            col += 1
                            record = 'W'
                            break
        
                        elif element == 'S' and ('N' in map_map[row + 1][col][4]):
                            row += 1
                            record = 'N'
                            break
        
                        else:
                            print('Wrong')
                            running = False
                            break 
    
                if '1' in map_map[row][col][4]: # complete
                    print('Finish')
                    print('\033[97m')
                    running = False
        else:
            print('WRONG START')

    complete_pip = False
    
    print('Connect the wire to start the plane or EXIT')
    print('Type "open <x> <y>" to uncover the wire pattern stored in the given x,y coordinates on the grid')
    print('OR')
    print('Type "swap <x1> <y1> <x2> <y2>" to swap the wire pattern stored in the coordinates given in x1, y1 to the ones'
          'stored in x2, y2')
    print('Example: ')
    print('"open 0 1" would uncover the wire pattern in 0, 1')
    print('"swap 0 1 2 6" would swap the wire pattern in 0, 1 with the one in 2, 6')
    print('submit when you finish by entering keywords "submit" and then "exit"\n')
    print_map(init_map)
    map_map = init_map
    while True:
        print('\033[92m')
        user_input = input('>>> ')
    
        user_input = input_filter(user_input)
    
        if user_input[0] == 'open' and len(user_input) == 3:
    
            if (int(user_input[1]) >= 0 and int(user_input[1]) < 6) and (int(user_input[2]) > 0 and int(user_input[2]) < 7):
    
                map_map[int(user_input[1])][int(user_input[2])] = whole_map[int(user_input[1])][int(user_input[2])]
                print_map(map_map)
            else:
                print('You cannot open it')
    
        elif user_input[0] == 'swap' and len(user_input) == 5:
    
            try:
                sweap = map_map[int(user_input[1])][int(user_input[2])]
                map_map[int(user_input[1])][int(user_input[2])] = map_map[int(user_input[3])][int(user_input[4])]
                map_map[int(user_input[3])][int(user_input[4])] = sweap
    
                print_map(map_map)
    
            except IndexError:
                print('You cannot swap them')
    
        elif user_input[0] == 'submit':
                    row = 2
                    col = 7
    
                    if 'E' in map_map[row][col - 1][4]:
    
                        col -= 1
    
                        running = True
                        record = 'E'
    
                        while running:
                
                            for element in map_map[row][col][4]:
    
                                if element != record:
    
                                    if element == 'N' and ('S' in map_map[row - 1][col][4]):
                                        row -= 1
                                        record = 'S'
                                        break
        
                                    elif element == 'W' and ('E' in map_map[row][col - 1][4]):
                                        col -= 1
                                        record = 'E'
                                        break
        
                                    elif element == 'E' and ('W' in map_map[row][col + 1][4]):
                                        col += 1
                                        record = 'W'
                                        break
        
                                    elif element == 'S' and ('N' in map_map[row + 1][col][4]):
                                        row += 1
                                        record = 'N'
                                        break
        
                                    else:
                                        print('Wrong')
                                        running = False
                                        break 
    
                            if '1' in map_map[row][col][4]: # complete
                                print('Finish type EXIT')
                                print('\033[97m')
                                complete_pip = True
                                break
                                
                    else:
                        print('WRONG START')
    
        elif user_input[0] == 'exit':
            print('\033[97m')
            break
    
        else:
            print('This does not make any sense ')
    return complete_pip
