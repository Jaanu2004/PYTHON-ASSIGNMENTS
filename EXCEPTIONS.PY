# 1. Generate Arithmetic Exception without Exception Handling
# result = 10 / 0  # Uncomment this to see ZeroDivisionError

# 2. Handle Arithmetic Exception using try-except block
try:
    result = 10 / 0  
except ZeroDivisionError as e:
    print("Arithmetic Exception Occurred:", e)
    
# 3. Method That Throws an Exception, Call it Without try block
def risky_method():
    raise ValueError("This method always raises an exception!")

# Handling the exception to prevent stopping execution
try:
    risky_method()
except ValueError as e:
    print("Caught exception from risky_method:", e)

# 4. Program with Multiple except Blocks
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
except Exception as e:
    print("An unexpected error occurred:", e)
    
# 5. Throw Exception with Custom Message
def check_number(n):
    if n < 0:
        raise ValueError("Negative numbers are not allowed!")

try:
    check_number(-5)
except ValueError as e:
    print("Custom Exception:", e)

# 6. Create Your Own Exception
class MyCustomException(Exception):
    def __init__(self, message="This is a custom exception"):
        self.message = message
        super().__init__(self.message)

try:
    raise MyCustomException("Something went wrong!")
except MyCustomException as e:
    print("Caught Custom Exception:", e)

# 7. Program with finally block
try:
    num = 10 / 0  
except ZeroDivisionError:
    print("Caught a division by zero error.")
finally:
    print("This will always execute, whether an exception occurs or not.")

# 8. Generate Arithmetic Exception
try:
    num = 10 / 0  # ZeroDivisionError
except ZeroDivisionError as e:
    print("Caught Arithmetic Exception:", e)

# 9. Generate FileNotFoundException
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print("FileNotFoundException caught:", e)

# 10. Generate ClassNotFoundException (Simulated using ImportError)
try:
    import non_existent_module  #Trying to access module that doesn't exist
except ImportError:
    print("Module not found error!")

# 11. Generate IOException
import os

try:
    os.remove("non_existent_file.txt")  # Attempt to delete a non-existing file
except OSError as e:
    print("IOException occurred:", e)

# 12. Generate NoSuchFieldException (Simulated using AttributeError)
class Sample:
    def __init__(self):
        self.field = 10

obj = Sample()
try:
    print(obj.non_existent_field)  # AttributeError simulating NoSuchFieldException
except AttributeError as e:
    print("NoSuchFieldException simulated:", e)
