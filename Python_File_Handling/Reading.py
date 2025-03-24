# Python Reading files (.txt, .json. csv)
import json
import csv

# Reading .txt files
# You can use absolute filepath as well
file_path = "File_Handling\\text.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
# If the file does not exist
except FileNotFoundError:
    print(f"That file was not found {file_path}")
# If user does not have permission to access that file
except PermissionError:
    print(f"You do not have permission to read that file {file_path}")


# Reading .json
file_path = "File_Handling\\newJson.json"
try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content["name"]) # json file is like a dictionary, thus we can access values using keys
# If the file does not exist
except FileNotFoundError:
    print(f"That file was not found {file_path}")
# If user does not have permission to access that file
except PermissionError:
    print(f"You do not have permission to read that file {file_path}")


# Reading csv files
file_path = "File_Handling\\newCSV.csv"
try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        print(content) # This just gives the memory address
        # To read the content, it must be printed line by line
        for line in content:
            print(line[0]) # Add index for specific columns
except FileNotFoundError:
    print(f"That file was not found {file_path}")
except PermissionError:
    print(f"You do not have permission to read that file {file_path}")