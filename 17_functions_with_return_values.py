"""
2 Cases
Case-1: How to access values outside the function
Case-2: How to pass values to variables present inside the function

In this section, we will discuss on
Case-1: How to access values outside the function
"""

print("Function with 1 return value")
print("-"*20)
# ----------------

# 2 steps to access values outside the function
# step-1: Inside function use 'return' statement to mention variables
# step-2: Assign function call to some variable to store the returned value

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    # step-1: Inside function use 'return' statement to mention variables
    return name

# step-2: Assign function call to some variable to store the returned value
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
######################################

print("Function with more than 1 return value: In Tuple")
print("-"*20)
# ----------------

# 2 steps to access values outside the function
# step-1: Inside function use 'return' statement to mention variables
# step-2: Assign function call to some variable to store the returned value

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    # step-1: Inside function use 'return' statement to mention variables
    return name, company # it will return in tuple

# step-2: Assign function call to some variable to store the returned value
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
######################################

print("Function with more than 1 return value: In List")
print("-"*20)
# ----------------

# 2 steps to access values outside the function
# step-1: Inside function use 'return' statement to mention variables
# step-2: Assign function call to some variable to store the returned value

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    # step-1: Inside function use 'return' statement to mention variables
    return [name, company]

# step-2: Assign function call to some variable to store the returned value
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
######################################

print("Function with more than 1 return value: In Dictionary")
print("-"*20)
# ----------------

# 2 steps to access values outside the function
# step-1: Inside function use 'return' statement to mention variables
# step-2: Assign function call to some variable to store the returned value

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    # step-1: Inside function use 'return' statement to mention variables
    return {"name": name, "company": company}

# step-2: Assign function call to some variable to store the returned value
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
######################################