"""
SDEV 140 Module 2
Evan Mitchell
11/1/2023

"""

#string formatting
# f - float, d - integer, s - string
#old way 'formatting' % value|variable name
print('Old way %.1f' %2.453)

#middle option {variable name : formatting}
print("Middle way {:.2f}".format(2.453))

#new way with f strings {variable|value : formatting}
print(f"New way {2.453:.2f}")
x = 2
print(f"New way: integers {x:03d}")

#for loops
#range returns a list of numbers: range(start,stop,step)
print("Range of values", list(range(3,7)))
print("Color Loop")
list_colors = ["color1","color2"]
for color in list_colors:
    print(color)
#for loop will look at each value in that list
print("First for loop")
total = 0
for x in range(1,4):
    print(x)
    total += x
    print("current sum: ", total)

#we can go in reverse
print("Reverse Loop")
for x in range(10,7,-1):
    print(x)

my_string = "Hello"
for c in my_string:
    print(c)

#If - then statements
x = 10
if x < 10:
    print("x is smaller")
elif x > 10:
    print("x is greater")
else:
    print("x is equal to")

#Letter grade
number = 77

if x > 89:
    print("A")
elif number > 79:
    print("B")
elif number > 69:
    print("C")
else:
    print("F")


#while loops
#counter controlled
counter = 0
while counter < 10:
    print(counter)
    ##additional steps can go here
    counter += 1

exit_str = 'ZZZ'

user_input = input("Enter a name or ZZZ to quit")
while user_input != 'ZZZ' and user_input != 'zzz':
    print(user_input)
    user_input = input("Enter a name or ZZZ to quit")


import random

print(random.randint(5,8))