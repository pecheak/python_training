"""
How to get or create objects
- Using class we can get or create objects

In this section, we should get 100% clarity on
1) CLASS OBJECT
2) INSTANCE OBJECTS
"""

print("How to get or create objects")
print("-"*20)
# -------------------


class Employee:
    pass

# pass : It is dummpy keyword
#       - To keep any block empty, we can make use of it
#       - Eventhough it is empty class it is valid class


# create 2 objects
e1 = Employee()
e2 = Employee()

# Total we have 3 objects here
# CLASS OBJECT: 'Employee' which is automatically getting created
# INSTANCE OBJECTS: 'e1' & 'e2' which we created

print("#"*40, end="\n\n")
###########################################

print("DATA inside objects")
print("-"*20)
# -------------

print("DATA Inside Brand New Class Object 'Employee':", Employee, sep="\n", end="\n\n")
print("DATA Inside Brand New Instance Object 'e1':", e1, sep="\n", end="\n\n")
print("DATA Inside Brand New Instance Object 'e2':", e2, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################################

print("METHODS inside objects")
print("-"*20)
# -------------

print("METHODS Inside Brand New Class Object 'Employee':", dir(Employee), sep="\n", end="\n\n")
print("METHODS Inside Brand New Instance Object 'e1':", dir(e1), sep="\n", end="\n\n")
print("METHODS Inside Brand New Instance Object 'e2':", dir(e2), sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################################


