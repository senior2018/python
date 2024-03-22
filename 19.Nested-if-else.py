#Nested If else 

"""
NESTED IF FORMAT

if condition 1:
    statement 1
    if condition 2:

"""

#Nested if example

# print('survey beggin')

# height = int(input('What is your height'))

# if height >= 10:
#     print('You can ride')
#     age = int(input('What is your age\n'))
#     if age >= 18:
#         print('You are allowed to compit\n')
        
# print('Survey completed')




"""
NESTED IF ELSE FORMAT

if condition 1:
    statement 1
    if condition 2:
        condition 2   
    else
        statement 2
else
    statement 1
"""


#if else example

# print('nested if else beggin')

# marks = int(input('What is your average marks\n'))

# if marks >= 50:
#     print('You passed the exams\n')
#     age = int(input('What is your age\n'))
#     if age >= 18:
#         print('Access granted\n')
#     else:
#         print('not enough age')
# else:
#     print('Your didnot pass')
    
# print('nested if else ended')



#If-else condition
#in python insted of using else-if we use ELIF

# print('else if beggin')

# number = int(input('Enter either 1, 2, 3, 4 or 5\n'))

# if number == 1:
#     print('one')
# elif number == 2: #Only this will be executed
#     print('Two')
# elif number == 3:
#     print('Three')
# elif number == 4:
#     print('Four')
# elif number == 5:
#     print('Five') 
# elif number == 2:
#     print('Two')
# else:
#     print('Out of bount')  
    
# print('Else if ended')

#in EF - ELIF after the any condition is true is exit at the point

#Supporse the same program we use only IF statement
#It will check the whole condition regaldless the true condition is found
#Example

print('else if beggin')

number = int(input('Enter either 1, 2, 3, 4 or 5\n'))

if number == 1:
    print('one')
if number == 2:
    print('Two')  #This will be axacuted
if number == 3:
    print('Three')
if number == 4:
    print('Four')
if number == 5:
    print('Five') 
if number == 2:
    print('Two') #And this also
else:
    print('Out of bount')  
    
print('Else if ended')