# Write a function to add integer values of an array
def arraySum(n):
    sum=0
    for i in n:
        sum+=i
    print(sum)
n=list(map(int,input().split()))
arraySum(n)

# Write a function to calculate the average value of an array of integers
def arrayAvg(n):
    sum=0
    for i in n:
        sum+=i
    avg=sum/(len(n))
    print(avg)
n=list(map(int,input().split()))
arrayAvg(n)

# Write a program to find the index of an array element 
n=int(input("Enter the element  to find its index : "))
arr=[12,23,5,78,13,3]
for i in range(0,len(arr)):
    if arr[i]==n:
        print(f"Element found at {i} index")
        break
else:
    print("Element Not found")
    
# Write a function to test if array contains a specific value
def findElement(n,ele):
    if ele in n:
        print("Found")
    else:
        print("Not Found")
n=list(map(int,input("enter array elements : ").split()))
ele=int(input("enter element to check : "))
findElement(n,ele)

# Write a function to remove a specific element from an array 
def removeEle(n,ele):
    if ele in n:
        n.remove(ele)
    else:
        print("Element Not found")

n=[12,34,56,78]
ele=int(input("Enter Element to remove :"))
removeEle(n,ele)

# Write a function to copy an array to another array 
def arrayCopy(arr1):
    return arr1.copy()
arr1=[12,2,356]
arr2=[34,46]
arr2=arrayCopy(arr1) #replaces the existing elements and stores copied values
print(arr2)

# Write a function to insert an element at a specific position in the array 
def insertEle(arr,ele,pos):
    return arr.insert(pos,ele)
arr=[12,23,45,56]
ele=int(input("Enter Element to insert : "))
pos=int(input("Enter Position to insert : "))
insertEle(arr,ele,pos)
print(arr)

# Write a function to find the minimum and maximum value of an array
arr=list(map(int,input().split()))
print(max(arr))
print(min(arr))

# Write a function to reverse an array of integer values 
def reverseArr(arr):
    n=len(arr)
    for i in range(n//2):
        arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
    return arr
arr=list(map(int,input().split()))
print("Reversed array:",reverseArr(arr))


#  Write a function to find the duplicate values of an array
def dupArray(arr):
    duplicates=[]
    dic={}
    for num in arr:
        if num in dic:
            if dic[num]==1:
                duplicates.append(num)
            dic[num]+=1
        else:
            dic[num]=1
    return duplicates
n=list(map(int,input().split()))
print(dupArray(n))

#  Write a method to remove duplicate elements from an array 
def removeDuplicates(arr):
    unique_list=[]
    seen=set()
    for num in arr:
        if num not in seen:
            unique_list.append(num)
            seen.add(num)
    return unique_list
n=list(map(int,input().split()))
print(removeDuplicates(n))

#  Write a program to find the common values between two arrays
def commonElements(arr1,arr2):
    l=[]
    for i in arr1:
        for j in arr2:
            if i==j:
                l.append(i)
    return l
arr1=[1,2,3,4]
arr2=[3,4,5,6]
print(commonElements(arr1,arr2))

#  Write a method to find the second largest number in an array 
def secondLargest(arr):
    large=second=arr[0]
    for num in arr:
        if num>large:
            second=large
            large=num
        elif num>second and num<large:
            second=num
    return second
arr=[12,34,13,56,49]
print(secondLargest(arr))
        
# . Write a method to find number of even number and odd numbers in an array 
def arrayEvenOdd(arr):
    e=[]
    o=[]
    for i in arr:
        if i%2==0:
            e.append(i)
        else:
            o.append(i)
    return e,o
arr=list(map(int,input("Enter Array elements").split()))
even,odd=arrayEvenOdd(arr)
print("Even Numbers : ",even)
print("Odd Numbers : ",odd)

#  Write a function to get the difference of largest and smallest value
def arrayDiff(arr):
    if not arr:
        return "Array is Empty! Enter Array Elements"
    return max(arr)-min(arr)
arr=list(map(int,input("Enter Array elements").split()))
print("The difference Between Largest and Smallest Element : ",arrayDiff(arr))

#  Write a method to verify if the array contains two specified elements(12,23) 
def arrayCheck(arr):
    if 12 in arr or 23 in arr:
        return "The Element Exist"
    else:
        return "The Element doesn't Exist"
arr=list(map(int,input("Enter Array elements").split()))
print(arrayCheck(arr))
    