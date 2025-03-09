'''A, B and C are classes 
A is a super class. B is a sub class of A. C is a sub class of B.  
Create three methods in each class, 2 methods are specific to each class and third 
method (override method) should be in all three Classes A, B and C 
Create a class with main method. Create an object for each class A, B and C in main 
method and call every method of each class using its own object/instance. 
Call an overridden method with super class reference to B and C class’s objects 
Runtime Polymorphism with Data Members/Instance variables, Repeat the above 
process only for data members'''

class A:
    def __init__(self):
        self.name="Class A"
        
    def method1(self):
        print("This is Unique in A")
        
    def method2(self):
        print("This is Unique in A")
        
    def method3(self):
        print("This is Common Method in A")
        
class B(A):
    def __init__(self):
        super().__init__()
        self.name="Class B"
        
    def method4(self):
        print("This is Unique in B")
        
    def method5(self):
        print("This is Unique in B")
        
    def method3(self):
        print("This is Common Method in B (overide Method)")
        
class C(B):
    def __init__(self):
        super().__init__()
        self.name="Class C"
        
    def method6(self):
        print("This is Unique in C")
        
    def method7(self):
        print("This is Unique in C")
        
    def method3(self):
        print("This is Common Method in C (overide Method)")
        
##Accesing Class A,B,C by creating objects
if __name__=="__main__":
    a=A()
    b=B()
    c=C()
    
    print("------Calling Methods of A----------")
    a.method1()
    a.method2()
    a.method3()
    
    print("\n--------Calling Methods of B---------")
    b.method1()
    b.method2()
    b.method3()
    b.method4()
    b.method5()
    
    print("\n------Calling Methods of C---------")
    c.method1()
    c.method2()
    c.method3()
    c.method4()
    c.method5()
    c.method6()
    c.method7()
     
    print("\n----Run Time Polymorphism-------")
    refA: A = B()
    print("Overridden method withh super class reference:")
    refA.method3()
    
    refA=C()
    refA.method3()
    
    print("Runtime Polymorphism with data memebers")
    refA=B()
    print(refA.name)
    
    refA=C()
    print(refA.name)