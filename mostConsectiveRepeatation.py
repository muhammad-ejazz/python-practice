# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a
# list, and returns the element in the list that has the most
# consecutive repetitions. If there are multiple elements that
# have the same number of longest repetitions, the result should
# be the one that appears first. If the input list is empty,
# it should return None.

def longest_repetition(li):
    # Your code here
    max_count = -1
    count = 0
    number = None
    for i in range(len(li)-1):
        if li[i] == li[i+1]:
            count = count + 1
        else:
            if count > max_count:
                max_count = count
                number = li[i]
            count = 0
    if count > 0:
        number = li[0]
    return number


#For example,

print (longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1]))
# 3

print (longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd']))
# b

print (longest_repetition([1,2,3,4,5]))
# 1

print (longest_repetition([4, 4, 4, 4, 4]))
# None
