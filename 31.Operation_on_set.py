'''
SOME OPPERATION OF SET ARE

union():
        - Return a set containing the union of sets
        
        - Its corespondent sysmbol |
        
update():
        - 	Update the set with the union of this set and others
        
        - Its corespondent sysmbol |=

intersection()
        - Returns a set, that is the intersection of two other sets
        
        - Its corespondent sysmbol &

intersection_update()
        - Removes the items in this set that are not present in other, specified set(s)
        
        - Its corespondent sysmbol &=

isdisjoint():
        - returns True if none of the items are present in both sets, 
          otherwise it returns False.

issubset():
        - seta is a SUBSET of setb if every element of seta is in setb
        
        - Returns whether another set contains this set or not
        
        - Its corespondand symbol is <=

issuperset():
        - It is opposite of SUBSET
        
        - Returns whether this set contains another set or not
        
        - Its corespondand symbol is >= 
        

add():
        - Adds an element to the set
        
clear():
        - Removes all the elements from the set

copy():
        - Returns a copy of the set
        
pop():
        - Removes an element from the set

remove():
        - Removes the specified element      

difference():
        - Returns a set containing the difference between two or more sets
        
        - Its corespondent sysmbol -

difference_update():
        - Removes the items in this set that are also included in another, specified set
        
        - Its corespondent sysmbol -=

discard()
        - Remove the specified item
        
symmetric_difference():
        - Returns a set with the symmetric differences of two sets
        
        - Its corespondent sysmbol ^

symmetric_difference_update():
        - Inserts the symmetric differences from this set and another
        
        - Its corespondent sysmbol ^=
'''

set1 = {'Samwel', 'Paul', 'Juma', 'John'}

set2 = {'Aman', 'Juma', 'Nely', 'Martha'}

'''UNION (|)'''
# print(set1.union(set2))

# print(set2.union(set1))

# print(set1 | set2)

# # Union set with other element

# print(set1.union(("Maah", 'Joshua')))



'''Update operation'''

# set1.update(set2) # Takes all the set 2 element and add them to set 1

# Can use also the symbol |=
# set1 |= set2

# print(set1)

# set1.update(['Maiko', 'Peace']) # Convert the list into a set and add the element in set 1

# print(set1)







''' INTERSECTION OPERATOR (&)'''

# print(set1.intersection(set2))

# print(set1 & set2)

# print(set1.intersection(("Maah", 'Joshua'))) # i will return an empty set





'''DIFFERENCE IN SET
the item that are in set1 but not in set 2'''

seta = {'Ram', 'Shyam', 'Jenny'}
setb = {'Jenny', 'Jiha', 'Aksan'}
setc = {'Ankuh', 'Pradeep', 'Ram'}

# print(seta.difference(setb)) 
# # Gives the item that are in seta but not in setb

# Using an operator
# print(seta - setb)   

# print(seta.difference(("tom", "groves"))) 

# seta.difference_update(setb) # Remove the intersection element from seta

# print(seta)




''' SYMMETRIC_DIFFERENCE
combine all the element of seta and setb except the intersection element and set then as seta'''

# print(seta.symmetric_difference(setb)) # does not allow multiple argument

# # Using symbol

# print(seta ^ setb ^ setc) # can allow multiple arguments

# seta.symmetric_difference_update(setb) # combine all the element of seta and setb except the intersection element and set then as seta

# print(seta)

'''
DISJOINT & ISSUBSET
'''
set_a = {1, 3, 4, 5, 6}
set_b = {2, 7, 8, 9, 10}
set_c = {3, 4, 5, 6}

# # isdisjoint check in either element is in both set

# print(set_a.isdisjoint(set_b)) # it will return True

# print(set_a.isdisjoint(set_c)) # it will return False

# print(set_a.isdisjoint(['Mosess', 'Kill'])) # It will return True

# print(set_a.isdisjoint(['Mosess', 4])) # It will return False




# # issubset

# print(set_a.issubset(set_b))    # Check if all set_a element are in set_b
#                                 # Return False

# print(set_c.issubset(set_a))    # it will return True

# print(set_a.issubset((2, 7, 8, 9, 10))) # it will return false

# print(set_b.issubset((2, 7, 8, 9, 10))) # it will return True





# #issuperset
# print(set_a.issuperset(set_c))  #  Check if all set_a contain all element of set_b 
#                                 # it will return True

# print(set_c.issuperset(set_a)) # it will return Farse

# print(set_a.issuperset((2, 7, 8, 9, 10))) # it will return false

# print(set_b.issuperset((8, 9, 10))) # it will return True


'''
Clearing & Deleting set
'''
# # deleting only elements

# set_d = {30, 40, 60}

# set_d.clear() # it delete all the element of the set

# print(set_d) # An empty set will be printed



# # deleting a whole set

# set_e = {45, 55, 65}

# del set_e

# print(set_e)  # It will return error "set_e is not defined"