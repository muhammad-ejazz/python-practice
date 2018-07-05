# Define a recursive procedure is_palindrome, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?

def is_palindrome(s):
    if s == '':
        return  True
    if s[0] != s[-1]:
        return False
    if s[0] == s[-1]:
        new_str = s[1:len(s)-1]
        return is_palindrome(new_str)

print (is_palindrome(''))
# >>> True
print(is_palindrome('abab'))
# >>> False
print(is_palindrome('abba'))
# >>> True