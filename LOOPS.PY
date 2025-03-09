# Write a program to print  “Bright IT Career”  ten times using for loop
n= 'Bright IT Career'
for i in range(10):
    print(n)

# Write a python program to print 1 to 20 numbers using the while loop. 
i=1
while(i<=20):
    print(i)
    i=i+1

# Program to equal operator and not equal operators
a=int(input("\nEnter Number :"))
b=int(input("Enter number :"))
if a==b:
    print("Equal")
elif a!=b:
    print("Not Equal")

#  Write a program to print the odd and even numbers. 
n=int(input("Enter Number range :"))
for i in range(n):
    if i%2==0:
        print("{} is Even".format(i))
    else:
        print("{} is odd".format(i))
        
# Write a program to print largest number among three numbers.
a=int(input("Enter 1st Number"))
b=int(input("Enter 2nd number"))
c=int(input("Enter 3rd number"))
if a>b and a>c:
    print("a is big")
elif b>c:
    print("b is big")
else:
    print("c is big")
    
# Write a  program to print even number between 10 and 20 using while
i=10
while(i<=20):
    if i%2==0:
        print(i,end=" ")
    i=i+1

# Write a program to print 1 to 10 using the do-while loop statement.
#since there is no do while we are simulating it
print("\nProgram to print 1 to 10 ")
i=1
while True:
    print(i)
    i=i+1
    if i>10:
        break
    
# Write a program to find Armstrong number or not 
n=int(input("Enter a number :"))
temp=n
size=len(str(n))
s=0
while n!=0:
    r=n%10
    s=s+(r**size)
    n=n//10
if temp==s:
    print("It is a Armstrong Number")
else:
    print("It is not a Armstrong Number")

# Write a program to find the prime or not.
def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input("enter Number"))
if prime(n):
    print("Prime")
else:
    print("Not prime")
    
# Write a program to palindrome or not.
n=int(input("Enter a Number"))
temp=n
s=0
while n!=0:
    r=n%10
    s=(s*10)+r
    n=n//10
if temp==s:
    print("Palidrome")
else:
    print("not palindrome")
    
# Program to check whether a number is EVEN or ODD using switch 
n=int(input("Enter a number :"))
switch={
    0:"Even",
    1:"Odd"
}
print(switch[n%2])

# . Print gender (Male/Female) program according to given M/F using switch
n=input("Enter Gender(M/F):")
gender={
    "M":"Male",
    "F":"Female"
}
print(gender[n])