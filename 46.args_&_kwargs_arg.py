'''
Arbitrary / variable length (A)
        args means Positional Arbitrary
        kwargs means Keyword Arbitrary

main key words are 
    Position Arbitrary  *args 
    Keyword Arbitrary   **kwargs
'''

# Example of *args 
# NOTE: in *args is *numbers it is considered as tuples

def sum(*numbers):
    
    print(numbers) # It will print a tuple list passes
    
    c=0
    for i in numbers:
        c+=i
    print(f'The sum is {c}')
    
sum(1,2,3,4)

sum(15,16.98,12.12,70)



# Consider the following example 

def add(*num, name):
    c=0
    print(num)
    print(name)
    
    for i in num:
        c+= i
    print(f'The sum = {c}')

add(3, 4, name = 'Juma')



# Consider also the following example 
# (other variable with *args)
# Here by default a will take 3 and the rest tu *num

def add(a, *num):
    c=0
    print(num)      # (4, 5, 6)
    print(a)        # 3
    
    for i in num:
        c+= i
    print(f'The sum = {c}')

add(3, 4, 5, 6)

















'''
kwargs arguments
'''
def info_person(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

info_person(name='Samwel', age=24, dept='Computer Science')

info_person(name='Neema', age=22, dept='Surveyor Engineer')





# you can pass *args followed by **kwargs

def info_person(*args,**kwargs):
    for key,value in kwargs.items():
        print(key,value)
    print(*args)

info_person(2, 3, name='Samwel', age=24, dept='Computer Science')

info_person(5, 6, name='Neema', age=22, dept='Surveyor Engineer')




# A program that Multply the numbers (2,3,4,-6,8)

def mult(*numbers):
    c=1
    for i in numbers:
        c*=i
    print(f'The Multiple is {c}')

  
mult(2,3,4,-6,8)