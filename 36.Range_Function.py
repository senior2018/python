''' 
RANGE() FUNCTION

Returns a sequence of number, starting from 0 by defaut and 
increaments by 1 (by default), and stops before a specified number

'''

a = range(5)

print(a[1]) # the output is 1
print(a[0]) # The output is 0

b = range(2,5)
print(b[0]) #the first number will be printed which is 2

#To print it continously we use for loop

c = range(2, 12)

for i in c:
    print(i) # It will print from 2 to 11
    
c = range(2, 12, 2)

for i in c:
    print(i) # It will print from 2 to 11 but while skipping two steps in each(2, 4, 6, 8, 10)
    
d = range(10,0,-2)

for i in d:
    print(i) # it will print from 10 to 0 while skipping two steps(10, 8, 6, 4, 2)
    
    
e = range(-1, -10,-2)

for i in e:
    print(i) # Output is -1, -3, -5, -7, -9
    
    
    
''' 
SIMPLE TASK
 
Find the sum of numbers from 0 to 100
'''

total = 0

for i in range(0,101):
    total += i
print(total)





''' 
Simple task 2

Find the sum of all even number from 0 to 100

'''

even = 0

for i in range(2, 101):
    even += i
print(even)