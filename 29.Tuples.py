'''
TUMPLES

    -A type of data that a very similar to list.
    
    the main different is that Tulple are immutable
    meaning that they cannot be changed once they are created
    and makes them idle for storing data that should not be modified.
    
'''

# Its declaration 
tuple1 = (12, 6, -8, 'Jenny', True)

# Its printing
print(tuple1)

print(type(tuple1))


# Printing at a certain index
print(tuple1[1])



# Special cases

tuple2 = (10)  # this is normal int 
print(type(tuple2))

tuple3 = (10,)  # this is tuple
print(type(tuple3))




'''NASTED TUPLE'''

tuple4 = (12, 4, -6, 'jenny', True)
tuple5 = (50, "ram", False)

tuple6 = (tuple4, tuple5)

print(len(tuple6))  # it will return 2
print(tuple6)

# But if it is 

tuple7 = tuple4 + tuple5 # combine the two tuples into one tuples

print(type(tuple7)) 

print(tuple7)


# Converting LIST into tuple and vice versa
list_1 = [3, 4, 5, 6, 7, 8]

print(tuple(list_1))