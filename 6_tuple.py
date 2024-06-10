"""
IMMUTABLE
tuple :
    -- We have option to store collection of values like list of names, list of email-ids etc
    -- We can store duplicate values
    -- Automatically index number will be assigned to each value
"""

print("Tuple PART-1")
print("Store the values")
print("--------------")

my_tuple_1 = (10, 12.4, "python", (100, 200))
# Internally it will create object of built-in class 'tuple' and store the values

# We can also use class name
my_tuple_2 = tuple((10, 12.4, "python", (100, 200)))

print(my_tuple_1, my_tuple_2, sep="\n")

print("############################")


print("Tuple PART-2")
print("Indexes are similar to string")
print("--------------")

my_tuple = (10, 12.4, "python", (100, 200))
print("my_tuple:", my_tuple, end="\n\n")

print("Course Name:", my_tuple[2]) # Python
print("2nd character in Course Name:", my_tuple[2][1], end="\n\n") # y

print("Inside Tuple:", my_tuple[-1]) # (100, 200)
print("2nd Value in Inside Tuple:", my_tuple[-1][1]) # 200

print("############################")

print("Tuple PART-3")
print("list of methods")
print("--------------")

print(dir(tuple))

print("############################")


print("Tuple PART-4")
print("'count' and 'index' methods")
print("--------------")

my_tuple = (10, 12.4, "python", (100, 200))
print("my_tuple:", my_tuple, end="\n\n")

count_of_python = my_tuple.count("python")
index_of_python = my_tuple.index("python")

print("count_of_python:", count_of_python)
print("index_of_python:", index_of_python)

print("############################")