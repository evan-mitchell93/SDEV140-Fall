"""
Evan Mitchell
Module 5 Examples
Functions and Recursion
11/20/2023
"""

#Function definition
def my_avg(num1,num2,num3):
    total = num1 + num2 + num3
    avg = total / 3
    return avg

#function call
#Assigns the returned value of my_avg to variable average
average = my_avg(76,100,89)
print(f"The average test score for the class: {average:.2f}")

#multiple return statements
def my_odd(x):
    if x % 2 == 1:
        return 1 #or True
    else:
        return 0 #or False
    
if my_odd(3):
    print("The number was odd")
else:
    print("The number was even")

#reusability
import my_module
my_module.my_func()