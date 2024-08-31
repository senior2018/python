""" 
Write a program to calculate the avarage of the height given by a user

"""

























height = input("enter all height separate by space")

height_list = height.split()
count = 0
for height in height_list:     # The loop to count the total number user entered
    count = count+1
print("There are total number of: ", count)

for i in range(count):     # Converting the number from string to int
    height_list[i] = int(height_list[i])
    
sum = 0
for person in height_list:   # Finding the sum of numbers
    sum += person
print('The total of the number you entered is:',sum)

average = sum/count # Calculating the avarage of numbers

print('The average is:-',average)