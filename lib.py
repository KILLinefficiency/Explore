from os import system
from platform import system as platform

# The awesome Explore Splash.
def explore_splash():
    splash = r"""
  ______                     _                          
 |  ____|                   | |                         
 | |__     __  __   _ __    | |    ___     _ __     ___ 
 |  __|    \ \/ /  | '_ \   | |   / _ \   | '__|   / _ \
 | |____    >  <   | |_) |  | |  | (_) |  | |     |  __/
 |______|  /_/\_\  | .__/   |_|   \___/   |_|      \___|
                   | |                                  
                   |_|                                  
    """
    print(splash)


"""
delete_item() deletes an item in the mess.
It takes the location of the item as a parameter.
Since the mess starts with item index: 1, delete_item() deletes
the item at (index - 1) location.
"""
def delete_item(array, index):
    del array[index - 1]


def trim_n(array):
    clean_array = []
    for trim in range(0, len(array)):
        if array[trim][-1] == "\n":
            clean_array.append(array[trim][0:-1])
        else:
            clean_array,append(array[trim])
    return clean_array

"""
CSV Reader
Working of the CSV Reader:
1. Opens the .csv file and splits the horizontal values into a list.
2. Removes the "\n" character from the contents of the list.
3. Generates a list containing the values of the first row.
4. The contents are separated by commas so the values in the list do not
   contain a comma.
5. The contents of the first row are displayed. They usually contain the names
   of the columns and hence are not numbered.
6. Displays the contents of the .csv file.
7. The contents of the .csv file are displayed one by one with proper
   numbering. The columns are separated as per the number of tabs
   specified by the user in shell.py file.
"""
def csv(location, spacing, csv_fs):
    csv_file = open(location, "r", encoding = "utf-8")
    contents = csv_file.readlines()
    for trim in range(0, len(contents)):
        contents[trim] = contents[trim][0:-1]
    first_line = contents[0].split(csv_fs)
    print("    ", end = "")
    for first_index in range(0, len(first_line)):
        print(str(first_line[first_index]), end = str("\t" * spacing))
    print()
    for val in range(1, len(contents)):
        row = contents[val].split(csv_fs)
        print(str(val) + ". ", end = " ")
        for itr in range(0, len(row)):
            print(str(row[itr]), end = str("\t" * spacing))
        print()

"""
parse_csv() reads data from a CSV file and returns a list with data
organized as rows.
Working of parse_csv():
1. Declares an empty list which is filled with data and returned at the end
   of the function.
2. The escape character "\n" is removed.
3. The function reads the CSV file and separates the data in each rows with ",".
4. The list of separated data is appended to the empty list (parsed_list).
5. parsed_list is returned.
"""
def parse_csv(location, csv_fs):
    parsed_list = []
    csv_parse_file = open(location, "r", encoding = "utf-8")
    parse_contents = csv_parse_file.readlines()
    parse_contents = trim_n(parse_contents)
    for add_cell in range(0, len(parse_contents)):
        info_cells = parse_contents[add_cell].split(csv_fs)
        parsed_list.append(info_cells)
    return parsed_list

def parse_file(location):
    parse_file = open(location, "r", encoding = "utf-8")
    file_data = parse_file.readlines()
    file_data = trim_n(file_data)
    return file_data

"""
starts_with() checks if the first parameter (a string) starts with the
given parameter (a string). Returns True if the first string starts with
the first one, returns False if it does not.
"""
def starts_with(string, trimmed_string):
    """Slicing the first string till the length of the second string
       to check if they match"""
    return (trimmed_string == string[0:len(trimmed_string)])


"""read_file() reads a text file and displays the contents as a whole."""
def read_file(location):
    rfile = open(location, "r", encoding = "utf-8")
    print(rfile.read())
    rfile.close()


"""
read_log() reads the log.txt file from the directory of this file (lib.py)
and displays the contents with numbering.
log.txt records the contents of the commands passed to the
prompt in shell.py file.
Working of read_log():
1. Prints a blank line only if log.txt contains something.
2. Removes the "\n" character from the lines of log.txt file.
3. Displays the contents of log.txt with numbering.
4. Prints a blank line before the first line and after the last line
   only if log.txt contains something.
"""
def read_log():
    read_log_file = open("log.txt", "r", encoding = "utf-8")
    log_history = read_log_file.readlines()
    if len(log_history) > 0:
        print()
    for trim_log in range(0, len(log_history)):
        log_history[trim_log] = log_history[trim_log][:-1]
    for disp_log in range(0, len(log_history)):
        print(str(disp_log + 1) + ". " + log_history[disp_log])
    if len(log_history) > 0:
        print()
    read_log_file.close()


"""
del_spaces() removes the extra unwanted spaces from the entered command.
Working of del_spaces():
1. The "for" loop iterates and deletes the empty strings
   generated for spaces after using split().
2. The loop deletes the few empty strings but
   causes an IndexError because the loop variable keeps
   increasing as it keeps iterating but the length of the
   list decreases as few of the empty strings get deleted.
   Thus, the code tries to access a higher index of the list
   which does not even exist.
3. The following function handles the IndexError and
   recursively calls itself to delete the remaining
   empty strings.
"""
def del_spaces(arr):
    new_arr = []
    for check_arr in range(0, len(arr)):
        if arr[check_arr] != "":
            new_arr.append(arr[check_arr])
    return new_arr

"""
clear_screen() makes the terminal tidy again.
The function checks the system, Explore is running on
and runs the terminal command to clear it up.

For Linux and MacOS, it runs: clear
For Windows, it runs: cls
"""
def clear_screen():
    if platform() == "Linux" or platform() == "Darwin":
        system("clear")
    elif platform() == "Windows":
        system("cls")
    else:
        print("Unable to clear screen.")

"""
disp_list() reads a multi-dimensional list.
Working of disp_list():
1. A loop iterates over the entire list.
2. Another loop iterated over all the elements (also lists) of the passed
   multi-dimensional list.
3. The function then prints each item,
"""
def disp_list(arr):
    for itr_item in range(0, len(arr)):
        for itr_content in range(0, len(arr[itr_item])):
            print("", end = "    ")
            print(arr[itr_item][itr_content], end = "    ")
        print()

def read_list(arr):
    for item in range(0, len(arr)):
        print(str(item + 1) + ". " + arr[item])

"""
del_left_zeros() removes all the zeros from the left side of the text
as eval() cannot evaluate string which has zeros on it's left side.
"""
def del_left_zeros(text):
    zero_counter = 0
    while text[zero_counter] == "0":
        zero_counter = zero_counter + 1
    return text[zero_counter:]

def join_string(arr, start, end):
    complete_string = ""
    for join_str in range(start, end + 1):
        complete_string = complete_string + arr[join_str] + " "
    complete_string = complete_string[:-1]
    return complete_string
