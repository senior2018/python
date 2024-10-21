'''
FUnctuin with argument means:-

passing a variable while creating 
a function and when calling a function calling

i.e 
def greet(Parameter):
    print()
    print()
    
greet(argument or actual parameter)
'''

def greet(name):
    print(f'Hello {name}')
    print('Welcome to NIT for bachelor in Computer science')
    
greet('Samwel')

# You can call it several time with different argument

greet('Yvone')
greet('Yusuph')



# Function to add two number

def add(a, b):
    c=a+b
    print(c)
    
add(10, 8)

# NOTE: the number of parameter you pass should be he same to number of arguments

# add(10) # This will return error