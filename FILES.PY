#creating file
with open("sample.txt", "w") as file:
    file.write("Hello, this is a sample text file!")
print("File created successfully!")


# Open and read a text file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)

# Program to Read a File Stream
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())
        
# Write a program to read a file stream supports random access
with open("sample.txt", "r") as file:
    file.seek(10)  # Move to the 10th byte
    print("Reading from 10th byte:", file.read(20))
    
#  Write a program to read a file a just to a particular index using seek()
with open("sample.txt", "r") as file:
    file.seek(5)  # Move to the 5th byte
    print("Reading from 5th byte:", file.read(15))
    
# Program to Check File Read and Write Permissions
import os

file_path = "sample.txt"

# Checking file permissions
if os.access(file_path, os.R_OK):
    print(f"{file_path} has Read permission.")
else:
    print(f"{file_path} does NOT have Read permission.")

if os.access(file_path, os.W_OK):
    print(f"{file_path} has Write permission.")
else:
    print(f"{file_path} does NOT have Write permission.")