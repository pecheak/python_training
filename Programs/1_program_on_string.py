"""
From the string given below,
Extract
IP
PICS

Expected Output:
--------------
123.123.123.123
wpaper.gif
--------------
"""

print("List of builtin functions")
print("--------------")

print(dir(__builtins__))

print("###########################")


print("input_data")
print("--------------")

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(input_data)
print(repr(input_data))
print(type(input_data))

print("###########################")


print("Extract IP: 1-WAY: WON'T WORK for all cases")
print("--------------")

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
ip = input_data[0:15]
print(ip)

print("###########################")


print("Extract IP: 2-WAY")
print("--------------")

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

start_index = 0
end_index = input_data.index(" ")
ip = input_data[0:end_index]
print(ip)

# >>> # About 'index' method
# >>> # Example-1
# >>> s= "WEL COME"
# >>> s.index("E")
# 1
# >>> # Example-2
# >>> s.index("E", 3) # Start looking from index-3 onwards
# 7
# >>> # Example-3
# >>> s.index("COME")
# 4
# >>>

print("###########################")

print("Extract IP: 3-WAY")
print("--------------")

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

sp= input_data.split()
print("Splitted Values: ", sp, end="\n\n")

ip = sp[0]
print("ip:", ip)

# >>> # About 'split' method
# >>> s= "WEL COME"
# Example-1
# >>> s.split()
# ['WEL', 'COME']
# >>>
# >>> # Example-2
# >>> s.split("E")
# ['W', 'L COM', '']
# >>>

print("###########################")





print("Extract PICS: 1-WAY")
print("--------------")

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

start_index = input_data.index("/pics/") # It will return index 1st "/"
start_index = start_index + 6

# 1-way
# end_index = input_data.index("HTTP") # It will return index of H
# end_index = end_index - 1 # Index of space after gif

# 2-way
end_index = input_data.index(" ", start_index)

img = input_data[start_index:end_index]
print(img)

print("###########################")

print("Extract PICS: 2-WAY")
print("--------------")

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

sp= input_data.split()
print("Splitted Values: ", sp, end="\n\n")

raw_img = sp[6] # '/pics/wpaper.gif'

# 1-way: Remove '/pics/' from '/pics/wpaper.gif'
img_1 = raw_img[6:]

# 2-way: Remove '/pics/' from '/pics/wpaper.gif'
raw_img_sp = raw_img.split("/") #
# print(raw_img_sp) # ['', 'pics', 'wpaper.gif']
img_2 = raw_img_sp[2] # Using +ve index no
img_3 = raw_img_sp[-1] # Using -ve index no

print(img_1, img_2, img_3, sep="\n")

print("###########################")