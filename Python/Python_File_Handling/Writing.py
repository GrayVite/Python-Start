# Python writing files (.txt, .json, .csv)
import json
import csv


txt_data = "I like fish" # Adding the '\n' creates a new line in our text file

# The filepath can be relative or absolute
file_path = "File_Handling\\output.txt"

# The try block catches the FileExistsError as mode="x" cannot be used if file already exitst
# You can also use mode="w" but it does not have such error. It will overwrite the file
try:
    # When opening a file it's best practice to close it, the with statement takes care of that
    with open(file_path, mode="x") as file:
        # the open function takes two parameters. 1st is filepath
        # second is mode: "w"->write, "x"->write if file doesn't exist, "r"->read, "a"->append
        # the open function return a file object for us
        # the as keyword assigns it the name filr
        file.write(txt_data)
        print(f"Text file '{file_path}' was created")
except FileExistsError:
    print(f"That file already exists. '{file_path}'")

with open(file_path, mode="a") as file:
    file.write("\nHello World") # To add to new line use "\n"
    print(f"Text was appended to '{file_path}'")


emplyees = ["Eugiene", "Squidward", "Spongebob", "Patrick"]
# To write entries of a list use a for loop
with open(file_path, mode="a") as file:
    file.write("\n")
    for employee in emplyees:
        file.write(employee + " ")


# For JSON files use the json library

employee_dict = {"name": "Spongebob",
                "age": 30, 
                "job": "Cook"}

file_path = "File_Handling\\newJson.json"

try:
    with open(file_path, "w") as file: 
        # indentation gives better formatting
        json.dump(employee_dict, file, indent=4) # (data, file, indentation=spaces)
        print(f"File was created: {file_path}")
except FileExistsError:
    print(f"{file_path} already exitst")


# for csv files use csv library
employees = [["name", "age", "job"],
            ["Kathryn", 30, "Cook"],
            ["Allen", 30, "Unemployed"],
            ["Luke", 28, "Scientist"]]

file_path = "File_Handling\\newCSV.csv"

try:
    with open(file_path, "w", newline="") as file: # use the newline from writer object
        writer = csv.writer(file) # writer is an object that provides methods to write to csv files
        for row in employees:
            writer.writerow(row) # the wirter method gives us a newline
        print(f"csv file was created: {file_path}")
except FileExistsError:
    print(f"File already exists: {file_path}")

