""" 
Question
Write a program to find out ho many days, weeks, months we have
left if we live until 90 years old

input
-your current age

output should be
-You have a days, b weeks and c months left 

Assumption
-1 year = 365 days
-1 year = 52 weeks
-1 year = 12months
"""

























#Solution
age = int(input('Enter your age\n'))

years_left = 90 - age

days_left = years_left * 365

months_left = years_left * 12

weeks_left = years_left * 52

print(f'You have a {days_left} days, {weeks_left} weeks, and {months_left} months left')