"""
    Write a simple program called Pizza order program that
    calculate the total bill when customer places the order 
     
    Small piza = 100
    Medium piza = 200
    Large piza = 300
    
    pepperoni for small Pizza =30
    pepperoni for medium or large Piza = 50
    
    extra cheese for any size Pizza = 20
"""















# Responce 1




choice = input("Do You want Pizza(Y/N)? ")


if choice == 'Y' or choice == 'y':
    
    size = input("What size of Pizze Do you want(S/M/L)? ")
    if size == 'S' or size == 's':
        bill = 100            
    elif size == 'M' or size == 'm':
        bill = 200
    elif size == 'L' or size =='l':
        bill = 300
    else:
        print("Incorect choice. Try again. ")
        
    addition = input("Do you need Pepperoni?")
    if size == 'S' or size == 's':
        bill += 30
    else:
        bill += 50
    
    extra = input("Do you need extra cheese(Y/N)? ")
    if extra == 'Y' or extra == 'y':
        bill += 20
        print(f"Your bill is {bill} we will prepare it for you")
    else:
        print(f"Your bill is {bill}, we will prepare it for you")
        
elif choice == 'N' or choice == 'n':
     print("Thank you, and Welcome again. ")

else:
    print("Incorect choice. Try again. ")
    
    
    
    
    
    
# Responce 2



size = input("What size pizza you want(S/M/L)? ")
bill = 0
if size == 'S' or size == 's':
    bill += 100
    print("small Pizza is 100")
elif size == "M" or size == "m":
    bill += 200
    print("Medium Pizza is 200")
else:
    bill += 300
    print("Large Pizza is 300")
    
add_pepperoni = input("Do you want pepperoni(Y/N)? ")
if add_pepperoni == 'Y' or add_pepperoni == 'y':
    if size == 'S' or size == 's':
        bill += 30
    else:
        bill += 50
        
extra_cheese = input("Do you need extra cheese(Y/N)? ")
if extra_cheese == 'Y' or extra_cheese == 'y':
    bill += 20
    
print(f"Your final bill is {bill}")