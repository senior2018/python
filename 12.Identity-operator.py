#Identity operator
#Include is and is not
#They are used to compare the object (memory adress, object id) and that they share the same location

a = 5
b = 5

#Short hint
# in python the memory manager stores 5 as one object and both a and b can access the object
# that is#

print (a is b)

#Returt true because 5 is a single object created and can be accessed by a and b#


#NOTE
#is compares the location and ID 
#while
#== compares the values


#To check the ID of object
print(id(5))
print(id(a))
print(id(b))



#BUT
x = 3
y = '3'

print(x is y) 
#return false because 3 and '3 are not the same data type 
#then two different object have been created with different location

print(id(x))
print(id(y))

#For is not

print(a is not b) # return false

print(x is not y) # return true 

c = 5 
d = 6
print(id(5))
print(id(c))
print(id(6))
print(id(d))