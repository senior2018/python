# Round function
# its Syntax ROUND(number, no-of-digits)#

print(round(7))  #It wil return 7

print(round(7, 2))  #It will return 7 because it is an int value

print(round(7.61))  #it will return 8 because rounding a number without specifying no of digit it change float number to int

print(round(2.66667, 2)) # Iit will return 2.67

print(round(2.6657, 0)) # It will return 3.0

print(round(2.489, 0)) #It will return 2.0


#Special casses
#Example for 7.5, 8.5, 6.5
#It will round to the nearest even number


print(round(7.5)) #it will return 8

print(round(6.5)) #it will return 6

print(round(2.5)) #it will return 2


#For int values

print(round(674, 2))  #It return 674

print(round(674, -1)) #It will return 670

print(round(8787, -2)) #it will return 8800

print(round(765, -3))  #It will return 1000

print(round(345, -3))  #It will return 0

print(round(665, -1))  #it will terurn 660

#NOTE
#When round up a even number having only 5 or 5 with zero next digits to it, it round to nearest even number

#Example
print(round(6501, -3))  #it will return 7000

print(round(6500, -3))  #it will return 6000

print(round(665, -1))  #it will return 660



#Special cases
print(round(674.1012, -1))  #it will return 670.0