# class Car:
#     # variables that are common for all instances
#     wheels = 'Four'

#     # Constructor method  - called when we initiate calls/ instance is created
#     def __init__(self,manufacturer,model):

#     # Instance variables specific to each instance 
#     self.manufacturer = manufacturer
#     self.model = model
        
    
#     # Instance method
#     def car_details(self):
#         return f'Four wheel car is manufactured by {self.manufacturer} and the model is {self.model}'

# car1 = Car('Toyota','Innova')
# car2 = Car('Renault','kwid')

# print(car1.model)


class math_power():

    def __init__(self,number):
        self.number = number

    def square(self):
        return self.number*self.number

    def cube(self):
        return self.number*self.number*self.number
    
    def quartic(self):
        return self.number*self.number*self.number*self.number


req1 = math_power(3)
print(req1.square())
print(req1.cube())
print(req1.quartic())


req1.quartic()


class Dog:
    # the Dog class
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        print("Wof!")
#let's create a couple of instances
roger=Dog("Rogger",8)
# let's inspect the objects we have, instances of the Bike class.
print(roger.name)
print(roger.age)

#let's bark!
roger.bark()


