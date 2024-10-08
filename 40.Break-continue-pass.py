'''
Break statement

terminate the loop at a certain condition

'''
# NESTED FOR LOOP"

list1 = ['Hi', 'Hello', 'Welcome']
names = ['Krishn', 'Ram', 'Madhav']

for item in list1:
    for name in names:
        print(item,name)
        if item=='Hello' and name=='Ram': # when this condition is reached it will skip and shift to the next item
            break
    print('Out of inner loop')
print('Out of outer loop')
  
  
  
'''
CONTINUE

Means continue with the next iteration
'''

count=1

while count<=10:
    print(count)
    count+=1
    if count == 7: # When this statement is reached Hi will be skipped
        continue
    print('Hi')
print('Out of loop') 






for i in range(1,11):
    if i == 7:          # 7 will be skipped
        continue 
    else:
        print(i)
        
        
        
'''
PASS 

means do nothing, used as a placeholder for future code.

When the pass statement is executed, nothing happens, 
but you avoid getting an error when empty code is not allowed.
'''

for i in range(0,11):
    pass