"""
    Module 4 Examples
    Lists,Tuples,Dictionaries and Functions
"""


#Lists are a collection of data elements.
#Lists are ordered, mutable and allow for duplicate values

#creating a list with specific values
my_list = [6,7,8,9,1,2,3]

#creating a list to populate with user input
user_list = []

#add 3 numbers from the user
for x in range(3):
    user_number = int(input("Enter an integer: "))
    user_list.append(user_number)

#accessing elements in a list using [index] where
#index is 0 -> len(list) - 1
print("Accessing the 2nd element at index 1: ",user_list[1])

#iterating over a list using a for loop
for item in user_list:
    value = item

#removing items from a list
#pop removes the last element and returns it
my_list.pop()

#pop(index) removes an element at a given index
my_list.pop(0)

#remove(value) removes a single instance of a value from the list
my_list.remove(7)

#finally you can use the del keyword to remove an index
del my_list[0]

print("my_list after removal of elements: ", my_list)

#Tuples are simlar to lists but they are immutable (cannot change values)

#creating a tuple
my_tuple = ("Hello","World")

#accessing values
print("First element from a tuple: ", my_tuple(0))

#unpacking tuples
#you can assign variables to elements of a tuple
word1,word2 = my_tuple

#Dictonaries store elements in key:value pairs. For {} notation
#keys must be inside of "". {"name":"Evan"}.. for dict() notation
#keys must be a valid variable name dict(name="Evan")

my_dict = {
    "username":"epmitche",
    "password":"a;lsdkfja;fl",
    "fav color": "purple",
    "age": 30
}

#to access values, use [key]
print("Dictionary value: ", my_dict['fav color'])

#to update a value use [key] = value
my_dict['password'] = "new password not secure"

#to remove a pair: pop(key),popitem() - last item added, del dict[key]
my_dict.pop('name')
my_dict.popitem() #removes age
del my_dict['password']



#functions allow us to reuse code and create "modules" like in SDEV 120
#functions are defined in the following way

def my_func(param1,param2):
    return param1 + param2 // 10

#my_func is the name that will be used to call or invoke the function
#param1 and param2 are parameters that are defined for use inside of the function
#arguments are the values we will pass in to the function that are referenced by the parameters
#the return statement sends a value back to the caller of the function. A lot of times you will assign
#the returned value to a variable

my_value = my_func(10,100)

#if you initialize a variable inside of a function, it is not accessible by the caller unless it is returned

def no_access():
    x = 10

#if i call no_access() I can not then access x
v = no_access()
print(x) #will not work

#if we updated to say return x at the bottom we still could not print(x) but we could print(v) wich would have the value from x