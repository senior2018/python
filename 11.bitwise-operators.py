#Bitwise operator
#They work in bitwise form
#include & (and), | (or), ^(XOR), ~ (not) 
#<< (left shift), >> (Right shift)

#Example
a = 5
b = 6

#It first convert 5 and 6 into bit and then perform and operation
#Similar to that logic operations

print(a & b)

print(a | b)

print(a ^ b)

#for ~ (not) 
#it convert the number into bit 
#then it reverse the bit
#then change the reversed bit to decimal number

print(~a)

#In simple way 
# ~a = -(a + 1)

#for << 

print(a<<2)

#convert a = 5 into bit == 0101
#left shift two means add zeros behind the bit withought arteling the behind
#that is 0101 == 010100
#We do not discard the bit ie we gain bits
#then convert 010100 to decimal  

#A simple formula for left shift 
# x << n === x * 2^n


#for >>

print(a>>2)

#convert a = 5 into bit == 0101
#Then remove the last two bit
#that is 0101 == 01
#We do discard the bit ie we lose bit
#then convert 01 to decimal  

#A simple formula for left shift 
# x >> n === x / 2^n




#Quize
#What is the output 
# 26 $ 23
# 17 | 24
# 17 ^ 24
# ~45
# 68 << 2
# 56 >> 3#
