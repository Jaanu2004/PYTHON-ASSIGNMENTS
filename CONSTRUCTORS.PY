# Class with Default, One-Argument, and Two-Argument Constructors
class ConstructorDemo:
    # Default constructor
    def __init__(self, name="Default", age=None):
        self.name = name
        self.age = age
        print(f"Constructor called: Name = {self.name}, Age = {self.age}")

# Instantiating objects with different constructors
obj1 = ConstructorDemo()               # Calls default constructor
obj2 = ConstructorDemo("Alice")        # Calls one-argument constructor
obj3 = ConstructorDemo("Bob", 25)      # Calls two-argument constructor


# Call the constructors(both default and argument constructors) of super class from a child class
class Parent:
    def __init__(self, message="Parent Constructor"):
        print(message)

class Child(Parent):
    def __init__(self):
        super().__init__("Calling Parent Constructor from Child")  # Calls Parent constructor
        print("Child Constructor Called")

# Instantiating child class
child_obj = Child()


# Apply Private, Public, Protected, and Default Access Modifiers to Constructors
class AccessModifiers:
    def __init__(self): 
        print("Public Constructor Called")

    def _protected_constructor(self):  
        print("Protected Constructor Called")

    def __private_constructor(self): 
        print("Private Constructor Called")

# Creating an instance of the class
obj = AccessModifiers()
obj._protected_constructor()  
# obj.__private_constructor()  # This will raise an AttributeError


#  Program Illustrating Attributes of a Constructor
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand  # Instance attribute
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")

# Creating objects with attributes
car1 = Car("KIA", "SONET", 2022)
car2 = Car("HYUNDAI", "I20", 2020)

# Accessing attributes
car1.display_info()
car2.display_info()