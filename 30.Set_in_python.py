''''
SET:
    - are used to store multiple multiple items in a single variables
    
    - Is a collection which is unordered, unchangable and unindexed
    
    - Set items are unchangable, but you can remove items and add new ones
    
    - Does not allow duplicate of items
    
    - On printing set, the element of set are automatic arranged inorder no matter how you re-arrange
    
    - On printing we do not use index becaue they are not arrangement in order

'''

# Example

set1 = {7, 3, 9, 5, 6, 7}

set2 = {9, 'John', True, -0.56}

print(set2)


# True and 1 are considered as same value
# So the starting value will be printed

set3 = {10, 4, -6, 1, 'John', True}

print(set3)





# Similar to False and 0 are considered as same value
# For duplicate values, only one value will be printed
set4 = {False, 19, 5, -9, 0, 'Aman', 9}

print(set4)


# Adding into a set
set4.add(99)

print(set4)

set4.add((67, 68, 69)) # add a tuple in a set but list id not allowed
print(set4)


#Removing a file
set4.remove(False)

print(set4)

# Discard can also be used to remove
# But the different from remove is that if the element is not there it does not return an error while remove return an error

set4.discard(77)

print(set4) # Set 4 will be printed with no error

# But if 
# set4.remove(77) # this will give an error


print(set4.pop()) #remove the last item in a set and return it


# To create an empty set use SET methot
# i.e 
set_2 = {} # this is not a set
print(type(set_2))


set5 = set() # this is an empty set
print(type(set5))



