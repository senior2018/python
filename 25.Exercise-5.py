""" 
QUESTION 
WAP which will select a random name from a list name  & 
the person will have to pay for everybody's bill

"""









import random

''' Responce 1 '''

# a = input("enter any five name five name separate them with space")

# asp = a.split(" ")

# x = random.choice(asp)

# print(x)








''' responce 2 '''


b = ['John', 'Antony', 'Michael', 'Juma']

length = len(b)

y = random.randint(0,length-1)

print(b[y])

# or

print(f'{b[y]}')