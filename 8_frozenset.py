"""
- frozenset:
    -- We have option to store collection of values like list of names, list of email-ids etc
    -- We can store unique values
    -- No Index
    -- unordered: Values order will change

"""

print("frozenset PART-1")
print("----------------")

my_frozenset_1 = frozenset([10, 10, 10, "python", "python", "java", "java"])
print(my_frozenset_1)

print("###################################\n")


print("frozenset PART-2")
print("Methods inside frozenset")
print("----------------")

print(dir(frozenset))

print("###################################\n")

print("frozenset PART-3")
print("'union' method")
print("----------------")

my_frozenset_1 = frozenset(["python", "Java"])
my_frozenset_2 = frozenset(["python", "Java", "c++", "c"])
print("my_frozenset_1:", my_frozenset_1)
print("my_frozenset_2:", my_frozenset_2)

my_frozenset_3 = my_frozenset_1.union(my_frozenset_2)
print("Union Result:", my_frozenset_3)

print("###################################\n")