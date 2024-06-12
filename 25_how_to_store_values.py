"""
How to store values inside object

1-way to store values inside object
"""

print("1-way to store values inside object")
print("-"*20)
# -------------------


class Employee:
    pass


# create 2 objects
e1 = Employee()
e2 = Employee()

# Total we have 3 objects here
# CLASS OBJECT: 'Employee' which is automatically getting created
# INSTANCE OBJECTS: 'e1' & 'e2' which we created

# Store data inside all 3 objects
Employee.company_name = "XYZ Company"
e1.name = "emp-1"
e2.name = "emp-2"

print("#"*40, end="\n\n")
###########################################

print("DATA inside objects")
print("-"*20)
# -------------

print("DATA Inside Brand New Class Object 'Employee':", Employee.company_name, sep="\n", end="\n\n")
print("DATA Inside Brand New Instance Object 'e1':", e1.name, sep="\n", end="\n\n")
print("DATA Inside Brand New Instance Object 'e2':", e2.name, sep="\n", end="\n\n")

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

# CLASS OBJECT:  'Employee' is common space for all instance objects
# so data which is comman across all instance objects, we can
# make use of CLASS OBJECT to store the common data

print("Access CLASS OBJECT Data using INSTANCE OBJECTS")
print("-"*20)
# -------------

print("Access Company_name using Class Object 'Employee':", Employee.company_name, sep="\n", end="\n\n")
print("Access Company_name using Instance Object 'e1':", e1.company_name, sep="\n", end="\n\n")
print("Access Company_name using Instance Object 'e2':", e2.company_name, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################################
