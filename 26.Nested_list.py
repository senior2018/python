""" NESTED LIST """

# LIST INSIDE THE LIST

# Example

number = [2, 4, 8, [3, 9, 1], 7, 5]
#         |  |  |        |    |  |
# index   0  1  2       3     4  5

# That is [3, 9, 1] will be at index 3 in a number list

# i.e 
print(number[3]) # output is [3, 9, 1]

#Now to access each element in the inside list

print(number[3][1]) # output is 9


collection = [['Juma', 'John', 'Amos', 'Jenny'], [15, 30, 25], ['PCB', 'EGM']]

print(collection[0][1]) # Output is John

print(collection[1][2]) # Output is 25

print(collection[2][0]) #Output is PCB


# Supporse I want to add PCM at the index 2 in collection list

collection[2].append('PCM')

print(collection)

collection[1].insert(1,-15)

print(collection[1])

#Supporse I want to remove Jenny in a list

collection[0].remove('Jenny')

print(collection[0])

# Supporse I want to update PCB to CBE

collection[2][0] = 'CBE' 

print(collection[2])