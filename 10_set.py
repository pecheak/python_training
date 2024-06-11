"""
MUTABLE
- set:
    -- We have option to store collection of values like list of names, list of email-ids etc
    -- We can store unique values
    -- No Index
    -- unordered: Values order will change

"""

print("set PART-1")
print("----------------")

my_set_1 = {10, 10, 10, "python", "python", "java", "java"}
print(my_set_1)

my_set_2 = set([10, 10, 10, "python", "python", "java", "java"])
print(my_set_2)

print("###################################\n")

print("set PART-2")
print("Methods inside set")
print("----------------")

print(dir(set))

print("###################################\n")

print("set PART-3")
print("'union' method")
print("----------------")

my_set_1 = set(["python", "Java"])
my_set_2 = set(["python", "Java", "c++", "c"])
print("my_set_1:", my_set_1)
print("my_set_2:", my_set_2)

my_set_3 = my_set_1.union(my_set_2)
print("Union Result:", my_set_3)

print("###################################\n")