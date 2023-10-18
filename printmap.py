testmap = [[2, 1, 3, 1, 4, 1, 9],
       [1, 0, 1, 0, 0, 0, 0],
       [5, 0, 6, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 0, 0],
       [10, 1, 7, 1, 8, 0, 0]]

# the room number and connection state is stored in a 2d matrix
# room number = (numbers other than '1' and '0') - 1
# '1' is connected, '0' is disconnect


print('\n\n')

for row in range(5): # max 5 rows
    for col in range(7): # go through every element in the matrix
        
        # check if it is connected horizontally
        if row % 2 == 0: # if row = 0, 2, 4 
            if testmap[row][col] != 1 and testmap[row][col] != 0: # check if it is a room
                print('[ROOM' + str(testmap[row][col] - 1) + ']', end='')
            else:
                if testmap[row][col] == 1: # connected
                    print('----', end='')
                else:
                    print('    ', end='') # disconnect
        # vertically
        else:
            if testmap[row][col] == 1:
                print('  |||  ', end='')
            
            if testmap[row][col] == 0:  # leave more empty spaces if it is the first element
                if col == 0:
                    print('       ', end='')
                
                else:
                    print('    ', end='')
        

        if col == 6:
            print('\n')

