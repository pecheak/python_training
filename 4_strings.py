"""
Strings
    -- We have option to store collection of characters like name, email-id etc
    -- Automatically index number will be assigned to each character
"""

print("String PART-1")
print("How to store values")
print("---------------")

a = 'PERSON'
# Internally it will create object of 'str' class and store the values

b = str('PERSON')

# print(a, b) # Default is space
print(a, b, sep="\n")

print("##################################\n")

print("String PART-2")
print("How to store values")
print("---------------")

a = 'PERSON'
b = "PERSON'S"
c = '''PERSON'S HEGHT IS XYZ" (" represents inches)'''
d = """PERSON'S HEGHT IS XYZ" (" represents inches)"""
# multi line comments are strings only but not assigned to any variable

print(a, b, c, d, sep="\n")

print("##################################\n")
print("String PART-3")
print("How to store values")
print("---------------")

a = "C:\newfolder\test.py"
# By default \n & \t will get replaced with newline & tab space
print("Value of 'a' is", a)

b = r"C:\newfolder\test.py"
# r -> Raw string, no spacial meaning for character followed by \ like \n\t
print("Value of 'b' in raw format is", b)

c = repr(a) # Convert existing string to RAW string
print("After converting 'a' to RAW String:", c)

print("##################################\n")
print("String PART-4")
print("How to store values")
print("---------------")

x = 10
y = 20
z = x + y

my_string = f"add of {x} & {y} is {z}"
# f - > format -> It replaces {variable_name} with value
print("my_string:", my_string)

print("##################################\n")
print("String PART-5")
print("Indexes: Access each character using index")
print("---------------")

my_string = "WEL COME"
print("my_string:", my_string)

print("0th Character using +ve index no:", my_string[0])
print("0th Character using -ve index no:", my_string[-8])

# Similarly
# print("100th Character using -ve index no:", my_string[100]) # ERROR

print("##################################\n")
print("String PART-6")
print("Slicing: Getting Substring")
print("---------------")

my_string = "WEL COME"
print("my_string:", my_string)

print("Substring from index-1 to 6 using + ve index no:", my_string[1:6])
print("Substring from index-1 to 6 using - ve index no:", my_string[-7:-2], "\n\n")

print("Substring from index-1 to END using + ve index no:", my_string[1:])
print("Substring from index-1 to END using - ve index no:", my_string[-7:], "\n\n")

print("Substring from BEGINNING to 6 using + ve index no:", my_string[:6])
print("Substring from BEGINNING to 6 using - ve index no:", my_string[:-2], "\n\n")

print("Substring from BEGINNING to END using + ve index no:", my_string[:])

print("##################################\n")
print("String PART-7")
print("Step Value: Skip Characters In Between")
print("---------------")

my_string = "WEL COME"
print("my_string:", my_string)

# Refer: 5_strings.xlsx section-2

print("Substring from index-1 to 6, using +ve index no, Default step=1", my_string[1:6])
print("Substring from index-1 to 6, using -ve index no, Default step=1", my_string[-7:-2], "\n\n")
# Step=1: Which means from index-1 to 6 give me every character

print("Substring from index-1 to 6, using +ve index no, step=1", my_string[1:6:1])
print("Substring from index-1 to 6, using -ve index no, step=1", my_string[-7:-2:1], "\n\n")
# Step=1: Which means from index-1 to 6 give me every character

print("Substring from index-1 to 6, using +ve index no, step=2", my_string[1:6:2])
print("Substring from index-1 to 6, using -ve index no, step=2", my_string[-7:-2:2], "\n\n")
# Step=2: Which means from index-1 to 6 give me every 2nd character

print("##################################\n")

print("String PART-8")
print("-ve Step Value: Reverse Order")
print("---------------")

my_string = "WEL COME"
print("my_string:", my_string)

# Refer: 5_strings.xlsx section-3

# Steps for example 6 to 1
# Start index = 6
# end index = 1
# step value = -1 for-reverse, step value is negative
print("Sub string from index-6 to 1 using +ve index, step=-1:", my_string[6:1:-1])
print("Sub string from index-6 to 1 using -ve index, step=-1:", my_string[-2:-7:-1], end="\n\n")
# end="\n\n", at the end put 2 \n\n
#

print("Sub string from index-6 to 1 using +ve index, step=-2:", my_string[6:1:-2])
print("Sub string from index-6 to 1 using -ve index, step=-2:", my_string[-2:-7:-2], end="\n\n")


print("##################################\n")



print("String PART-9")
print("Methods inside 'str' class")
print("---------------")

print(dir(str))

print("##################################\n")

print("String PART-10")
print("Startswith() method")
print("---------------")

my_string = "WEL COME"
print("my_string:", my_string)

result = my_string.startswith("WEL")
print("my_string.startswith() result:", result)

print("##################################\n")