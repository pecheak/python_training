"""
Variable Scopes
1) Local Scope
2) Enclosed Scope
3) Global Scope
4) builtins
"""

print("1) Local Scope:")
print("-"*20)
# ------------

def f():
    a = 100 # Local Scope, We can't access outside the function
    print("Inside Func, value of a is: ", a)

f()
# print("Value of a:", a) # WE CAN'T ACCESS HERE

print("#"*40, end="\n\n")
#########################



print("2) Global Scope:")
print("-"*20)
# ------------

x = 100 # Global scope, we can access anywhere in the program
def f():
    print("Inside f() global x is :", x) # We can access
f()
print("Value of x in global:", x)

print("#"*40, end="\n\n")
#########################




print("2) Global Scope: Change global variable value inside function")
print("-"*20)
# ------------


x = 100
def f():
    # x = 10 # It will create local variable
    global x
    x = 1000 # Change value of global variable
    print("Inside f() global x is :", x) # 1000

f()
print("Value of x in global:", x) # 1000

print("#"*40, end="\n\n")
#########################




print("3) Enclosed Scope Example-1:")
print("-"*20)
# ------------

def outer_function():
    c = 100
    # Enclosed Scope: Which means, current function & inner function can access
    def inner_function():
        print("In Innerfunction value of c is:", c)
    inner_function()

outer_function()


print("#"*40, end="\n\n")
#########################



print("3) Enclosed Scope Example-2: ")
print("Change outer function variable inside inner function")
print("-"*20)
# ------------

def outer_function():
    c = 100 # Enclosed Scope Variable
    def inner_function():
        # c = 1000 # It will create local variable
        nonlocal c # refers enclosed scope variable
        c = 1000
        print("In Innerfunction value of c is:", c)
    inner_function()
    print("In outer function value of c is:", c)

outer_function()

print("#"*40, end="\n\n")
#########################




# Check for variables/names
# ------------
# 1st check in Local Scope
# If Not Found
# then
# check in Enclosed Scope
# If Not Found
# then
# Check in Global scope
# If Not Found
# then
# check in 'builtins'
# If Not Found
# then
# throw error
#########################