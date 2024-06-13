"""
Operator Overloading:

We can provide implementation to each operator like +, - etc
in our class as well like int, str classes

In python for each operator there is system defined name
Example:
    + = __add__
    - = __sub__

If we want to support for any operator then we need to write method
using system defined name given to that operator
Example:
    if we want to support + then we need to write method __add__

"""

print("Supported + operator")
print("-"*20)
# ---------------


class Employee:
    def __init__(self, ename):
        self.ename = ename

    def __add__(self, other): # self=e1, other=e2
        concat_result = e1.ename + other.ename
        return concat_result

e1 = Employee("emp-1")
e2 = Employee("emp-2")

# Support + to concatinate both the names
add_result = e1 + e2 # Internally e1.__add__(e2)
print("add_result:", add_result)

print("#"*40, end="\n\n")
##################################




print("Supported Iteration")
print("-"*20)
# ---------------


class Employee:
    def __init__(self, ename):
        self.ename = ename

    def __add__(self, other): # self=e1, other=e2
        concat_result = self.ename + other.ename
        return concat_result

    def __iter__(self):
        self.start_index = 0
        return self

    def __next__(self):
        current_index = self.start_index
        if current_index < len(self.ename):
            self.start_index = self.start_index + 1
            return self.ename[current_index]
        else:
            raise StopIteration


e1 = Employee("emp-1")
e2 = Employee("emp-2")

# Support + to concatinate both the names
add_result = e1 + e2 # Internally e1.__add__(e2)
print("add_result:", add_result)

# To support Iteration, we need to implement 2 methods
# 1) __iter__() # This will be called 1st time, before starting iteration
# 2) __next__() # This will be called in every iteration

for i in e1:
    print("i:", i)
# Expected Output
# e
# m
# p
# -
# 1

for j in e2:
    print("j:", j)

# Expected Output
# e
# m
# p
# -
# 2

print("#"*40, end="\n\n")
##################################