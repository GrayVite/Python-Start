# Python File Detection

# This module provides python the ability to interact with files
import os

filepath = "File_Handling\\text.txt"


# The os.path.exists() returns True if a file exists at the filepath

# To check for relative paths
if os.path.exists(filepath):
    print(f"The location '{filepath}' exists")
else:
    print(f"That location '{filepath}' doesn't exist")


# To check for absolute paths
filepath = "C:\\Users\\Laptop House\\OneDrive\\Desktop\\to do list.txt"
if os.path.exists(filepath):
    print(f"The location '{filepath}' exists")
else:
    print(f"That location '{filepath}' doesn't exist")


filepath = "OOP"
if os.path.exists(filepath):
    print(f"The location '{filepath}' exists")

    if os.path.isfile(filepath): # Check if the location is a file 
        print("That is a file")
    elif os.path.isdir(filepath): # Check if the location is a folder/directory
        print("That is a directory")

else:
    print(f"That location '{filepath}' doesn't exist")