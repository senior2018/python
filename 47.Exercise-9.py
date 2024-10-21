'''
Write a Program to check a number is prime, odd or even.
'''
import math

print("Welcome.")
print('This program is special to check if a number is ODD, EVEN or PRIME')

while True:
    qn = input('Do you want to Try (Y/N)')
    
    if qn == 'N' or qn == 'n':
        print('Thankyou Welcome again to try')
        break
    elif qn == 'Y' or qn =='y':
        num = int(input('Enter a number you want to check'))
        
        if num%num == 1 or num%1 == num:
            print(f'This number {num} is prime number')
        elif num%2 != 0:
            print(f'This {num} is odd')
        else:
            print(f'This {num} is even')
    else:
        print('Invalid Input please enter a valid one.')