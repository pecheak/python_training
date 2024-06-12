"""
Using Decorator Design Pattern
"""

print("Without Using Decorator: We are repeating code in all functions")
print("-"*20)
# -----------------


def add(a, b):
    print("Result is:")
    print(a + b)
    print("End of the result")


def sub(a, b):
    print("Result is:")
    print(a - b)
    print("End of the result")


add(10, 20)
sub(10, 20)


print("#"*40, end="\n\n")
##################################

# Here in add() & sub() function we have few-statements/code are common
# which we need to reuse

print("Our Common Function: WRONG DESIGN: IT WILL NOT WORK")
print("-"*20)
# -----------------

def my_common_func(): # WRONG DESIGN
    print("Result is:")
    print("End of the result")

def add(a, b):
    my_common_func() # WRONG
    print(a + b)
    my_common_func() # WRONG


def sub(a, b):
    my_common_func()
    print(a - b)
    my_common_func()


add(10, 20)
sub(10, 20)

print("THIS IS WRONG DESIGN")

print("#"*40, end="\n\n")
##################################



print("PARTIAL IMPLEMENTATION")
print("Function as per Decorator Design Pattern")
print("for reusing common functionality")
print("-"*20)
# -----------------


# Function as per Decorator Design Pattern
def my_decorator(my_func):
    def decorated_func(x, y): # This can be used for 2 argument functions
        print("Result Is:")
        my_func(x,y)
        print("End Of The Result")
    return decorated_func


# -----------------
# Function-1: add
###################
def my_decorator(my_func):  # my_func = add
    def decorated_func(x, y): # x = 10, y = 20
        print("Result Is:")
        my_func(x,y) # add(10,20)
        print("End Of The Result")
    return decorated_func

def add(a,b):
    print(a + b)

inner_func = my_decorator(add)
# inner_func = decorated_func
# inner_func having reference to decorated_func
inner_func(10, 20)
###################

# -----------------
# Function-2: sub
###################
def my_decorator(my_func): # my_func = sub
    def decorated_func(x, y): # x=10, y=20
        print("Result Is:")
        my_func(x,y) # sub(10,20)
        print("End Of The Result")
    return decorated_func


def sub(a,b):
    print(a - b)

inner_func = my_decorator(sub)
inner_func(10,20)
###################

print("PARTIALLY IMPLEMENTED HERE, Check below block for FINAL DECORATOR")

print("#"*40, end="\n\n")
##################################





print("FINAL and CORRECT IMPLEMENTATION")
print("-"*20)
# -----------------


# Decorator
def my_decorator(my_func):
    def decorated_func(x, y): # This can be used for 2 argument functions
        print("Result Is:")
        my_func(x,y)
        print("End Of The Result")
    return decorated_func


# -----------------
# Function-1: add
###################
@my_decorator
def add(a,b):
    print(a + b)

add(10,20)

# @my_decorator will take care of below 2 steps
# inner_func = my_decorator(add)
# inner_func(10, 20)
###################

# -----------------
# Function-2: sub
###################
@my_decorator
def sub(a,b):
    print(a - b)

sub(10, 20)

# @my_decorator will take care of below 2 steps
# inner_func = my_decorator(sub)
# inner_func(10,20)
###################


print("FINAL and CORRECT IMPLEMENTATION")
print("#"*40, end="\n\n")
##################################





print("FINAL and CORRECT IMPLEMENTATION")
print("-"*20)
# -----------------


# Decorator
def my_decorator(my_func):
    def decorated_func(x, y): # This can be used for 2 argument functions
        print("Result Is:")
        my_func(x,y)
        print("End Of The Result")
    return decorated_func


# -----------------
# Function-1: add
###################
@my_decorator
def add(a,b):
    print(a + b)

add(10,20)

# @my_decorator will take care of below 2 steps
# inner_func = my_decorator(add)
# inner_func(10, 20)
###################

# -----------------
# Function-2: sub
###################
@my_decorator
def sub(a,b):
    print(a - b)

sub(10, 20)

# @my_decorator will take care of below 2 steps
# inner_func = my_decorator(sub)
# inner_func(10,20)
###################


print("FINAL and CORRECT IMPLEMENTATION")
print("#"*40, end="\n\n")
##################################
:white_check_mark:
11

12:44
21_variable_scopes.py
12:47
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



