'''
There are four types of argument:
    1. Default
    2. Positional (P)
    3. Keyword (K)
    4. Arbitrary / variable length (A)
            |---A P
            |---K P
            
            
'''

# Positional Argument 
# This follows the order of the arrangement of the arguments
# Parameters takes the value as they are arranged in arguments 

def greet(name, dept):
    print(f'Hello! {name}')
    print(f'Are you at {dept} department?')
    
greet('Samwel', 'Computer Science')









# Keyword argument
# This associate the value with the paraeter name

def add(a, b, c):
    d = a+b
    e = d+c
    print(e)
    
add(a = 9.99, b = 8, c = 5.98)









# Default Arguments
# Here value are being provided at the definition of the function
# cmp is a default argument
def status(names, depat, cmp='CRDB Bank'):
    print(f'Hello {names}')
    print(f'Would you like to be in {depat} department at {cmp} company')
    
status('Samwel', 'Computer Science')

# But the default value can be overrided if the parramenter is defined
# Example below NMB will be printed and not CRDB

def status(names, depat, cmp='CRDB Bank'):
    print(f'Hello {names}')
    print(f'Would you like to be in {depat} department at {cmp} company')
    
status('Samwel', 'Computer Science', 'NMB Bank')

# NOTE: the default adgument should be defined after known argument
# Example:- defining as follows:
# def status(names, cmp='CRDB Bank', depat): will return error 









'''
Arbitrary Position Argument.

* is used to accept arbitrary position arguments

Example:
- Adding a list of uknown numbers
'''

def sum(*numbers):
    c=0
    for i in numbers:
        c+=i
    print(f'The sum is {c}')
    
sum(1,2,3,4)

sum(15,16.98,12.12,70)








