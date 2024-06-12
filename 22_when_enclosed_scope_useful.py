"""
When we can make use of Enclosed Scope Variable
"""

print("Using Global Variable To Trace Total Log Files Processed")
print("-"*20)
# ------------------

# Total log processed = total txt files processed + total csv file processed

total_log_processd = 0

def txt_log_process_function():
    global total_log_processd
    total_log_processd = total_log_processd + 1


def csv_log_process_function():
    global total_log_processd
    total_log_processd = total_log_processd + 1

txt_log_process_function()
txt_log_process_function()
csv_log_process_function()
csv_log_process_function()

print("total_log_processd:", total_log_processd)

print("#"*40, end="\n\n")
#####################################




print("Using Enclosed Scope Variable To Trace Total Log Files Processed")
print("-"*20)
# ------------------

def log_process_function():

    total_log_processd = 0

    def txt_log_process_function():
        nonlocal total_log_processd
        total_log_processd = total_log_processd + 1

    def csv_log_process_function():
        nonlocal total_log_processd
        total_log_processd = total_log_processd + 1

    def get_total_log_files_processed():
        return total_log_processd

    return [txt_log_process_function, csv_log_process_function, get_total_log_files_processed]


received_functions = log_process_function()
# received_functions = [txt_log_process_function, csv_log_process_function, get_total_log_files_processed]

# received_functions[0] = txt_log_process_function
received_functions[0]()
received_functions[0]()
received_functions[0]()

# received_functions[1] = csv_log_process_function
received_functions[1]()
received_functions[1]()
received_functions[1]()

# received_functions[2] = get_total_log_files_processed function
count = received_functions[2]()
print("Total Logs Processed:", count)

print("#"*40, end="\n\n")
#####################################