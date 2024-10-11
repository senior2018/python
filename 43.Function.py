'''
FUNCTION

- Is a block of code which only run when it is called.
- You can pass data known as parameters, into a funcion
- A function can data as a result

'''

# Dfinition of a fncion

def greet():
    print('Hi!')
    print('Samwel')
    
    
    
# Calling a function

greet()

# Can be called as many time as you want

greet()
greet()
greet()



for i in range(1, 12):
    if i == 2:
        for j in range(1, 3):
            print(f'i2 {i}')
            continue
    if i == 5 or i == 7:
        print(f'i3 {i}')
        continue 
    if i == 11:
        print(f'i4 {i}')
        continue
    print(f'i1 {i}')
    