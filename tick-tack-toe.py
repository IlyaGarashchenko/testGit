import numpy, os, string

def print_table(matrix):
    """
    :param matrix:
    :return:
    """
    size = 15
    print("-" * size)

    for open in matrix:
        write = ' | '
        for x in open:
            if x == 0:
                c = ' '
            elif x == 1:
                c = 'X'
            elif x == 2:
                c = 'O'
            write += c + ' | '
        print(write)
        print("-" * size)

def get_empty_matrix(size_x, size_y, value):
    """
        Gets size_x and size_y and returns matrix of 0,0 of that size
        :param matrix:
        :param size_x:
        :param size_y:
        :return:
        """
    # line where is will our list
    my_list = []
    # loop which say how lists wil be in list
    for count_x in range (0, size_x):
    # time list in which we put inside value
        temp_list = []
    # loop which say how much element we put in each list
        for count_y in range (0, size_y):
    #append element for list
            temp_list.append(value)
        my_list.append(temp_list)
    return my_list

def set_matrix_value(use_matrix, x, y, value):
    """
    Assigns a value inside the matrix
    :param matrix:
    :param x:
    :param y:
    :param value:
    :return:
    """


    # Check to see if x and y both are intergers

    try:
        x = int(x)
        y = int(y)
    except ValueError:
        return False

    # Check to see if range given is correct inside matrix
    if x > 3 or y > 3 or x < 0 or y < 0:
        return False

    if x == ' ' or y == ' ':
        return False


    if x < len(use_matrix):
        if y < len(use_matrix[y]):
            # Check to see if there is already value
            if use_matrix[x][y] == 0:
                # No value, good. We set one now. And return True
                use_matrix[x][y] = value
                return True
            else:
                # There is a value, the square is taken, return False
                return False
    # Invalid Range
    return False

def check_winner(matrix):
    """
    Check if someone won in matrix
    :param matrix:
    :return:
    """
    new_matrix = matrix[:]
    for win_coord in new_matrix:
        if win_coord[0] == 0:
            continue
        if win_coord[0] == win_coord[1] == win_coord[2]:
            return True

    for win_coord in numpy.transpose(new_matrix):
        if win_coord[0] == 0:
            continue
        if win_coord[0] == win_coord[1] == win_coord[2]:
           return True

    if ((new_matrix[0][0] == new_matrix[1][1] == new_matrix[2][2])) and (new_matrix[0][0] != 0):
       return True

    if ((new_matrix[0][2] == new_matrix[1][1] == new_matrix[2][0])) and (new_matrix[0][2] != 0):
       return True

    return False

# Creating an empty Matrix for our Tic-Tac-Toe game
matrix = get_empty_matrix(3, 3, 0)
print_table(matrix)

flag_in_game = True

while flag_in_game == True:
    # Iterating Between Player 1 and Player 2
    for y in range(1, 3):
        result = False
        # Checking that input of player is correct
        while result == False:
           x = input("Player " + str(y) + " - Tell me where to put: ")
           temp_list = x.split(' ')
           if len(temp_list) != 2:
               result = False
           else:
               result = set_matrix_value(matrix, temp_list[0], temp_list[1], y)
           if result == False:
             print("Please Try Again !")
           else:
             os.system("cls")

        # Checking if there is victory
        if check_winner(matrix) == True:
           print("Player " + str(y) + " You are win!")
           print_table(matrix)
           break

        print_table(matrix)




    












