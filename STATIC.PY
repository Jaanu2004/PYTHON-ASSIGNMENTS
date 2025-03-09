#  Define a static variable and access that through a class 
class Student:
    clg="Aditya Degree College"
    def __init__(self):
       self.name="Jahnavi"
       self.no=27
    
s1=Student() #Creating an instance
s2=Student()
print(Student.clg) #Accessing through class

# Define a static variable and access that through a instance 
print(s1.clg)
print(s2.clg)

# Define a static variable and change within the instance 
s1.clg="Aditya Degree College for Women"
print(s1.clg)
print(Student.clg)

# Define a static variable and change within the class 
Student.clg="Aditya Degree College for Women,Rajahmundry"
s2.name="Bhanu"
print(Student.clg)
print(s1.name,s1.clg)
print(s2.name,s2.clg)