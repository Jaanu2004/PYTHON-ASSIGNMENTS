# Different ways creating a string 
name="Jahnavi"
print(name)
Gender='Female'
print(Gender)
degree=input("Enter Your Degree") #reading input from user
print(degree)
bio="""This is used to read multiline strings
This is Jahnavi
Pursuing Bsc Data Science"""
print(bio)


#Concatenating two strings using + operator
str1="Ramu and Ravi"
str2="are very good Friends"
print(str1+" "+str2)

# Finding the length of the string 
str1="Theses are coding Challanges"
print(len(str1)) #Using inbuilt function

#Finding length using for loop
s=0
for i in str1:
    s=s+1
print(s)


# Extract a string using Substring 
str1="Accessing Substring"
print(str1[:9])
print(str1[10:])
print(str1[::-1])

# Searching in strings using index() 
print("position of 'String 'is at ",str1.index("Substring"))

# Matching a String Against a Regular Expression With matches() 
import re
str1="Jahnavi"
str2="Jahnavi goes to College"
print(re.match(str1,str2)) #Only matches if it starts with the given word

# Comparing strings 
str1="Biryani"
str2="biryani"
print(str1==str2)
print(str1!=str2)
print(str1<str2)
print(str1>str2)
str1=str2 #assigning same value 
print(str1==str2)

# startsWith(), endsWith() and compareTo()
name="Varadharaja Mannar"
name1="Devaratha Raiser"
print(name.startswith("Varadha"))
print(name.endswith("Mannar"))

#since there is no compareTo function in python we are writing function for it
def compareTo(str1,str2):
    if str1<str2:
        return -1
    elif str1>str2:
        return 1
    elif str1==str2:
        return 0
print(compareTo(name,name1))

# Trimming strings with strip()-strip reomoves whitespacces-tabs,spaces,newlines
text="  'Take this' "
trimText=text.strip()
print("before using strip()",text)
print("After using strip()",trimText)    

# Replacing characters in strings with replace()
fruit="Mango is my favourite"
rep=fruit.replace("Mango","Apple")
print("Before replace:",fruit)
print("After replace:",rep)

#  Splitting strings with split()
print(fruit.split(" "))

#  Converting integer objects to Strings 
age=19
strconv=str(age)
print("age in int datatype",type(age))

print("After conversion into str",type(strconv))

# Converting to uppercase and lowercase 
print(name.lower())
print(name1.upper())