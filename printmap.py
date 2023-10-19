"""

Rooms and connections are stored as a 2D matrix where:
    1 or 0 determine connection status (1 indicating there is a connection present and 0 indicating no connection),
    Room number is any integer greater than one (then subtracted by 1),
    for example :
    Room 1 = 2 on the matrix,
    Room 9 = 10 on the matrix,
    and so on for all the rooms

**IMPORTANT**
Room display logic is SUBJECT TO CHANGE since formatting for room numbers with digits greater than one have not been
considered yet

This program is also SUBJECT TO CHANGE to be made into a function for later use; is currently in TESTING state, using
predefined values

"""

test_map = [[2, 1, 3, 1, 4, 1, 9],  # every 4th row holds room data, starting from row 1 (index 0)

            [1, 0, 1, 0, 0, 0, 0],  # the 3 rows after the room data row holds vertical connection data, including
            [1, 0, 1, 0, 0, 0, 0],  # formatting for print display - mainly for aesthetic purposes
            [1, 0, 1, 0, 0, 0, 0],

            [5, 0, 6, 0, 0, 0, 0],

            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],

            [10, 1, 7, 1, 8, 0, 0]]


print('\n')

rows = len(test_map)  # number of times to iterate for rows
cols = len(test_map[1])  # number of times to iterate for columns, should be the same for all rows

for row in range(rows):  # goes through each row
    for col in range(cols):  # goes through each element within a row

        # first checks if the row is holding room data or vertical connections data
        if row % 4 == 0:  # changed this to every 4 because of changed matrix logic

            # checks if there is a room in each element
            if test_map[row][col] != 1 and test_map[row][col] != 0:
                print(f'[ROOM {test_map[row][col] - 1}]', end='')
                # changed this to use an f string; generally better than concatenating and converting variables to print

            else:

                # checks if the element is a horizontal connection or not
                if test_map[row][col] == 1:
                    print('=====', end='')
                else:
                    print('     ', end='')

        else:

            if test_map[row][col] == 1:
                print('   ||  ', end='')

            # whitespace formatting
            if test_map[row][col] == 0:

                # slightly more whitespace if it is the first element
                if col == 0:
                    print('       ', end='')

                else:
                    print('      ', end='')

        if col == 6:
            print('\n', end='')  # changed this to not create a newline between connections
