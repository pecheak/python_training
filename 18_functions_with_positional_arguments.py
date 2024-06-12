"""
Case-2: How to pass values to variables present inside the function

2 ways to pass values
1-way is we can pass only values
2-way is we can pass values using key=value format

In this section, we will discuss
1-way is we can pass only values
"""

print("Function with positional arguments")
print("-"*20)
# --------------


# name & company are called positional arguments
def employee(name, company):
    print("Name:", name)
    print("Company:", company)
    return [name, company]


received_value = employee("emp-1", "comp-1")
print("received_value:", received_value, end="\n\n")

received_value = employee("emp-2", "comp-1")
print("received_value:", received_value, end="\n\n")

received_value = employee("emp-3", "comp-2")
print("received_value:", received_value, end="\n\n")

print("#"*40, end="\n\n")
###################################



print("Function with variable positional arguments")
print("-"*20)
# --------------


# *prev_companies called variable positional arguments
# name & company are called positional arguments
def employee(name, company, *prev_companies):
    print("Name:", name)
    print("Company:", company)
    print("Prev_companies:", prev_companies)
    return [name, company, prev_companies]


received_value = employee("emp-1", "comp-1")
# prev_companies = ()
print("received_value:", received_value, end="\n\n")

received_value = employee("emp-2", "comp-1")
# prev_companies = ()
print("received_value:", received_value, end="\n\n")

received_value = employee("emp-3", "comp-2")
# prev_companies = ()
print("received_value:", received_value, end="\n\n")

received_value = employee("emp-4", "comp-2", "my_prev_comp_1")
# prev_companies = ("my_prev_comp_1", )
print("received_value:", received_value, end="\n\n")

received_value = employee("emp-5", "comp-2", "my_prev_comp_1", "my_prev_comp_2")
# prev_companies = ("my_prev_comp_1", "my_prev_comp_2")
print("received_value:", received_value, end="\n\n")

print("#"*40, end="\n\n")
###################################