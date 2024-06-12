"""
Write function to receive log_file_path as an argument,
let the function extract information and return extracted
information in list of tuples where each tuple is each row data

Expected return Value:
--------------
[
(123.123.123.123     wpaper.gif),
(123.123.123.123     No Image),
(123.123.123.123     5star2000.gif),
(123.123.123.123     5star.gif),
(123.123.123.123     a2hlogo.jpg),
(123.123.123.123     No Image)
]
--------------

"""

print("Function to Extract Info")
print("-"*20)
# ---------------


def log_process_function_pos_args(log_file_path):
    my_log_file_handle = open(log_file_path, "r")
    log_file_content = my_log_file_handle.readlines()
    my_log_file_handle.close()
    extracted_info = []
    for each_line in log_file_content:
        if each_line.startswith("123"):
            sp = each_line.split()
            ip = sp[0]
            raw_img = sp[6]  # /pics/wpaper.gif
            if raw_img.startswith("/pics/"):
                img = raw_img[6:]
            else:
                img = "No Image"
            each_line_tuple = (ip, img)
            extracted_info.append(each_line_tuple)
    return extracted_info


def log_process_function_kw_args(*, log_file_path):
    my_log_file_handle = open(log_file_path, "r")
    log_file_content = my_log_file_handle.readlines()
    my_log_file_handle.close()
    extracted_info = []
    for each_line in log_file_content:
        if each_line.startswith("123"):
            sp = each_line.split()
            ip = sp[0]
            raw_img = sp[6]  # /pics/wpaper.gif
            if raw_img.startswith("/pics/"):
                img = raw_img[6:]
            else:
                img = "No Image"
            each_line_tuple = (ip, img)
            extracted_info.append(each_line_tuple)
    return extracted_info


pos_arg_func_result = log_process_function_pos_args(r"../log/server_log.txt")
kw_arg_func_result = log_process_function_kw_args(log_file_path=r"../log/server_log.txt")

print("pos_arg_func_result:", pos_arg_func_result)
print("kw_arg_func_result:", kw_arg_func_result)

print("#"*40, end="\n\n")
#################################




print('Write to file')
print("-"*20)
# ---------------

my_out_file_handle = open("func_report.txt", "w")
print("IP", "PICS", sep="\t", file=my_out_file_handle)

# Data is
# pos_arg_func_result: [('123.123.123.123', 'wpaper.gif'), ('123.123.123.123', 'No Image'), ('123.123.123.123', '5star2000.gif'), ('123.123.123.123', '5star.gif'), ('123.123.123.123', 'a2hlogo.jpg'), ('123.123.123.123', 'No Image')]
# for each_value in pos_arg_func_result:
#     print(each_value[0], each_value[1], sep="\t", file=my_out_file_handle)

# OR

# Data is
# pos_arg_func_result: [('123.123.123.123', 'wpaper.gif'), ('123.123.123.123', 'No Image'), ('123.123.123.123', '5star2000.gif'), ('123.123.123.123', '5star.gif'), ('123.123.123.123', 'a2hlogo.jpg'), ('123.123.123.123', 'No Image')]
for i, j in pos_arg_func_result:
    print(i, j, sep="\t", file=my_out_file_handle)

my_out_file_handle.close()

print("""
created "func_report.txt", Please check
""")

print("#"*40, end="\n\n")
#################################
