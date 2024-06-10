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