# WORKING WITH FILES
# CREATE A NEW FILE
# MODES --> 'w' -- WRITING, 'r' -- READING, 'r+' -- READING/WRITING
file = open("./data.csv", "w")
# WRITE DATA TO FILE
file.write("""Writing a very random
text into the file
to see whether formatting really
works while creating a file.""")

# READING A FILE --> COMMENT WRITING ABOVE AND CHANGE THE FLAG
print(file.read())
# LINE BY LINE READING
for line in file:
    print(line)
# CLOSE THE RESOURCE
file.close()

# IF WE DON'T WANT TO CLOSE RESOURCE, USE THE with ____ as ___ SYNTAX
with open("./data.csv", "r") as file:
    print(file.read())

# CHECK IF A FILE EXISTS
import os

fileName = "./data.csv"
if os.path.isfile(fileName):
    print(f"Do your logic if the file {fileName} exists...")
else:
    print(f"File {fileName} does not exist")
