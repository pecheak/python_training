"""
multiple inheritance
"""

print("multiple inheritance")
print("-"*20)
# ---------------

# Assume this is OLD & Exisiting class
class Salary:
    def add_salary(self, salary):
        self.salary = salary
    def view_salary(self):
        return self.salary

# Assume this is OLD & Exisiting class
class Tax:
    def add_tax(self, tax):
        self.tax = tax
    def view_tax(self):
        return self.tax

# Client Requirement:
# Write class which is having
#   1) add/view salary
#   2) add/view tax
#   3) add/view name

class Employee(Salary, Tax):
    def add_name(self, ename):
        self.ename = ename
    def view_name(self):
        return self.ename


e1 = Employee()
e1.add_salary(20000)
e1.add_tax(2000)
e1.add_name("emp-1")

print("Salary:", e1.view_salary())
print("Tax:", e1.view_tax())
print("Name:", e1.view_name())

print("#"*40, end="\n\n")
##################################