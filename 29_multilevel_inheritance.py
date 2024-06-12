"""
Inheritance:
1) multilevel inheritance
2) multiple inheritance

Here
1) multilevel inheritance
"""

print("1) multilevel inheritance")
print("-"*20)
# ---------------

# Assume this is OLD & Exisiting class
class Salary:
    def add_salary(self, salary):
        self.salary = salary
    def view_salary(self):
        return self.salary

# New Requirement to provide below functionality in salary class
# 1) add tax method
# 2) view tax method
# 3) currently, view_salary() methods returns 'salary' but
#   modify view_salary method to return (salary-tax)


# Employee: sub/child class
# Salary: Super/Parent class
class Employee(Salary):

    # Requirement 1) add tax method
    def add_tax(self, tax):
        self.tax = tax

    # Requirement 2) view tax method
    def view_tax(self):
        return self.tax

    # Requirement 3) currently, view_salary() methods returns 'salary' but
    #   modify view_salary method to return (salary-tax)

    # POLYMORPHISM: We an use same name as super class
    def view_salary(self): # It will OVERRIDE super class view_salary
        # We can access super class method using 2 ways
        # 1-way
        # s = super().view_salary()
        # 2-way
        # s = Salary.view_salary(self)
        return self.salary - self.tax


e1 = Employee()
e1.add_salary(20000)
e1.add_tax(2000)
print("salary:", e1.view_salary())
print("tax:", e1.view_tax())

print("#"*40, end="\n\n")
##################################