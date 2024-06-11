# 2 Cases
# ---------------
# Case-1: We can end the while-loop in between
# CAse-2: We can skip current iteration in between and go for next iteration
########################################

print("# Case-1: We can end the while-loop in between")
print("-"*20)
# ------------------

my_list = ["C", "Java-1", "python", "Java-2", "Perl"]
print("my_list:", my_list)

# Requirement: Check any value starting with "Java"

index_no = 0
while index_no < len(my_list):
    if my_list[index_no].startswith("Java"):
        print("Course Java Found")
        break
    index_no += 1

# for j in my_list:
#     if j.startswith("Java"):
#         print("Course Java Found")
#         break

print("#"*40, end="\n\n")
########################################






print("# CAse-2: We can skip current iteration in between and go for next iteration")
print("-"*20)
# ------------------

my_list = ["C", "Java-1", "python", "Java-2", "Perl"]
print("my_list:", my_list)


index_no = 0
while index_no < len(my_list):
    if not my_list[index_no].startswith("Java"):
        index_no += 1
        continue
    # Below code needs to be executed only for Java courses,
    # other than java courses are not required
    print("This is Java Course Name is:", my_list[index_no])
    print("This Java course duration 5 days")
    print("This is one version of Java", end="\n\n")
    index_no += 1

# for j in my_list:
#     if not j.startswith("Java"):
#         continue
#     # Below code needs to be executed only for Java courses,
#     # other than java courses are not required
#     print("This is Java Course Name is:", j)
#     print("This Java course duration 5 days")
#     print("This is one version of Java", end="\n\n")


print("#"*40, end="\n\n")
########################################



print("Like if-else and for-else, we have 'while-else'")
print("-"*20)
# ------------------

my_list = ["C", "Java-1", "python", "Java-2", "Perl"]
print("my_list:", my_list)

index_no = 0
while index_no < len(my_list):
    print("Each Value:", my_list[index_no])
    index_no += 1
else:
    print("This is while-else block")
    print("After completing all the iteration, 'else' block will execute")
    print("after completing the for-loop if we want to do some cleanup activity")
    print("We can use this block to do some cleanup activity ")


# for i in my_list:
#     print("Each Value:", i)
# else:
#     print("This is for-else block")
#     print("After completing all the iteration, 'else' block will execute")
#     print("after completing the for-loop if we want to do some cleanup activity")
#     print("We can use this block to do some cleanup activity ")

print("#"*40, end="\n\n")
########################################