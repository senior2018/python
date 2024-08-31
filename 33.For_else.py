""" 
In for else loop,

Else block will be printed only if the for block is printed succesfull
it will not be printed is there is any error
"""

numbers = [2, 3, 4, 5, 6, 7]

for i in numbers:
    print(i)
else:
    print("The loop is successfull printed.")
    

# Wherever there is brak statement else block will no be excecuted
nums = [10, 20, 30, 40, 50]

for i in nums:
    print(i)
    if i == 30:
        break
else:
    print('The loop is finished.') # It will not be printed
    
    
    
# More example
marks = (2, 7, 8, 13, 15, 26, 9)

for i in marks:
    if i%2 == 0:
        print(i, ' is dvisible by 2.')
    else:
        print(i, ' is not divisible by 2.')
else:
    print('The end of the loop')