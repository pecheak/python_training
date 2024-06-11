"""
"if" conditional statement: Based on the condition we can execute block
of statements.

In some languages, we will use {} to make a block

if some_condition
{
s1
    s2
        s3
    s4
s5
}
s6

in python, we wont use {} to make a block, instead of we will use INDENTATION

if some_condition
    s1
    s2
    s3
    s4
    s5
    if some_condition
        s1
        s2
        s3
        s4
        s5
s6
"""

print("Only using 'if':")
print("----------------")

x = 10
if x == 10 and x > 0 and x < 100:
    print("All conditions are true")

print("#########################\n")

print("Only using 'if':")
print("----------------")

x = 10
if x == 10:
    print("x is equal to 10")
if x > 10:
    print("x is greater than 10")
if x < 10:
    print("x is less than 10")

print("#########################\n")

print("Using 'if-elif':")
print("----------------")

x = 10
if x == 10:
    print("x is equal to 10")
elif x > 10:
    print("x is greater than 10")
elif x < 10:
    print("x is less than 10")

print("#########################\n")

print("Using 'if-elif-else':")
print("----------------")

x = 10
if x == 10:
    print("x is equal to 10")
elif x > 10:
    print("x is greater than 10")
else:
    print("x is less than 10")

print("#########################\n")





print("Using 'if' with string/list/tuple/any-other-collections:")
print("----------------")

my_string = "Python"
print("my_string:", my_string)

my_list = ["C", "Java-1", "python", "Java-2", "Perl"]
print("my_list:", my_list)

if "tho" in my_string:
    print("Substring 'tho' found")

if "Java-1" in my_list:
    print("Course 'Java-1' found")

print("#########################\n")





print("'if' with dictionary")
print("----------------")

my_dictionary = {"course": "python", "duration": 10, "location": "india"}
print("my_dictionary:", my_dictionary, end="\n\n")

# >>> my_dictionary.keys()
# ['course', 'duration', 'location']
# >>>
if "course" in my_dictionary.keys():
    print("Key 'course' found")

# >>> my_dictionary.values()
# ['python', 10, 'india']
if 'python' in my_dictionary.values():
    print("Value 'python' found")

# >>> my_dictionary.items()
# [('course', 'python'), ('duration', 10), ('location', 'india')]
if ('course', 'python') in my_dictionary.items():
    print("Item ('course', 'python') found")

print("#########################\n")