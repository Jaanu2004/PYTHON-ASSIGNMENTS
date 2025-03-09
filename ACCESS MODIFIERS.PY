'''Create a class with PRIVATE fields, private method and a main method. Print the fields 
in main method. Call the private method in main method. 
Create a sub class and try to access the private fields and methods from sub class.'''

class Parent:
    def __init__(self):
        self.__private_field = "This is Private"  # Private field

    def __private_method(self):  # Private method
        print("This is a private method")

    def access_private_method(self):  
        self.__private_method()  # Indirect access via public method

    def access_private_field(self):  
        return self.__private_field  # Indirect access via public method

class Child(Parent):
    def __init__(self):
        super().__init__()

    def try_access_private(self):
        print("Trying to access private members from Child class:")

        # These will cause AttributeError
        # print(self.__private_field)  
        # self.__private_method()

        #  Use parent class methods
        print("Accessing Private Field through Parent Method:", self.access_private_field())
        self.access_private_method()

if __name__ == "__main__":
    obj = Parent()
    print("Accessing Private Field (Indirectly):", obj.access_private_field())  
    obj.access_private_method()  

    print("\nTrying to access private members from Child class:")
    child_obj = Child()
    child_obj.try_access_private()  

'''Create a class with PROTECTED fields and methods. Access these fields and methods 
from any other class in the same package.  
Also, Access the PROTECTED fields and methods from child class located in a different 
package 
Access the PROTECTED fields and methods from any class in different package '''

class Parent:
    def __init__(self):
        self._protected_field = "I am Protected"  # Protected field

    def _protected_method(self):  # Protected method
        print("This is a protected method")

class Child(Parent):
    def access_protected(self):
        print("Accessing Protected Field in Child:", self._protected_field)  
        self._protected_method()  

if __name__ == "__main__":
    obj = Parent()
    print("Accessing Protected Field (From Same Package):", obj._protected_field)  
    obj._protected_method()  

    print("\nAccessing Protected Members from Child Class:")
    child_obj = Child()
    child_obj.access_protected()

'''Create a class with PUBLIC fields and methods.  
Access the public methods and fields from any class in the same package or different 
package.'''

class PublicClass:
    def __init__(self):
        self.public_field = "I am Public"  # Public field

    def public_method(self):  # Public method
        print("This is a public method")

if __name__ == "__main__":
    obj = PublicClass()
    print("Accessing Public Field:", obj.public_field)  
    obj.public_method() 
