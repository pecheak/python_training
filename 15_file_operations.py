"""
Read/Write operations with text files like .txt
"""

"""
We need to follow 3 steps
Step-1: Connect to file
Step-2: Read/Write
Step-3: Disconnect
"""

"""
We have functions for all 3 steps

Step-1: Connect to file
    - open() function

Step-2: Read/Write
    - For Writing: 1) write 2) writelines 3) print-function
    - For Reading: 1) read 2) readline 3) readlines

Step-3: Disconnect
    - close()
"""

print("All Write Operations")
print("-" * 20)
# ---------------

# Step-1: Connect to file
# ---------------

# my_file_handle = open("file name or file path here", "mode")
my_file_handle = open("my_out_file.txt", "w")
# mode "w": Write only mode
# mode "w": It will create new file
# mode "w": IMPORTANT: It will erase existing file content

# Step-2: Write
# ---------------
# For Writing: 1) write 2) writelines 3) print-function

# Our Data
x = 10
y = "Python"

# Convert other type of data to 'string' because 1) write 2) writelines
#   expects data in the form of string
x = str(x)

# 1) write: We can pass one string
my_file_handle.write(x + "\n")
my_file_handle.write(y + "\n")

# 2) writelines
my_data_in_list = [x + "\n", y + "\n"]
my_file_handle.writelines(my_data_in_list)

# 3) print-function
print(x, y, 20, "Java", sep="\n", file=my_file_handle)

# Step-3: Disconnect
# ---------------
my_file_handle.close()

print("""
Created 'my_out_file.txt'. Please check
""")

print("#" * 40, end="\n\n")
#########################################





print("Read Operations: 1) read")
print("-"*20)
# ---------------

# Step-1: Connect to file
# ---------------
my_file_handle = open("my_out_file.txt", "r")
# mode "r": Read Only mode
# mode "r": It will not create new file if file not present

# Step-2: Read
# ---------------
file_content = my_file_handle.read()
# It will return complete file content in one string
print("file_content:", file_content, sep="\n", end="\n\n")
print("file_content in RAW FORMAT:", repr(file_content), sep="\n", end="\n\n")

# Step-3: Disconnect
# ---------------
my_file_handle.close()

print("#"*40, end="\n\n")
#########################################





print("Read Operations: 2) readline")
print("-"*20)
# ---------------

# Step-1: Connect to file
# ---------------
my_file_handle = open("my_out_file.txt", "r")
# mode "r": Read Only mode
# mode "r": It will not create new file if file not present

# Step-2: Read
# ---------------
file_content = my_file_handle.readline()# It will return one line
print("1st line ", file_content, sep="\n", end="\n\n")

file_content = my_file_handle.readline()# It will return one line
print("2nd line ", file_content, sep="\n", end="\n\n")

# Step-3: Disconnect
# ---------------
my_file_handle.close()

print("#"*40, end="\n\n")
#########################################

print("Read Operations: 2) readline using for-loop")
print("-"*20)
# ---------------

# Step-1: Connect to file
# ---------------
my_file_handle = open("my_out_file.txt", "r")
# mode "r": Read Only mode
# mode "r": It will not create new file if file not present

# Step-2: Read
# ---------------
for each_line in my_file_handle:
    print("each_line:", each_line)

# Step-3: Disconnect
# ---------------
my_file_handle.close()

print("#"*40, end="\n\n")
#########################################


print("Read Operations: 3) readlines")
print("-"*20)
# ---------------

# Step-1: Connect to file
# ---------------
my_file_handle = open("my_out_file.txt", "r")
# mode "r": Read Only mode
# mode "r": It will not create new file if file not present

# Step-2: Read
# ---------------
file_content = my_file_handle.readlines()
# It will return complete file content in list
print("file_content:", file_content, sep="\n", end="\n\n")

# Step-3: Disconnect
# ---------------
my_file_handle.close()

print("#"*40, end="\n\n")
#########################################


# Different Modes
# ---------------
# mode "w": Write Only, It will create new file, IMPORTANT it will erase file content
# mode "r": Read Only, It will not create new file
# mode 'a': Append Only, It will create new file only if file not present

# mode "w+": Read/Write, It will create new file, IMPORTANT it will erase file content
# mode "r+": Read/Write, It will not create new file
# mode 'a+': Read/Write, It will create new file only if file not present
#########################################