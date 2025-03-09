#Write a function for arithmetic operators(+,-,*,/) 
def arithmeticOperators(a,b):
    additon=a+b
    subtraction=a-b
    multiplication=a*b
    division=a/b
    print("Addition of {} and {} is {}".format(num1,num2,additon))
    print("Subtraction of {} and {} is {}".format(num1,num2,subtraction))
    print("multiplication of {} and {} is {}".format(num1,num2,multiplication))
    print("division of {} and {} is {}".format(num1,num2,division))
num1=int(input("Enter Number :"))
num2=int(input("Enter number :"))
arithmeticOperators(num1,num2)

#Write a method for increment and decrement operators(++, --)

#Incremented for loop
print("Incremented for loop")
for i in range(0,10,2):
    print(i,end=" ")
#Decremented for loop
print("\nDecremented for loop")
for i in range(10,0,-1):
    print(i,end=" ")
        
# Write a program to find the two numbers equal or not. 
a=int(input("\nEnter Number :"))
b=int(input("Enter number :"))
if a==b:
    print("Equal")
else:
    print("Not Equal")

# Program for relational operators (<,<==, >, >==) 
c=int(input("\nEnter Number :"))
d=int(input("Enter number :"))
print(c>d)
print(c<d)
print(c<=d)
print(c>=d)
print(c==d)
print(c!=d)

# Print the smaller and larger number 
def greater(a,b):
    if a>b:
        print("a is big")
    else:
        print("b is big")
def smaller(a,b):
    if a<b:
        print("a is small")
    else:
        print("b is small")

a=int(input("\nEnter Number :"))
b=int(input("Enter number :"))
greater(a,b)
smaller(a,b)