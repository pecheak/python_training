"""
Exceptions Handling: When we get error program will terminate abruptly.
which we can handle using Exceptions Handling
"""
#
# print("Without Handling Exceptions")
# print("-"*20)
# # ---------------
#
# a = 10
# b = 0
# c = a/b # Program terminated abruptly here.
# print("c:", c)
#
# print("#"*40, end="\n\n")
# ##################################
#


print("Handling Exceptions using try/except")
print("-"*20)
# ---------------

try:
    a = 10
    b = 0
    c = a / b  # Program WILL NOT TERMINATE, Instead control will pass to except block
    print("c:", c) # This will never execute
except:
    print("Reached Except Block")
    print("We will write code here to take care of error occurred in try")

print("#"*40, end="\n\n")
##################################





print("try/except with exception classes")
print("-"*20)
# ---------------

# Exception Classes:
# - We need to have classes for each error
# - We have few classes present in builtins
# - We can write our own exception classes
# - 'Exception' is super class for all exception classes

try:
    a = 10
    b = 0
    c = a / xyz  # Program WILL NOT TERMINATE, Instead control will pass to except block
    print("c:", c) # This will never execute
except ZeroDivisionError: # This is one way to mention class name
    print("This is ZDE ")
except NameError as ne: # This is other way to mention class name
    print("This is NE and ne is:", ne)

print("#"*40, end="\n\n")
##################################


print("try/except/else")
print("-"*20)
# ---------------

# OPTION-1: Where any statement is giving error then it will to same except block
try:
    my_file_handle = open("x:/xyz/asda.txt", "r")
    file_content = my_file_handle.read()
    my_file_handle.close()
except Exception as e: # Exception class is super class, it can receive any error
    print("Some Error in Try:", e)


# OPTION-2: Only file related error we are handling in except block
#   so we takenout remaining part of the code and put it in else block
try:
    my_file_handle = open("x:/xyz/asda.txt", "r")
except Exception as e: # Exception class is super class, it can receive any error
    print("Some Error in Try:", e)
else:
    try:
        file_content = my_file_handle.read()
        my_file_handle.close()
    except:
        print("Some in else block code as well")

# If try success then skip 'except' and execute 'else'
# If try failed then skip 'else' and execute 'except'

print("#"*40, end="\n\n")
##################################





print("try/except/else/finally")
print("-"*20)
# ---------------

try:
    my_file_handle = open("temp.txt", "w")
except Exception as e:
    print("Except Block for File Open Releated error")
else:
    print("Reached else block")
    my_file_handle.write("Hello")
finally:
    print("Reached finally block")
    my_file_handle.close()

# finally block
# - If try success/failed, but finally block will execute
# - If except success/failed, but finally block will execute
# - If else success/failed, but finally block will execute

print("#"*40, end="\n\n")
##################################



print("About 'assert' statement")
print("-"*20)
# ---------------

a = 10
assert a == 10
# This will throw error "AssertionError" if condition false

print("#"*40, end="\n\n")
##################################


print("We can handle Assertion Error As well")
print("-"*20)
# ---------------

try:
    a = 10
    assert a > 10
    # This will throw error "AssertionError" if condition false
except AssertionError:
    print("This is Assertion Error")

print("#"*40, end="\n\n")
##################################




print("User Defined Exception Class Example-1")
print("-"*20)
# ---------------

# Minimum Requirement: Our class should be sub-class of 'Exception' class

class MyError(Exception):
    pass # Even though it is empty class, it is valid exception class

# raise: We can manually throw error

try:
    a = 10
    if a == 10:
        raise MyError
    if a > 10:
        raise MyError
    if a < 10:
        raise NameError
except MyError:
    print("In Except: It is MyError")

print("#"*40, end="\n\n")
##################################

print("User Defined Exception Class Example-2")
print("-"*20)
# ---------------

# Requirement: Pass some message while raising exception

class MyError(Exception):
    def __init__(self, msg):
        self.error_message = msg

try:
    a = 10
    if a == 10:
        raise MyError("Here value of a is 10")
    if a > 10:
        raise MyError("Here value of a is gt 10")
    if a < 10:
        raise MyError("Here value of a is lt 10")

except MyError as me:
    print("In Except: It is MyError and message is:", me.error_message)

print("#"*40, end="\n\n")
##################################