# -------Classes/Objects---------
# A Class is like an object constructor, or a "blueprint" for creating objects.

# Create a Class---Create a class named MyClass, with a property named x:
class MyClass:
    x=5
print(MyClass)

# Create Object---Create an object named p1, and print the value of x:
class MyClass:
    y=6
p1=MyClass()
print(p1.y)

# The __init__() Function----All classes have a function called __init__(), which is always executed when the class is being initiated.
# Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
    # The __init__() function is called automatically every time the class is being used to create a new object.
    def __init__(self,name,age):
     self.name=name
     self.age=age
p1=Person("Rohit",40)
print(p1.name)
print(p1.age)

# The __str__() Function : The string representation of an object WITHOUT the __str__() function:
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person("Sachin",50)
print(p1)
# The string representation of an object WITH the __str__() function:
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name}({self.age})"
p1=Person("Surya",33)
print(p1)


# Object Methods : Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfun(self):
        # The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
        print("Hello my name is " +self.name)

p1=Person("Kanna",26)   
p1.myfun()


class Dog:
    # the Dog class
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        print("Wof!")
        
roger=Dog("Rogger",8)
print(roger.name)
print(roger.age)

roger.bark()


# let's define the class Bike
class Bike():
# Constructor
    def __init__(self,colour,frame_material):
        self.colour = colour
        self.frame_material = frame_material
    
    def brake(self):
        print("Braking!")
#let's create a couple of instances
red_bike = Bike('Red', 'Carbon fiber')
blue_bike = Bike('Blue', 'Steel')
# let's inspect the objects we have, instances of the Bike class.
print(red_bike.colour)
print(red_bike.frame_material)
print(blue_bike.colour)
print(blue_bike.frame_material)
# let's brake!
red_bike.brake()






