'''
Write a program that print a number upto n (i.e 1 to hundred)
and then in such sequence when a number is divisible by 
3 print Fizzy when divisible by 5 prnt Buzzy and when are 
both divisible by 3 and 5 print FizzyBuzzy

'''






















for i in range(1, 100):
    if i%3 == 0 and i%5 == 0:
        print('FizzyBuzzy')
    elif i%5 == 0:
        print('Buzzy')
    elif i%3 == 0:
        print('Fizzy')
    else:
        print(i)