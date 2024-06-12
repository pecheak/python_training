"""
Here 2nd way to pass values

2-way is we can pass values using key=value format
"""

print("Function with keyword or named arguments")
print("-"*20)
# --------------


# name & company are called keyword or named arguments
# * is just syntax, It tells this is keyword/named argument function
# We are not passing any values to *
def employee(*, name, company):
    print("Name:", name)
    print("Company:", company)
    return [name, company]


received_value = employee(name="emp-1", company="comp-1")
print("received_value:", received_value, end="\n\n")

received_value = employee(company="comp-1", name="emp-2")
print("received_value:", received_value, end="\n\n")

received_value = employee(name="emp-3", company="comp-2")
print("received_value:", received_value, end="\n\n")

print("#"*40, end="\n\n")
###################################




print("Function with variable keyword or named arguments")
print("-"*20)
# --------------

# **prev_companies are variable keyword or named arguments
def employee(*, name, company, **prev_companies):
    print("Name:", name)
    print("Company:", company)
    print("Prev_companies:", prev_companies)
    return [name, company, prev_companies]


received_value = employee(name="emp-1", company="comp-1")
# prev_companies = {}
print("received_value:", received_value, end="\n\n")

received_value = employee(name="emp-2", company="comp-1")
# prev_companies = {}
print("received_value:", received_value, end="\n\n")

received_value = employee(name="emp-3", company="comp-2")
# prev_companies = {}
print("received_value:", received_value, end="\n\n")

received_value = employee(name="emp-4", company="comp-2", pc1="my_prev_comp_1")
# prev_companies = {pc1: "my_prev_comp_1"}
print("received_value:", received_value, end="\n\n")

received_value = employee(name="emp-5", company="comp-2", pc1="my_prev_comp_1", pc2="my_prev_comp_2")
# prev_companies = {pc1="my_prev_comp_1", pc2="my_prev_comp_2"}
print("received_value:", received_value, end="\n\n")

print("#"*40, end="\n\n")
###################################
