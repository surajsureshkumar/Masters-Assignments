"""
This is a  program which finds if skyscrapers are in
valid configuration that meets all the criteria for the puzzle

MY PROGRAM IS STRUCTURED LIKE THIS
puzzle-->output_matrix-->duplicate-->building_faults(-->check)
"""

from collections import Counter, namedtuple
import numpy as np


def output_matrix(size, clues, matrix):
    """
    This function is used to print the output
    :param size: is the size of the input
    :param clues: is the clues of the matrix
    :param matrix: the matrix itself
    :return:
    """
    print(f'\t     {" ".join(clues[0])}')  # prints the first clue
    print('\t'.expandtabs(8) + '-' * size * 2)  # prints the upper box line
    # Looping with the dimension being the range
    for i in range(size):
        # the below line prints the third line from the input file and prints it vertically
        print('\t'.expandtabs(6) + clues[3][i] + '|', end=' ')
        print(f'{" ".join(matrix[i])}', end=' ')  # prints the matrix row by row
        # prints the clue from the input file and prints it vertically and adds a line
        print('|' + clues[1][i])
    print('\t'.expandtabs(8) + '-' * size * 2)  # prints the lower box line
    # the below line prints the clue from the input file and prints it horizontally
    print(f'\t     {" ".join(clues[2])}')


def duplicate(size, matrix, dimension):
    """
    This function checks for the duplicate value in the matrix
    :param size: is the size of the input
    :param matrix: is the buildings
    :param dimension: is the dimensions of the matrix
    :return:
    """
    dup_flag = 0
    for i in range(size):
        # joins all elements from the matrix using empty space
        # counter keeps track of repeated numbers
        freq = dict(Counter(''.join(matrix[i])))
        if len(freq) != size:
            # j is the keys which will hold the value(ex: 1312)
            vals = [j for j in freq if freq[j] > 1]
            print(f'{dimension} {i}, value {vals}')  # prints the missing value
            dup_flag = 1  # setting flag to 1
    return dup_flag


def puzzle():
    """
    This function is the main chunk of the program
    :return:
    """
    # Named tuple
    data = namedtuple('input', ['dim', 'clues', 'matrix'])
    # empty list
    lst = []
    data.dim = 0
    with open(f'C:\\Users\suraj\PycharmProjects\Skyscrapers\data\puzzle_11.txt') as file:
        for line in file:
            line = line.strip()
            if line == '':
                break
            if data.dim == 0:
                data.dim = int(line.strip())  # gets first line
            else:
                lst.append(tuple(line[::2]))  # appends all lines
            data.clues = lst[:4]
            data.matrix = np.array(lst[4:])  # crating an array so to check for tranpose later

        output_matrix(data.dim, data.clues, data.matrix)  # to print
        # checks if value is from 1 to dimension
        # data.matrix.reshape(data.dim * data.dim, ) rearranges the lists to one list and iterates it as one list
        # if int(i) not in range(1, data.dim + 1) checks if values is in range, else then append to check
        check = [i for i in data.matrix.reshape(data.dim * data.dim, ) if int(i) not in range(1, data.dim + 1)]

        # condition to check if matrix is in range or not
        if len(check) != 0:
            print(f'{check} in matrix. Out of range')
            print('Invalid input')
            return

        flag = []  # empty list
        flag.append(duplicate(data.dim, data.matrix, 'Row'))  # if duplicate found return 1 or else 0
        flag.append(duplicate(data.dim, data.matrix.T, 'Column'))

        # checks if 1 in flag if present return and does not check any further
        if 1 in flag:
            print('Invalid input')
            return

        building_faults(data.dim, data.matrix, data.clues)


def building_faults(dim, matrix, clues):
    """
    building_faults checks for the visibility and if the puzzle is valid
    :param dim: is the dimension of the matrix
    :param matrix: is the matrix itself
    :param clues: clues is the outer values
    :return: flag
    """
    west_check = [[int(i) for i in j] for j in matrix]  # creating a new matrix for checking west visibility
    north_check = []
    # converting matrix to one list
    matrix = matrix.reshape(dim * dim, )
    for i in range(dim):
        # converting the matrix to desired form to check north and south
        # and, i specifies the start and :: end index
        # we are going to taking all the values from start index to the end index
        # Example--1:2:3, index1 to index n-1 takes the first index to be 1 and last index to n-1 which is 2
        # skips to the value of the dimension by taking the value of it
        # Suppose if dimension is 4 then it skips by four to right and this is constant for the specified dimension
        north_check.append([int(j) for j in matrix[i::dim]])

    def check(matrix, clues, dim, direction):
        """
        Check function checks for the visibility
        :param matrix: the matrix with the values
        :param clues:  is the outer values which enclose the matrix
        :param dim:   is the dimensions of the matrix
        :param direction: is the way to which the clues is facing
        :return:
        """
        # checks the visibility
        flag = 0
        for i in range(dim):
            # taking line by line
            block = matrix[i]
            visibility = int(clues[i])  # converting string to int
            count = 0  # to count the visibility
            max = 0
            for j in block:
                # if number in one block is greater than max then one is visible
                if int(j) > max:
                    count += 1
                    max = int(j)
            # checking if count is same or not
            if count != visibility:
                # if it is wrong then printing the wrong row and the direction
                print(f'Error in row {i} when looking from {direction}')
                flag = 1
        return flag

    # initializing a flag to check if the clues are in valid
    building_flag = []
    # Check for north and west initially and then reversing it cause north is top to bottom and south is the opposite of
    # north. Similarly for west and east
    building_flag.append(check(north_check, clues[0], dim, 'North'))  # checking the visibility for north
    building_flag.append(
        check([i[::-1] for i in west_check], clues[1], dim, 'East'))  # reversing west and checking the visibility
    building_flag.append(
        check([i[::-1] for i in north_check], clues[2], dim, 'South'))  # reversing north and checking the visibility
    building_flag.append(check(west_check, clues[3], dim, 'West'))  # checking the visibility for west

    if 1 in building_flag:
        # if the above condition satisfies then the following is printed
        print('Invalid input')
        print('Puzzle not solved')


def main():
    """
    The main method
    :return:
    """
    puzzle()
    print('-' * 30)


if __name__ == "__main__":
    main()
