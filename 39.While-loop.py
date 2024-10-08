'''
WHILE LOOP 

execute the loop untill the given condition is true.

WHILE LOOP with ELSE

else block will be executed when while loop is false

WHILE is used when you dont know how many times the program to print
'''

count = 1

while count <= 5:
    print(count)
    count +=1 
print('Out of loop')

while count > 0:
    print(count)
    count -= 1
print("Out of loop")


# While loop with else
counts = 5

while counts>0:
    print(counts)
    counts -=1
else:
    print('This is else block')
    
print('Out of loop')




# Else block will not be printed

number = 5

while number>0:
    print(number)
    number -=1
    if number == 3:
        break
else:
    print('This is else block')
    
print('Out of loop')



# A program to find the total n number

total = 0
numbers = int(input("Enter a number (form o to quit):"))
while numbers !=0:
    total += numbers
    numbers = int(input("Enter a number (form o to quit):"))
print('The total is', total)