'''Write two methods with the same name but different number of parameters of same type 
and call the methods  '''

class Calc:
    def add(self, a, b=0):  # Default argument for second parameter
        return a + b
    def add(self, *args):  # Variable-length arguments
        return sum(args)

# Creating an object
math_obj = Calc()

# Calling methods with different number of parameters
print("Sum with 1 argument:", math_obj.add(10))      
print("Sum with 2 arguments:", math_obj.add(10, 20)) 
print("Sum with n arguments:", math_obj.add(10, 20,30,45)) 


'''Write two methods with the same name but different number of parameters of different 
data type and call the methods 
No method overloading in python '''
class Example:
    def show(self, a):
        if isinstance(a, int):
            print(f"Integer method called: {a}")
        elif isinstance(a, str):
            print(f"String method called: {a}")
        else:
            print(f"Other type method called: {a}")

obj = Example()
obj.show(10)       # Calls integer version
obj.show("Hello")  # Calls string version
obj.show(3.14)     # Calls default version

# Methods with the Same Name and Same Number of Parameters of the Same Type
class Example:
    def show(self, a, b, operation="add"):
        if operation == "add":
            print(f"Addition: {a + b}")
        elif operation == "multiply":
            print(f"Multiplication: {a * b}")

obj = Example()
obj.show(2, 3)                  # Default is addition
obj.show(2, 3, operation="multiply")  # Multiplication