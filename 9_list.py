"""
MUTABLE
list :
    -- We have option to store collection of values like list of names, list of email-ids etc
    -- We can store duplicate values
    -- Automatically index number will be assigned to each value
"""

print("list PART-1")
print("Store the values")
print("--------------")

my_list_1 = [10, 12.4, "python", (100, 200)]
# Internally it will create object of built-in class 'list' and store the values

# We can also use class name
my_list_2 = list((10, 12.4, "python", (100, 200)))

print(my_list_1, my_list_2, sep="\n")

print("############################")


print("list PART-2")
print("Indexes are similar to string")
print("--------------")

my_list = [10, 12.4, "python", (100, 200)]
print("my_list:", my_list, end="\n\n")

print("Course Name:", my_list[2]) # Python
print("2nd character in Course Name:", my_list[2][1], end="\n\n") # y

print("Inside list:", my_list[-1]) # (100, 200)
print("2nd Value in Inside list:", my_list[-1][1]) # 200

print("############################")

print("list PART-3")
print("list of methods")
print("--------------")

print(dir(list))

print("############################")

print("list PART-4")
print("'count' and 'index' methods")
print("--------------")

my_list = [10, 12.4, "python", (100, 200)]
print("my_list:", my_list, end="\n\n")

count_of_python = my_list.count("python")
index_of_python = my_list.index("python")

print("count_of_python:", count_of_python)
print("index_of_python:", index_of_python)

print("############################")