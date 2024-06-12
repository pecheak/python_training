"""
How to store values inside object

3-way to store values inside object

In this section, we should get clarity on

1) __new__() method: Constructor
2) __init__() method: Initializer
3) super class 'object' by default all our classes are inherited from 'object' class
"""

print("3-way to store values inside object")
print("-"*20)
# -------------------

# class Employee: # Internally it inherited from 'object' class
# OR
class Employee(object):

    def __init__(self, ename): # Automatically this method is getting called
        self.name = ename

    @classmethod
    def store_company_name(cls, cname):
        cls.company_name = cname

    @classmethod
    def get_company_name(cls):
        return cls.company_name

    def get_employee_name(self):
        return self.name


# create 2 objects
e1 = Employee("emp-1")
e2 = Employee("emp-2")
Employee.store_company_name("XYZ Company") # cls=Employee

print("#"*40, end="\n\n")
###########################################

print("DATA inside objects")
print("-"*20)
# -------------

print("DATA Inside Brand New Class Object 'Employee':", Employee.get_company_name(), sep="\n", end="\n\n")
print("DATA Inside Brand New Instance Object 'e1':", e1.get_employee_name(), sep="\n", end="\n\n")
print("DATA Inside Brand New Instance Object 'e2':", e2.get_employee_name(), sep="\n", end="\n\n")

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