#ARTHMETIC OPERATION
#include +, -, *, ? %

# Difference between / and // 

#when / is used it return a float number

print(72/25)
# Return 2.88

print(-72/25)
# Return -2.88

#when // is used it return an int number it round it to downward for positive number and upward for negative number

print(72//25) 
# return 2 

print(-72//25) 
# return -3 

# power is obtained by ** 

print(3**3)

#Multiple operators it follows the BODMAS rule automatic

print(3 + 2 * 6 // 3)

#Priority of the operators
                #   ()               P (prentesis)
#   R -> L       #   **              E (Exponent)
#   L -> R       #   *, /, //, %     M D (multiplication & Division)
#   L -> R       #   +, -            A S (Addition & Substraction)
    

# Example in equation bellow
sam = 5 + 2 * 3 - 1 + 10/5

print(sam)

# From priority above multiplication will start followed by division, sub then add
