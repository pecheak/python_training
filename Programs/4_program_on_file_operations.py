"""
Read data from server_log.txt

then

extract
IP
PICS

then

Write extrated data to log_report.txt

Expected Output in log_report.txt:
--------------
    IP                  PICS
123.123.123.123     wpaper.gif
123.123.123.123     No Image
123.123.123.123     5star2000.gif
123.123.123.123     5star.gif
123.123.123.123     a2hlogo.jpg
123.123.123.123     No Image
--------------
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




print("Extract Info and Write to file")
print("-"*20)
# ----------------

# Step-1: Connect to file
# ----------------
my_txt_file_handle = open("log_report.txt", "w")

# Step-2: Write
# ----------------
# Write Heading: For Writing: 1) write 2) writelines 3) print-function

# Write Heading 1) write
# my_txt_file_handle.write("IP\tPICS\n")

# Write Heading 2) writelines
heading_in_list = ["IP\t", "PICS\n"]
# my_txt_file_handle.writelines(heading_in_list)

# Write Heading 3) print-function
print("IP", "PICS", sep="\t", file=my_txt_file_handle)

for each_line in file_content_in_list:
    if each_line.startswith("123"):
        sp = each_line.split()
        ip = sp[0]
        raw_img = sp[6] # /pics/wpaper.gif
        if raw_img.startswith("/pics/"):
            img = raw_img[6:]
        else:
            img = "No Image"
        print(ip, img, sep="\t", file=my_txt_file_handle)


# Step-3: Disconnect
# ----------------
my_txt_file_handle.close()

print("""
Created 'log_report.txt', Please Check
""")

print("#"*40, end="\n\n")
#########################################