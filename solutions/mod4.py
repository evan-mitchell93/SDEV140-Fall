#prime solutions
import math
user_num = int(input("Enter an integer: "))

def is_prime(x):
    #the all() function returns true if all items in an iterable are true
    #if all numbers % i  != 0 then it is a prime
    #i goes from 2 to sqrt of the given number
    if all(num%i != 0 for i in range(2,int(math.sqrt(num))+1)):
        #if it is true it is prime and we want to display the number
        print(num)

#calling the function for each number in the list based on user input
for num in range(2,user_num + 1):
    is_prime(num)



#dictionary sorting solutions

sample_dict = {'Apple':0.50,'Banana':0.20,'Mango':0.99,'Coconut':2.99,'Pineapple':3.99}

#use the sorted function which takes an iterable (list,dict, etc), a key for what to stort by and reverse true or false
#use the .items() to get key value pairs so we have access to both pieces
#we want to sort by the value not the key so lambda x: x[1] gives us the value
sorted_dict = sorted(sample_dict.items(),key=lambda x: x[1],reverse=True)

print(sorted_dict[:3])

