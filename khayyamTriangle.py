# Double Gold Star

# Khayyam Triangle

# The French mathematician, Blaise Pascal, who built a mechanical computer in
# the 17th century, studied a pattern of numbers now commonly known in parts of
# the world as Pascal's Triangle (it was also previously studied by many Indian,
# Chinese, and Persian mathematicians, and is known by different names in other
# parts of the world).

# The pattern is shown below:

#                    1
#                   1 1
#                  1 2 1
#                 1 3 3 1
#                1 4 6 4 1
#                   ...

# Each number is the sum of the number above it to the left and the number above
# it to the right (any missing numbers are counted as 0).

# Define a procedure, triangle(n), that takes a number n as its input, and
# returns a list of the first n rows in the triangle. Each element of the
# returned list should be a list of the numbers at the corresponding row in the
# triangle.

def pascal(n):
    if n == 1:
        return [1]
    else:
        p_line = pascal(n - 1)
        line = [p_line[i] + p_line[i + 1] for i in range(len(p_line) - 1)]
        line.insert(0, 1)
        line.append(1)
    return line

def triangle(n):
    if n == 0:
        return []
    else:
        line = []
        for i in range(1, n+1):
            line.append(pascal(i))
        return line

#For example:

print (triangle(0))
#>>> []

print (triangle(1))
#>>> [[1]]

print (triangle(2))
#>> [[1], [1, 1]]

print (triangle(3))
#>>> [[1], [1, 1], [1, 2, 1]]

print (triangle(6))
#>>> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]