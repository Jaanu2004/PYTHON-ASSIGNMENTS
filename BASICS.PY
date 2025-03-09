#Write a program to print your name.
print("Jahnavi Rambha")

#Write a program for a Single line comment and multi-line comments 

#This is Single line Comment

'''This is multiline 
comment in python.
We can write as many lines we want
'''

#Define variables for different Data Types int, Boolean, char, float, double and print on the Console.

integer_var=14
boolean_var=True
str_var="String" #Since python doesn't have char type it stores as str
float_var=14.98
double_var=1.2345678924536354748959  #Since python doesn't have double type it stores as float

print("Integer :",type(integer_var))
print("Boolean :",type(boolean_var))
print("String :",type(str_var))
print("Float : ",type(float_var))
print("Double :",type(double_var))

#Define the local and Global variables with the same name and print both variables and understand the scope of the variables 
value=10
def var1():
    print("Inside function without assigning value: ",value)
def var2():
    value=5
    print("Inside Function without global keyword :",value)
def var3():
    global value
    value=8
    print("Inside function using global keyword :",value)
print("Global :",value)
var1()
print("Global :",value)
var2()
print("Global :",value)
var3()
print("Global :",value)