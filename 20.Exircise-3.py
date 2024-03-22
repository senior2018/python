"""
QUESTION
Write a program to check whether given year is leap or not

Hint of a leap year
i. Divisible by 4 ->leap year
ii. it should NOT be divisible by 100 -> leap year
iii. If divisible by 100, it should be divisible by 400

"""

year = int(input('Which year you want to check\n'))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('leap year 1')
        else:
            print('Not a leap year 1')
    else:
        print('leap year 2')
else:
    print('Not a leap year 2')