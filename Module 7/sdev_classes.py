"""
Evan Mitchell
12-4-2023
SDEV 140 Module 7
Classes
"""

def my_example(x):
    """This is our example docstring"""
    return x + 4

my_example(5)

#class definitions
class Student():
    def __init__(self,name,fav_color,major="SDEV"):
        self.f_name = name
        self.major = major
        self.fav_color = fav_color

    def say_hello(self):
        print(f"Bonjour {self.f_name}")

    def __str__(self):
        return f"Student: {self.f_name}, Major: {self.major}"
    #accessors
    def get_name(self):
        return self.f_name
    
    def get_color(self):
        return self.fav_color
    #mutator
    def change_color(self,new_color):
        self.fav_color = new_color

s = Student("Evan","Purple","CSCI")
print(s)
s.say_hello()





