# For loop
name = 'Mona'
for i in name:
    print(i) 
    
'''
Output
M
o
n
a
'''

names = ['Mona','Lisa','Braison']

# for i in names:
#     print(i)

'''
Output
Mona
Lisa
Braison
'''

# Indentation is more important thing to remember
for i in names:
    print(i)
    if i=='Mona':
        print('Hey, It\'s me')
        
# Square of each number in a list       
list1 = [2,3,4,5,6]
squares = []
for i in list1:
    square = i**2
    squares.append(square) # Adds the square nummbers and store them in a list
    print(square)
print('The list of square is: ', squares) # Printing the new list