"""
Evan Mitchell
12-4-2023
SDEV 140 Module 7
Classes
"""

"""def my_example(x):
    This is our example docstring
    return x + 4

my_example(5)

#class definitions
class Student():
    def __init__(self,name,fav_color,major="SDEV",):
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
s.say_hello()"""


#####Subclassing

#Parent/Super class

class Person:
    def __init__(self,first_name,last_name):
        self.f_name = first_name
        self.l_name = last_name
    
    def printname(self):
        print(self.l_name + ', ' + self.f_name)

p1 = Person("Evan","Mitchell")
p1.printname()

### subclass student
class Student(Person):
    def __init__(self,first_name,last_name,major,year,gpa=0.0):
        Person.__init__(self,first_name,last_name)
        self.major = major
        self.year = year
        self.gpa = gpa
    #overide the parent method. Will be called from student
    def printname(self):
        print(self.l_name + ", " + self.f_name + " :" + str(self.gpa))
    
    def update_gpa(self,new_gpa):
        self.gpa = new_gpa
    def get_gpa(self):
        return self.gpa
s1 = Student("Bob","Bobber","INFM","Freshman")
s1.update_gpa(3.5)
s1.printname()

#create second subclass
class Instructor(Person):
    def __init__(self, first_name, last_name,department,salary):
        Person.__init__(self,first_name, last_name)
        self.dep = department
        self.sal = salary
import pickle
"""i1 = Instructor("Evan","Mitchell","SOIT","Some dollars")
i1.printname()
print(i1.sal)



#file handler f with filename opened in write binary mode
f = open("ourobjects.obj","wb")
#pass in the object variable and file handler
pickle.dump(i1,f)

f.close()"""

 ##get the Instructor from the file
f = open('ourobjects.obj','rb')
instructor_test = pickle.load(f)

print(instructor_test.sal)
f.close()
