"""
Webscraping using beautifulsoup library

Finally get log data
"""
print("Get data from website")
print("-"*20)
# -------------

import urllib.request as u

my_web_file_handle = u.urlopen("https://www.jafsoft.com/searchengines/log_sample.html")
web_content = my_web_file_handle.read()
my_web_file_handle.close()

print(web_content)

print("#"*40, end="\n\n")
#####################################

print("Create object of BeautifulSoup class")
print("-"*20)
# ------------

from bs4 import BeautifulSoup
soup = BeautifulSoup(web_content, "html.parser")
print(soup)

print("#"*40, end="\n\n")
#####################################





print("Head Tag")
print("-"*20)
# ------------
# x = soup.head
print(soup.head)

print("#"*40, end="\n\n")
#####################################

print("Body Tag")
print("-"*20)
# ------------

print(soup.body)

print("#"*40, end="\n\n")
#####################################





print("log data tag")
print("-"*20)
# ------------

print(soup.body.pre)

print("#"*40, end="\n\n")
#####################################

print("log data in string")
print("-"*20)
# ------------

log_data = soup.body.pre.text
print(log_data)

print("#"*40, end="\n\n")
#####################################

print("type of log data")
print("-"*20)
# ------------

log_data = soup.body.pre.text
print(type(log_data))

print("#"*40, end="\n\n")
#####################################

print("log data in raw format")
print("-"*20)
# ------------

log_data = soup.body.pre.text
print(repr(log_data))

print("#"*40, end="\n\n")
#####################################

print("list of lines")
print("-"*20)
# ------------

list_of_lines = log_data.splitlines()
print(list_of_lines)

print("#"*40, end="\n\n")
#####################################




print("Extract Info and Write to file")
print("-"*20)
# ----------------

# ----------------
my_txt_file_handle = open("web_report.txt", "w")
print("IP", "PICS", sep="\t", file=my_txt_file_handle)

for each_line in list_of_lines:
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
Created 'web_report.txt', Please Check
""")

print("#"*40, end="\n\n")
#########################################