# Writing a multiple If statement one thing to consider
# is INDENTATION FORMAT

height = int(input("What is your height? "))

if height>=3:
    print("can ride")
    age=int(input("What is your age? "))
    if age<12:
        bill = 15000
        print("Ticket price is 15,000 Tsh. ")
    elif age<=18:
        bill = 30000
        print("Please pay 30,000 Tsh. ")
    else:
        bill = 50000
        print("Please pay 50,000 Tsh. ")
        
    Want_photo = input("Do you want photo (Y/N)? ")
    if Want_photo == 'Y' or Want_photo == 'y':
        bill = bill + 5000
        print(f"Your bill is {bill}")
        
else:
    print("Cant ride")
    
print("Thankyou. Bye. ")