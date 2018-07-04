# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.
import string
characters = string.ascii_lowercase
strings = []
for i in range(len(characters)):
    strings.append(characters[i])

def shift_n_letters(letter, n):
    # Your code here
    i = strings.index(letter)
    i = (i + n) % 26
    return strings[i]

print (shift_n_letters('s', 1))
#>>> t
print (shift_n_letters('s', 2))
#>>> u
print (shift_n_letters('s', 10))
#>>> c
print (shift_n_letters('s', -10))
#>>> i