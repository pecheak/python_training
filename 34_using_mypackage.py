"""
Packages:
We can keep/organize modules in folders/sub-folders.
These folders are called PACKAGES
"""

print("1-way to import")
print("-"*20)
# ---------------

import mypackage.db.mymodule

print("course:", mypackage.db.mymodule.course)

add_result = mypackage.db.mymodule.add(10, 20)
print("add_result:", add_result)

e1 = mypackage.db.mymodule.Employee()
e1.add_name("emp-1")
print("Name:", e1.view_name())

print("#"*40, end="\n\n")
##################################

print("2-way to import")
print("-"*20)
# ---------------

import mypackage.db.mymodule as mm

print("course:", mm.course)

add_result = mm.add(10, 20)
print("add_result:", add_result)

e1 = mm.Employee()
e1.add_name("emp-1")
print("Name:", e1.view_name())

print("#"*40, end="\n\n")
##################################


print("3-way to import")
print("-"*20)
# ---------------

# We can import whichever we want
# No Need to prefix module name to access

from mypackage.db.mymodule import course, add, Employee

print("course:", course)

add_result = add(10, 20)
print("add_result:", add_result)

e1 = Employee()
e1.add_name("emp-1")
print("Name:", e1.view_name())

print("#"*40, end="\n\n")
##################################

print("4-way to import")
print("-"*20)
# ---------------

# We can import whichever we want
# No Need to prefix module name to access

from mypackage.db.mymodule import course as c, add as a, Employee as E

print("course:", c)

add_result = a(10, 20)
print("add_result:", add_result)

e1 = E()
e1.add_name("emp-1")
print("Name:", e1.view_name())

print("#"*40, end="\n\n")
##################################