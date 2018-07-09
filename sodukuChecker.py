# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]

incorrect = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 4],
              [4, 1, 2, 3],
              [3, 4, 1, 2]]

incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]

incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]

matrix6 = [[1, 1.5, 3], [3, 1, 1.5], [1.5, 3, 1]]


def maxi(matrix):
    maximum = float('-inf')
    for row in matrix:
        maximum = max(maximum, max(row))
    return maximum


def mini(matrix):
    minimum = float('inf')
    for row in matrix:
        minimum = min(minimum, min(row))
    return minimum


def check_sudoku(matrix):

    matrix1 = []
    for i in range(len(matrix)):
        line1 = []
        for j in range(len(matrix[i])):
            if not str.isdigit(str(matrix[i][j])):
                return False
            if not float.is_integer(float(matrix[i][j])):
                return False
            line1.append(matrix[j][i])
        matrix1.append(line1)

    maximum = maxi(matrix)
    minimum = mini(matrix)
    numbers = range(minimum, maximum+1)

    for row in matrix:
        counter_dictionary = {number: 0 for number in numbers}
        for value in row:
            counter_dictionary[value] += 1
        for count in counter_dictionary.values():
            if count == 0 or count > 1:
                return False

    for row in matrix1:
        counter_dictionary = {number: 0 for number in numbers}
        for value in row:
            counter_dictionary[value] += 1
        for count in counter_dictionary.values():
            if count == 0 or count > 1:
                return False
    return True

print (check_sudoku(incorrect))
# >>> False

print(check_sudoku(correct))
# >>> True

print(check_sudoku(incorrect2))
# >>> False

print(check_sudoku(incorrect3))
# >>> False

print(check_sudoku(incorrect4))
# >>> False

print(check_sudoku(incorrect5))
# >>> False

print(check_sudoku(matrix6))
# >>> False
