# Create an abstract class with abstract and non-abstract methods. 
from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):  
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):  # Abstract method
        pass  

    def sleep(self):  # Non-abstract method
        print(f"{self.name} is sleeping.")

# Create a sub class for an abstract class. Create an object in the child class for the  abstract class and access the non-abstract methods
class Dog(Animal):
    def make_sound(self):  # Implementing the abstract method
        print(f"{self.name} says: Woof Woof!")

# Creating an object for the abstract class inside the child class
dog = Dog("Tommy")
dog.sleep() 

# Create an instance for the child class in child class and call abstract methods 
dog.make_sound()  

# Create an instance for the child class in child class and call non-abstract methods
dog.sleep()  
