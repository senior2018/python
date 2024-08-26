""" 
WRITE A PROGRAM THAT WILL ALLOW USER TO UPDATE THE LIST
BUY USER TO ENTER THE COLLUMN NUMBER AND DATA TO PLACE 
IT WITH

GIVEN THE LIST 

r1 = ['Q', 'Q', 'Q']
r2 = ['Q', 'Q', 'Q']
r3 = ['Q', 'Q', 'Q']

"""





















r1 = ['Q', 'Q', 'Q']
r2 = ['Q', 'Q', 'Q']
r3 = ['Q', 'Q', 'Q']

my_ls = [r1, r2, r3]


print(my_ls)

pos = input("Enter the position of a list you want to insert a new data\n")

item = input("Enter the data you want to insert\n")

row = int(pos[0]) - 1

col = int(pos[1]) - 1

my_ls[row][col] = item

print(my_ls)