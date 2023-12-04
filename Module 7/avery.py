"""/// N O T E S ///

CLASSES: Programmers who use objects and classes know
    - The interface that can be used with a class
    - The state of an object
    - How to instantiate a class to obtain an object

Objects are abstractions
    - Package their state and methods in a single entity that can be referened with a name
Class definition is like a blueprint for each of the objects of that class
    - Definitions of all the methods an object recognizes
    - Descriptions of the data structures used to maintain the state of an object

(Tkinter(Easy Frame(Main))) ('main' class is a subclass of easyframe is a subclass of tkinter)

SYNTAX:
class <class name>(<parent class name>):
<method definition-1>


Instance Variable: Each instance of an object within a class has it's own instance variable. Ex. each student in a classroom has an instance variable of their test scores.

Example:
(Class)Person
    (Attributes)
    Name
    Age
    Address
(Subclass)Instructor
    Dept
    Salary
    Classes
(Subclass)Student   #many students
    Major
    Classes
    GPA

    

"""


#Using (''' ''' we can comment into the help page)
#Scroll over different parts of this holding CTRL

"""() DOCSTRING COMMENT CREATION
def my_example():
    '''This is our example docstring'''
    return "Hello"
my_example()
#"""

#""" 'CLASS' DEFINITIONS
#'''
class Student():

    def __init__(self,name,fav_color,major="SDEV"):
        self.f_name = name
        self.major = major
        self.fav_color = fav_color

    def say_hello(self):    #self is a required part of this definition for some reason. Deleting it fails the system
        print(f"Bonjour {self.f_name}")

    def __str__(self):
        return (f"Student: {self.fname}, Major: {self.major}")
    
    #Accessor
    def get_name(self):
        return self.f_name
    
    def get_color(self):
        return self.fav_color
    
    def chnage_color(self, new_color):
        self.fav_color = new_color
    
s = Student("Avery", "Green", "CSCI")   #s is now all we need to call Student()
print(s)
s.say_hello()   #returns the method 'say_hello' from class Student()
    #'''

#"""

#"""
#'''

    #'''
#"""

