# F-string
# A new format for strings#

#For-instance you want to print
name = 'Sammie'
age = 30
height = 6.6

#print('my name is ' + name + 'I am ' + age + 'years old') 

#the above statement provide an error due to different variable types
#to solve such kind of error We do as follows

#using typecasting method
print('My name is ' + name + ' I am ' + str(age) + ' Years old')

#Or using , sign
print('My name is ', name, 'I am ', age, 'Years old. My height is ', height)

#Now What if you have different multiple of vatiables is where F-string is applied
#You just apply as follows
print(f'My name is {name} I am {age} Years old. My height is {height} meters')

#You can also place an expression inside {}
print(f'My name is {name} I am {age-6} Years old. My height is {height} meters')

