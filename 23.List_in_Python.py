# LIST is a collection of multiple data types

#Example:
# Collection of collection of multimple simmilar data type
# int type
enrole = [1, 2, 3, 4, 5]

#string type
name = ['John', 'Mosses', 'Antony', 'Light']

# But also can  be collection of multiple diffetent data type
# Int and float
details = [1, 'John', 2.34]



""" CREATING A LIST FROM USER INPUT USE SPLIT FUNCTION """
                 
# name = input("Enter five different data")
# namesp = name.split(" ")  # It means that wherever there is space it will be cutoff as one element in a list

# print(namesp) 


# # ALSO
# sub = input("Enter any data you wish to store in a list by separating them with coma(,) ")
# sub_sp = sub.split(",")    # when ever there is comma data will be considered as one element

# print(sub_sp)



# PRINTING THE LIST
# ACCESSING THE ELEMENT IN A LIST IS USING INDEX NUMBERS

# EXAMPLE

# index   0   1   2    3    4
#         |   |   |    |    |
marks = [20, 40, 80, 55.5, 23]

#but also index can be as follows
#         -5  -4  -3   -2   -1
#         |   |   |    |    |
marks = [20, 40, 80, 55.5, 23]

#Printing the whole list

print(marks)   # output is [20, 40, 80, 55.5, 23]

# Printing a single element

print(marks[1]) # output is 40

# Supporse if we use neg index it print in backward ways

print(marks[-1]) # output is 23




# SUPPORSE we print only some of element

height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(height[1:5]) #output will be [2, 3, 4, 5]

# It means 1 === index number and 5 === column number
# Starting from index 1 and taking all number upto column 5 or 
# also 5 act as a lengh of element is a list starting from the beggining

#if 

print(height[3:]) # output is [4, 5, 6, 7, 8, 9, 0]







#SUPPORSE  we print 

num = [12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

print(num[1:7:4]) # output will be [14, 22]

# It means that 1 stand for index number
# 7 stand for column number starting from the beggining(at index 0)
# Number of steps ( from above count start at index 1)




# Supporse we need to SORT the list 

mix = [4, 23, 4, -5, 67, -43, 43, 0, -1]

mix.sort()

print(mix) # Output will be [-43, -5, -1, 0, 4, 4, 23, 43, 67]




# Supporse we need to REVERSE the list 

arry = [4, 23, 4, -5, 67, -43, 43, 0, -1]

arry.reverse()

print(arry) # Output will be [-1, 0, 43, -43, 67, -5, 4, 23, 4]



# Printing min and max from the list

number = [2, 87, -93, 6, 24, -6]

print(max(number)) #output will be 87

print(min(number)) #output will be -93



# ADDING ONE ELEMENT AT A TIME

number.append(45)
print(number)

# ADDING ELEMENT AT A CERTAIN INDEX

number.insert(2, 55) #Add 55 at index 2
print(number)


# ADDING MULTIPLE DATA AT A TIME
number.extend([34, 20, 30,60]) #will be added at the end of the list
print(number)

# UPDATING AN ELEMENT IN A LIST
number[0] = 100 # will replace 2 with 100
print(number)

#UPDATING MULTIPLE ELEMENT
number[3:7:3] = [93, 6] # will replace -93 and -6 with 93 and 6
print(number)

#REMOVING ITEM FROM THE LIST
number.remove(6) #it will remove the first 6 from the list
print(number)

#REMOVING THE LAST ELEMENT FROM THE LIST
number.pop() #it will remove 60 from the list
print(number)

print(number.pop()) # it will return the removed element at this time will be 30

#REMOVING AT A CERTAIN INDEX
print(number.pop(2)) # 55 will be removed and printed


# CLEARING OR REMOVING ALL FROM THE LIST
# number.clear()

# RETURNING A SHALLOW COPY OF THE LIST
# number.copy

# RETURN THE NUMBER OF APPEARANCE OF ITEM IN A LIST
print(number.count(6))