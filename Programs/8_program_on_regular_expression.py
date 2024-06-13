"""
Get data from server_log.txt
then
extract info using regular expression
"""

print("Read data from server_log.txt")
print("-"*20)
# ----------------

# Step-1: Connect to file
# ----------------
my_log_file_handle = open(r"../log/server_log.txt", "r")

# Step-2: Read
# ----------------
file_content_in_list = my_log_file_handle.readlines()
print(file_content_in_list)

# Step-3: Disconnect
# ----------------
my_log_file_handle.close()

print("#"*40, end="\n\n")
#########################################

print("Check whether it is IP address line or not")
print("-"*20)
# ----------------

import re

for each_line in file_content_in_list:
    match_result = re.match('\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}.*', each_line)
    if match_result is not None:
        print('Each Line:', each_line)
        print("match_result:", match_result, end="\n\n")

# COMMENT
"""
IDENTIFIERS
# --------------
\d -> represents any ONE digit b/n 0 to 9
\D -> represents any ONE non-digit. Except 0 to 9 any character
. -> represents any ONE some character
\. -> strictly DOT
[.] -> strictly DOT
# --------------

# QUANTIFIERS
# --------------
\d{3} -> Internally it will become \d\d\d
\d{1,3} -> Internally it will become (\d|\d\d|\d\d\d)
[0-9]{3} -> [0-9][0-9][0-9]
[0-255] -> It can be any number b/n 0 to 2 OR it can be 5
[0-255252525252525] -> It can be any number b/n 0 to 2 OR it can be 5
[a-z0-9] -> it can be one lower case or one number
[a0x] -> it can be any character in this group
# --------------

# MODIFIERS
# --------------
# * -> 0 or more times
# + -> 1 or more times
# ? -> 0 or 1 time
# --------------
"""

print("#"*40, end="\n\n")
#########################################





print("Extract IP")
print("-"*20)
# ----------------

import re

for each_line in file_content_in_list:
    match_result = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        print(ip)

# COMMENT
"""
- put () IP address pattern so that match() will capture IP address
- This is called GROUP
- Each group will be having number starting from 1
"""

print("#"*40, end="\n\n")
#########################################




print("Extract IP, DATE")
print("-"*20)
# ----------------

import re

for each_line in file_content_in_list:
    match_result = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        print(ip, dt)

# COMMENT
"""

26/Apr/2000

26
--
\d\d # Strictly 2 digits
\d{2} # Strictly 2 digits
[0-9][0-9] # Strictly 2 digits
[0-9]\d # Strictly 2 digits
\d[0-9] # Strictly 2 digits
[0-9]{2} # Strictly 2 digits

\d{1,2} # Minimum one digit, maximum 2 digits
[0-9]{1,2} # Minimum one digit, maximum 2 digits
\d?\d # Minimum one digit, maximum 2 digits
[0-9]?[0-9] # Minimum one digit, maximum 2 digits
\d?[0-9] # Minimum one digit, maximum 2 digits
[0-9]?\d # Minimum one digit, maximum 2 digits
--

Apr
--
[a-zA-Z]{3}
[A-Z][a-z]{2}
(Jan|Feb|Mar)
--

"""

print("#"*40, end="\n\n")
#########################################


print("Extract IP, DATE, PICS")
print("THIS IS PARTIAL OUTPUT-1")
print("-"*20)
# ----------------

import re

for each_line in file_content_in_list:
    match_result = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(\w+\.(gif|jpg)).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(3)
        print(ip, dt, img)

# COMMENT
"""
[0-9A-Za-z_]+
OR
\w+ shorcut for [0-9A-Za-z_]+

\W Excluding [0-9A-Za-z_]
OR
[^0-9A-Za-z_] -> ^ means excluding
"""

print("\nTHIS IS PARTIAL OUTPUT-1\n")

print("#"*40, end="\n\n")
#########################################

print("Extract IP, DATE, PICS")
print("We made * non-greedy just before image pattern")
print("THIS IS PARTIAL OUTPUT-2")
print("-"*20)
# ----------------

import re

for each_line in file_content_in_list:
    match_result = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*?(\w+\.(gif|jpg)).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(3)
        print(ip, dt, img)

# COMMENT
"""

# MODIFIERS
# --------------

# GREEDY
# * -> 0 or more times
# + -> 1 or more times
# ? -> 0 or 1 time
#
#
# NON-GREEDY
# *? -> 0 or more times
# +? -> 1 or more times
# ?? -> 0 or 1 time
#
# --------------
"""

print("\nTHIS IS PARTIAL OUTPUT-2\n")

print("#"*40, end="\n\n")
#########################################

print("Extract IP, DATE, PICS")
print("We made image-name optional")
print("THIS IS PARTIAL OUTPUT-3")
print("-"*20)
# ----------------

import re

for each_line in file_content_in_list:
    match_result = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*?(\w+\.(gif|jpg))?.*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(3)
        print(ip, dt, img)

# COMMENT
"""

"""

print("\nTHIS IS PARTIAL OUTPUT-3\n")

print("#"*40, end="\n\n")
#########################################

print("Extract IP, DATE, PICS")
print('This time we are providing more information')
print("THIS IS FINAL OUTPUT")
print("-"*20)
# ----------------

import re

for each_line in file_content_in_list:
    match_result = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*?(GET|POST|PUT|PATCH|DELETE)\s+/(pics/(\w+\.(gif|jpg)))?.*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(5)
        if img is None:
            img = "No Image"
        print(ip, dt, img)

# COMMENT
"""
\s -> One Space
\S -> any One non-space character

making below pattern OPTIONAL so that, it will consider line
which is having pics and not having pics

(pics/(\w+\.(gif|jpg)))?

"""

print("\nTHIS IS FINAL OUTPUT\n")

print("#"*40, end="\n\n")
#########################################