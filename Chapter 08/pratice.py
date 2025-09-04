
#? Q1. Create a text file and write content
with open("myfile.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("Welcome to File I/O practice.\n")

#? Q2. Read the entire content of a file
with open("myfile.txt", "r") as file:
    content = file.read()
    print(content)


#? Q3. Read all lines into a list
with open("myfile.txt", "r") as file:
    lines = file.readlines()
    print(lines)

#? Q4. Append new content to a file
with open("myfile.txt", "a") as file:
    file.write("This line is added later.\n")

#? Q5. Copy content from one file to another
with open("myfile.txt", "r") as source:
    content = source.read()

with open("copyfile.txt", "w") as dest:
    dest.write(content)

#? Q6. Count number of lines in a file
with open("myfile.txt", "r") as file:
    lines = file.readlines()
    print("Total lines:", len(lines))