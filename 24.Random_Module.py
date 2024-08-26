# RANDOM MODULE - is use to generate sudo random numbers
# FIRST WE NEED TO IMPORT RANDOM FUNCTIONS.

import random

# SOME DIFFERENT RANDOM FUNCTION

a = random.randint(1,4)   #this will return random int number from 1 to 4  
# print(a)

b = random.randrange(1,4) # This will print random int between 1 to 3, 4 will not be included
# print(b)

c = random.random() # this will print random float number i.e 0.
# print(c)

d = random.uniform(1,3) # This will give you float number between 1 and 3
# print(d)

# Printing a random number from a list
l = [2, 4, 20, -6, -4, 7, 9, 14, 5, -2]
e = random.choice(l)
# print(e)

# Printing a random arrandement of item in a list 
l = [2, 4, 20, -6, -4, 7, 9, 14, 5, -2]
random.shuffle(l)
print(l)
 