'''
PASSWORD CREATOR PROGRAM

Example the output should be:

welcome to password generator!
How many letter would you like in your password?
4
How many symbols would you like?
3
How many numbers would you like?
2

9eSn)n*&9


'''
import random

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
          'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
          'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 
          'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
          'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

sysmbol = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*',
           '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?',
           '@', '[', '\\', ']', '^', '_', '{', '|', '}', '~']


number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print('Welcome to password generator!')

n_letter = int(input('How many letters you want in your password?\n'))

n_sysmbol = int(input('How many sysmbols you want in your password?\n'))

n_number = int(input('How many numbers you want in your password?\n'))






password = []                         # Purpose is to store the selected character   

for i in range(1, n_letter + 1 ):
    char = random.choice(letter)
    password += char                 #  the selected letters will be stored to password list
    
for i in range(1, n_sysmbol + 1):
    char = random.choice(sysmbol)
    password += char                #  the selected sysmbol will be stored to password list
    
for i in range(1, n_number + 1):
    char = random.choice(number)
    password += char                #  the selected number will be stored to password list

random.shuffle(password)            # Shuffle the list 

p = ""                              # purpose is to store the character from the list

for i in password:
    p += i
print(p)                            # Printing the list now


























'''
For more advanced
'''

"""
import random
import string

def generate_password(num_letters, num_symbols, num_numbers):
    # Generate random letters
    letters = random.choices(string.ascii_letters, k=num_letters)
    
    # Generate random symbols
    symbols = random.choices(string.punctuation, k=num_symbols)
    
    # Generate random numbers
    numbers = random.choices(string.digits, k=num_numbers)
    
    # Combine all parts
    password_list = letters + symbols + numbers
    
    # Shuffle the combined list to ensure randomness
    random.shuffle(password_list)
    
    # Convert list to string
    password = ''.join(password_list)
    
    return password

def main():
    print("Welcome to the password generator!")
    
    num_letters = int(input("How many letters would you like in your password? "))
    num_symbols = int(input("How many symbols would you like? "))
    num_numbers = int(input("How many numbers would you like? "))
    
    password = generate_password(num_letters, num_symbols, num_numbers)
    
    print("\nYour generated password is:")
    print(password)

if __name__ == "__main__":
    main()"""