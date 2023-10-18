testmap = [[2, 1, 3, 1, 4, 1, 9],
       [1, 0, 1, 0, 0, 0, 0],
       [5, 0, 6, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 0, 0],
       [10, 1, 7, 1, 8, 0, 0]]


print('\n\n')

for row in range(5):
    for col in range(7):
        
        if row % 2 == 0:
            if testmap[row][col] != 1 and testmap[row][col] != 0:
                print('[ROOM' + str(testmap[row][col] - 1) + ']', end='')
            else:
                if testmap[row][col] == 1:
                    print('----', end='')
                else:
                    print('    ', end='')

        else:
            if testmap[row][col] == 1:
                print('  |||  ', end='')
            
            if testmap[row][col] == 0:
                if col == 0:
                    print('       ', end='')
                
                else:
                    print('    ', end='')
        

        if col == 6:
            print('\n')

