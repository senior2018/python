#if else statement
#In is else statement indentation is used in identify the block to be executed

#syntax is as follows
"""
if (condition):
    do this 
    You can add more than one block but should be indent format 
else:
    do this
"""

#Condition can be expresses using
#<=, <, ==, !=, >, >=

age = int(input('What is your age'))

if(age >= 18):
    print('You can vote')
else:
    print('You cant vote')
    
    
#NOTE
#Any block within if else statement should be indent format or else it is an error
#example the below code gives error

    """
    if(age >= 18):
        print('You can vote')
    print('go and vote')
    else:
        print('You cant vote')
        
        OR
        
        
    if(age >= 18):
    print('You can vote')
    else:
    print('You cant vote')
    """
    
#IF code without Else 
#If block can be executed is true
#and if false block outside the if can be executed if there is
#else it just execute the program

height = 15 

if(height <= 10):
    print('You are tall enough')
print('Yes hello')      #this code will be executed weather the if statement is true or false



#IF statement can also be written as
if height == 13:
    print('The height is good')
    print('Go and jump') #this code will be executed only if if statement is true
else:
    print('No enough height')