"""
How to store values inside object

2-way to store values inside object
"""

print("2-way to store values inside object")
print("-"*20)
# -------------------


class Employee:
    @classmethod
    def store_company_name(cls, cname):
        cls.company_name = cname

    @classmethod
    def get_company_name(cls):
        return cls.company_name

    def store_employee_name(self, ename):
        self.name = ename

    def get_employee_name(self):
        return self.name


# create 2 objects
e1 = Employee()
e2 = Employee()


# Store data inside all 3 objects
Employee.store_company_name("XYZ Company") # cls=Employee

#e1.store_company_name("XYZ Company") #
# Here @classmethod will make sure to pass cls=Employee
#   eventhough we are calling using 'e1'

e1.store_employee_name("emp-1") # self=e1
e2.store_employee_name("emp-2") # self=e2
# Employee.store_employee_name("emp-3")

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