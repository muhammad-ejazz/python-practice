# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.
import string
characters = list(string.ascii_lowercase)

def rotate(string, number):
    new_str = ''
    for ind in range(len(string)):
        if string[ind] != ' ':
            i = characters.index(string[ind])
            i = (i + number) % 26
            new_str += characters[i]
        else:
            new_str += string[ind]
    return new_str

print (rotate ('sarah', 13))
#>>> 'fnenu'
print (rotate('fnenu',13))
#>>> 'sarah'
print (rotate('dave',5))
#>>>'ifaj'
print (rotate('ifaj',-5))
#>>>'dave'
print (rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17))
#>>> ???