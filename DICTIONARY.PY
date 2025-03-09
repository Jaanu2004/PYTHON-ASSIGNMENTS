# Create a Dictionary with at least 5 key value pairs of the Student ID and Name
data={
    35:"Rohith",
    18:"Kohli",
    7:"Dhoni",
    33:"Hardik",
    1:"K L Rahul"   
}
print(data)
# Adding the values in dictionary 
data[41]="Shreyas"
print(data)
#  Updating the values in dictionary 
data[35]="Rohith Sharma"
print(data)
# Accessing the value in dictionary
print(data[18])

# Create a nested loop dictionary
info={
    101:{'name':"Krish",'course':'Ds','marks':{"ds":25,"stat":24}},
    102:{'name':"Karthik",'course':'Bca','marks':{"cs":20,"stat":24}},
    103:{'name':"Arjun",'course':'Ds','marks':{"ds":22,"stat":20}},
    104:{'name':"Mahesh",'course':'Bca','marks':{"cs":25,"stat":21}},
    105:{'name':"Hishanth",'course':'Ds','marks':{"ds":19,"stat":23}}
}
print(info[101]["name"])

#Accessing all the elements through loop 
for id,details in info.items():
    print(f"\nID :{id}")
    print(f"Name : {details['name']}")
    print(f"Course : {details['course']}")
    for ds,stat in details['marks'].items():
        print(f"Marks : {ds} {stat}")
        
#  Print the keys present in a particular dictionary 
print(info.keys())

# Delete a value from a dictionary 
info[101].pop("course")
print(info)