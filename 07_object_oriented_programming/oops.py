# Class name should always be capitalized
    # self here means whoever calls it, some languages uses this has context or this(js)
    # init it often called as constructor, which gets called automaticallt when a class is called
class Car:

    total_car = 0

    def __init__(self, brand, model):
        # If you apply 2 underscores before a variale, you can only access it within the class, however if someone wants to access it then they can only do it via getter method.
        self.__brand = brand
        self.__model = model
        Car.total_car += 1 #This is also a way of accessing variables within the class, but yes we can continue to use self.

    @property
    def model(self):
        return self.__model

    # You can name this method anything, but it is a basic convention so we should follow as it is.
    def get_brand(self):
        return self.__brand + " !"


    def carType(self):
        print(f"The car is {self.__model}, {self.__brand}")

    def fuel_type(self):
        return "Petrol or Disel"
    
    @staticmethod
    def general_description():
        return "Cars are availale in both petrol, disel and electric"
    
my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)


my_car2 = Car("Tata", "Safari")
# print(my_car2.model)

my_car.carType()
my_car2.carType()


# Inheritance (extend a class)

class ElecticCar(Car):
    def __init__(self, brand, model, battery_size):
        # Using super takes you to the parent class and then we take the brand and model access from there.
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

my_tesla = ElecticCar("Tesla", "Model S", "85kWh")
print(my_tesla.model)


# Encapsulation
# Make some variables private so that not everyone can access it.

print(my_tesla.get_brand())


# Polymorphism
# 2 different methods by returns different values based on class
# fuel_type

print(my_car2.fuel_type())
print(my_tesla.fuel_type())


# Keep a track of number of objects made using Car Class ; total_car

# print(my_car2.total_car) # This is not the correct way of checking the total cars

print(Car.total_car) # So you can check the values like this.

# Extended classes also adds into this total_car as the init method is being called there as well


# Static method
# A static method means a method which is only accessible by the Class itself, but not by it's instances.

# print(my_car2.general_description()) # This should not work


# So we write "@staticmethod" before the definition itself, so that it's stays within the Class and cannot be accessed by the inherited ones.
# No need to use "self" as the connectioning isn't required.

# @staticmethod is called as decorator
print(Car.general_description())


# Read-only atrribute

# my_car2.model = "City"
# We need to first make it private using 2 underscores.
# Then we use the @property to make sure we are able to access it as a variable like .moel instead of .model()
print(my_car2.model)

# This above code changes the car model, but we want to prevent this.
# This is often used to make sure no-one is able to overwrite the value once it is set.


# Use instance() to check if it is a instance of Car and ElectricCar.
print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElecticCar))


# Multiple inheritance

class Battery:
    def battery_info(self):
        return "This is battery info"

class Engine:
    def engine_info(self):
        return "This is engine info"


class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")

print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())