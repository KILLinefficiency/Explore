from requests import get
VERSION = 3.0
CODENAME = "Kal-El"
LICENSE = "GNU General Public License v3.0"
AUTHOR = "Shreyas Sable"
REPOSITORY = "https://www.github.com/KILLinefficiency/Explore"

SERVER_IP = ""
CSV_FS = ","
CSV_SPACING = 4

exit_comms = ["exit", "exit.", "bye", "bye."]

mess = ""
cluster = ""
book = {}

explore_errors = [
    "\nSystem Error Encountered.\n\nNavigate to Explore's directory and run:\n\n\tmake reset\n\nAlternative: Get a fresh copy of Explore from https://www.github.com/KILLinefficiency/Explore\n",
    "Invalid Key Entered.",
    "Access Denied.",
    "Referenced Data Item(s) not found.",
    "Command Limit Reached.",
    "Invalid Datatypes.",
    "Invalid Key.",
    "Item Not Found.",
    "Invalid Syntax.",
    "Cannot Divide By Zero.",
    "Invalid Expression.",
    "Cannot Read System File.",
    "Invalid File/Directory.",
    "Data Item already exists.",
    "Invalid Import Mode.",
    "Key Already Exists.",
    "Not Found."
]

def error(error_code):
    global explore_errors
    print(explore_errors[int(error_code) - 1])

cmd_requests = {
    "disp": 0,
    "push": 0,
    "pop": 0,
    "mov": 0,
    "count": 0,
    "getmess": 0,
    "calc": 0,
    "getbook": 0,
    "read": 0,
    "csv": 0,
    "book": 0,
    "export": 0,
    "import": 0,
    "set": 0,
    "getcluster": 0,
    "change": 0,
    "get": 0,
    "rem": 0,
    "find": 0,
    "dump": 0
}

cmd_limit = {}

total_commands = list(cmd_requests.keys())
commands = list(cmd_requests.keys())
limit_commands = list(cmd_limit.keys())

def set_limit(command, limit):
    global cmd_limit
    cmd_limit[command] = limit

def rem_limit(commands):
    global cmd_limit
    global cmd_requests
    for rem_limits in range(0, len(commands)):
        del cmd_limit[commands[rem_limits]]
    for reset_counter in range(0, len(commands)):
        cmd_requests[commands[reset_counter]] = 0

def incr_limit_count(command):
    global cmd_requests
    cmd_requests[command] = cmd_requests[command] + 1

def limit_status(commands):
    global total_commands
    limit_commands = list(cmd_limit.keys())
    print()
    for status in range(0, len(commands)):
        limit_enabled = "No"
        requests = None
        limit = 0
        if commands[status] in limit_commands:
            limit_enabled = "Yes"
            limit = cmd_limit[commands[status]]
        requests = cmd_requests[commands[status]]
        print(str(status + 1) + ". Command: " + commands[status] + "\nLimit Enabled: " + limit_enabled + "\nRequests: " + str(requests) + "\nLimit: " + str(limit) + "\n")

def delete_item(array, index):
    del array[index - 1]

def enc_dec(text, key):
    enc_dec_text = ""
    for encrypt in range(0, len(text)):
        enc_dec_text = enc_dec_text + chr(ord(text[encrypt]) ^ key)
    return enc_dec_text

data_types = ["num", "num\n", "alpha", "alpha\n"]

def get_data(ip, memory):
    try:
        global mess
        global cluster
        address = "http://" + ip + ":2166/" + memory
        data = get(address)
        if memory == "mess":
            mess = data.text[0:-1]
        elif memory == "cluster":
            cluster = data.text[0:-1]
    except KeyboardInterrupt:
        pass
        print()
    except ConnectionError:
        print("Server Not Running.")

def set_data(memory):
    global mess
    global cluster
    memory_file = open(("." + memory + "_server_file.txt"), "w+", encoding = "utf-8")
    if memory == "mess":
        memory_file.write(mess)
    elif memory == "cluster":
        memory_file.write(cluster)
    memory_file.close()

def gen_mess_values():
    global mess
    mess_values = mess.split("\n")
    mess_values = del_spaces(mess_values)
    return mess_values

def gen_cluster_values():
    global cluster
    cluster_values = cluster.split("\n")
    cluster_values = del_spaces(cluster_values)
    return cluster_values

def gen_mess_list():
    global mess
    true_mess = []
    mess_values = gen_mess_values()
    for add_to_true_mess in range(0, len(mess_values)):
        mess_items = mess_values[add_to_true_mess].split(" ")
        if mess_items[-1] == "num":
            true_mess.append(float(mess_items[0]))
        elif mess_items[-1] == "alpha":
            true_mess.append(str(join_string(mess_items, 0, len(mess_items) - 2)))
    return true_mess

def gen_cluster_dict():
    global cluster
    true_cluster = {}
    cluster_values = gen_cluster_values()
    for add_to_true_cluster in range(0, len(cluster_values)):
        cluster_items = cluster_values[add_to_true_cluster].split(" ")
        if cluster_items[-1] == "num":
            true_cluster[cluster_items[0]] = float(join_string(cluster_items, 1, len(cluster_items) - 2))
        elif cluster_items[-1] == "alpha":
            true_cluster[cluster_items[0]] = str(join_string(cluster_items, 1, len(cluster_items) - 2))
    return true_cluster

def add_n(items):
    for add_n in range(0, len(items)):
        if items[add_n][-1] != "\n":
            items[add_n] = items[add_n] + "\n"

def add_mess(value, data_type):
    global mess
    mess = mess + str(value) + " " + data_type + "\n"

def insert_mess(value, data_type, position):
    global mess
    mess_values = gen_mess_values()
    add_n(mess_values)
    mess = ""
    mess_values.insert(position - 1, str(value) + " " + data_type + "\n")
    for concat_mess in range(0, len(mess_values)):
        mess = mess + mess_values[concat_mess]

def get_from_mess(position):
    global mess
    mess_items = mess.split("\n")
    mess_items = del_spaces(mess_items)
    required_item = mess_items[position - 1]
    required_item = required_item.split()
    value = join_string(required_item, 0, len(required_item) - 2)
    if required_item[-1] == "num":
        value = float(value)
    elif required_item[-1] == "alpha":
        value = str(value)
    if position > 0:
        return value
    else:
        pass

def move_in_mess(value, data_type, position):
    global mess
    mess_values = gen_mess_values()
    add_n(mess_values)
    del mess_values[position - 1]
    mess_values.insert(position - 1, str(value) + " " + data_type + "\n")
    mess = ""
    for concat_mess in range(0, len(mess_values)):
        mess = mess + mess_values[concat_mess]

def count_mess():
    mess_values = gen_mess_values()
    return len(mess_values)

def clean_mess():
    global mess
    mess = ""

def pop_from_mess(items):
    global mess
    mess_values = gen_mess_values()
    add_n(mess_values)
    if items == []:
        mess_values[-1] = ""
    else:
        for del_item in range(0, len(items)):
            mess_values[int(items[del_item]) - 1] = ""
    mess_values = del_spaces(mess_values)
    mess = ""
    for concat_mess in range(0, len(mess_values)):
        mess = mess + mess_values[concat_mess]

def add_cluster(key, value, data_type):
    global cluster
    cluster = cluster + str(key) + " " + str(value) + " " + data_type + "\n"

def gen_cluster_keys():
    cluster_items = gen_cluster_dict()
    cluster_keys = list(cluster_items.keys())
    return cluster_keys

def gen_cluster_key_values():
    cluster_items = gen_cluster_dict()
    cluster_values = list(cluster_items.values())
    return cluster_values

def change_in_cluster(key, new_value, data_type):
    global cluster
    cluster_values = gen_cluster_values()
    add_n(cluster_values)
    cluster_keys = gen_cluster_keys()
    key_index = cluster_keys.index(key)
    del cluster_values[key_index]
    cluster_values.insert(key_index, str(key) + " " + str(new_value) + " " + data_type + "\n")
    cluster = ""
    for concat_cluster in range(0, len(cluster_values)):
        cluster = cluster + cluster_values[concat_cluster]

def get_from_cluster(key):
    global cluster
    cluster_items = cluster.split("\n")
    cluster_items = del_spaces(cluster_items)
    for search_item in range(0, len(cluster_items)):
        individual_item = cluster_items[search_item].split()
        if individual_item[0] == key:
            value = join_string(individual_item, 1, len(individual_item) - 2)
            if individual_item[-1] == "num":
                return float(value)
            elif individual_item[-1] == "alpha":
                return str(value)

def rem_from_cluster(key):
    global cluster
    cluster_values = gen_cluster_values()
    add_n(cluster_values)
    for rem_items in range(0, len(cluster_values)):
        if starts_with(cluster_values[rem_items], key):
            cluster_values[rem_items] = ""
    cluster_values = del_spaces(cluster_values)
    cluster = ""
    for cluster_concat in range(0, len(cluster_values)):
        cluster = cluster + cluster_values[cluster_concat]

def clean_cluster():
    global cluster
    cluster = ""

def count_cluster():
    cluster_values = gen_cluster_values()
    return len(cluster_values)

def add_to_ms_directly_safe(value, memory_structure):
    global data_types
    global mess
    global cluster
    split_array = value.split(" ")
    if split_array[-1] in data_types: 
        if memory_structure == "mess":
            mess = mess + value
        elif memory_structure == "cluster":
            cluster = cluster + value

def add_to_ms_directly_unsafe(value, memory_structure):
    global mess
    global cluster
    if memory_structure == "mess":
        mess = mess + value
    elif memory_structure == "cluster":
        cluster = cluster + value

def trim_n(array):
    clean_array = []
    for trim in range(0, len(array)):
        if array[trim][-1] == "\n":
            clean_array.append(array[trim][0:-1])
        else:
            clean_array,append(array[trim])
    return clean_array

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

def starts_with(string, trimmed_string):
    return (trimmed_string == string[0:len(trimmed_string)])

def read_file(location):
    rfile = open(location, "r", encoding = "utf-8")
    print(rfile.read())
    rfile.close()

def del_spaces(arr):
    new_arr = []
    for check_arr in range(0, len(arr)):
        if arr[check_arr] != "":
            new_arr.append(arr[check_arr])
    return new_arr

def disp_list(arr):
    for itr_item in range(0, len(arr)):
        for itr_content in range(0, len(arr[itr_item])):
            print("", end = "    ")
            print(arr[itr_item][itr_content], end = "    ")
        print()

def read_list(arr):
    for item in range(0, len(arr)):
        print(str(item + 1) + ". " + arr[item])

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

def del_comments(commands):
    clean_commands = []
    for trim_comments in range(0, len(commands)):
        if not(starts_with(commands[trim_comments], "...")):
            clean_commands.append(commands[trim_commands])
    return clean_commands

"""
Comments will also be present on the same line as that of
the Explore command statement. The following function
detects and deletes these comments. The detection is done
by checking if a individual word is or starts with "...".
If yes, then the function deletes the word and all the words
onwards to that word.
"""
def del_line_comm(commands):
    try:
        for del_comm in range(0, len(commands)):
            if commands[del_comm] == "..." or starts_with(commands[del_comm], "..."):
                del commands[commands.index(commands[del_comm]):]
    except IndexError:
        del_line_comm(commands)

def invoke(command):
    global commands
    limit_commands = list(cmd_limit.keys())
    error_catch = 0
    try:
        command = command.replace("\t", " ")
        command = command.strip()
        cmd = command.split(" ")
        cmd = del_spaces(cmd)
        # Deletes all the comments present with the Explore command.
        del_line_comm(cmd)

        for add_spaces in range(0, len(cmd)):
            for put_spaces in range(0, len(cmd[add_spaces])):
                if "|" in cmd[add_spaces]:
                    cmd[add_spaces] = cmd[add_spaces].replace("|", " ")
        
        try:
            for replace_ref in range(0, len(cmd)):
                if starts_with(cmd[replace_ref], "x_"):
                    cmd[replace_ref] = str(get_from_mess(int(cmd[replace_ref][2:])))
                elif starts_with(cmd[replace_ref], "y_"):
                    cmd[replace_ref] = str(get_from_cluster(cmd[replace_ref][2:]))
                elif starts_with(cmd[replace_ref], "b_"):
                    info_address = cmd[replace_ref][2:].split("->")
                    if book[info_address[0]][0] == "text":
                        cmd[replace_ref] = str(book[info_address[0]][1][int(info_address[1]) - 1])
                    elif book[info_address[0]][0] == "csv":
                        cmd[replace_ref] = str(book[info_address[0]][1][int(info_address[1]) - 1][int(info_address[2]) - 1])
        except (KeyError, ValueError, IndexError):
            error(4)
            error_catch = error_catch + 1
        try:
            if (cmd[0] in commands) and (cmd[0] in limit_commands) and (len(cmd) != 0):
                if cmd_requests[cmd[0]] >= cmd_limit[cmd[0]]:
                    error(5)
                    return None
        except KeyError:
            error_catch = error_catch + 1

        if cmd[0] in limit_commands:
            incr_limit_count(cmd[0])

        if cmd[0] == "limit":
            try:
                if cmd[1] == "enable":
                    if cmd[2] == "all":
                        for limit_all in range(0, len(total_commands)):
                            set_limit(total_commands[limit_all], int(eval(join_string(cmd, 3, len(cmd) - 1))))
                    elif cmd[2] != "all":
                        set_limit(cmd[2], int(eval(join_string(cmd, 3, len(cmd) - 1))))
                elif cmd[1] == "disable":
                    if cmd[2] == "all":
                        rem_limit(list(cmd_limit.keys()))
                    elif cmd[2] != "all":
                        rem_limit(cmd[2:])
                elif cmd[1] == "status":
                    if cmd[2] == "all":
                        limit_status(total_commands)
                    elif cmd[2] != "all":
                        limit_status(cmd[2:])
            except IndexError:
                error_catch = error_catch + 1

        elif (cmd[0] == "about" or cmd[0] == "info") and len(cmd) == 1:
            return {
                "Version": VERSION,
                "Codename": CODENAME,
                "License": LICENSE,
                "Author": AUTHOR,
                "Repository": REPOSITORY
            }
        elif cmd[0] == "disp":
            disp_data = join_string(cmd, 1, len(cmd) - 1)
            print(disp_data)

        elif cmd[0] == "push" and cmd[1] == "num":
            try:
                num_data = cmd[2]
                if len(cmd) == 3:
                    add_mess(num_data, "num")
                if len(cmd) == 4:
                    insert_mess(eval(num_data), "num", int(cmd[-1]))
            except ValueError:
                    error(6)
            except KeyError:
                error(2)

        elif cmd[0] == "push" and cmd[1] == "alpha" and len(cmd) >= 3:
            try:
                try:
                    data_push = cmd[2]
                    # Pushes the data item at a particular index in the mess.
                    if type(int(cmd[-1])) == type(1):
                        insert_data = join_string(cmd, 2, len(cmd) - 2)
                        insert_mess(insert_data, "alpha", int(cmd[-1]))
                # Pushes the data item at the last position in the mess.
                except ValueError:
                    push_data = join_string(cmd, 2, len(cmd) - 1)
                    add_mess(push_data, "alpha")
            except ValueError:
                    error(6)
            except KeyError:
                error(2)

        elif cmd[0] == "pop":
            try:
                pop_from_mess(cmd[1:])
            except IndexError:
                pass

        elif cmd[0] == "mov":
            if cmd[1] == "num":
                mov_data = ""
                for join_mov_data in range(2, len(cmd) - 1):
                    mov_data = mov_data + del_left_zeros(cmd[join_mov_data]) + " "
                mov_data = mov_data[:-1]
                move_in_mess(mov_data, "num", int(cmd[-1]))
            elif cmd[1] == "alpha":
                # Replaces the current data item of the given index with the supplied alphabetic data item.
                try:
                    mov_data = join_string(cmd, 2, len(cmd) - 2)
                    move_in_mess(mov_data, "alpha", int(cmd[-1]))
                except ValueError:
                        error(6)
                except IndexError:
                    error(8)
                except KeyError:
                    error(2)
            else:
                    error(9)

        elif cmd[0] == "count" and len(cmd) == 2:
            if cmd[1] == "mess":
                print(count_mess())
            elif cmd[1] == "cluster":
                print(count_cluster())
            elif cmd[1] == "book":
                print(len(book))
            else:
                error(9)

        elif cmd[0] == "clean":
            clean_list = cmd[1:]
            if "mess" in clean_list:
                clean_mess()
            if "cluster" in clean_list:
                clean_cluster()
            if "book" in clean_list:
                clear()

        elif cmd[0] == "calc":
            try:
                equation = ""
                # Concatenates the operators and the numeric values.
                for check in range(1, len(cmd)):
                    equation = equation + del_left_zeros(cmd[check])
                maths_answer = eval(equation)
                if maths_answer == True:
                    print("Yes. (1)")
                elif maths_answer == False:
                    print("No. (0)")
                else:
                    print(maths_answer)
            except ValueError:
                    error(6)
            except IndexError:
                error(8)
            except ZeroDivisionError:
                error(10)
            except EOFError:
                error(11)

        elif cmd[0] == "getbook" and len(cmd) == 1:
            # Gets the data labels of all the parsed data.
            book_keys = list(book.keys())
            if len(book_keys) == 0:
                pass
            else:
                for itr_book in range(0, len(book_keys)):
                    # Displays the label of the parsed data and the contents
                    # in an organized way.
                    print()
                    print(str(book_keys[itr_book]) + ": ")
                    print()
                    if book[book_keys[itr_book]][0] == "csv":
                        disp_list(book[book_keys[itr_book]][1])
                    elif book[book_keys[itr_book]][0] == "text":
                        read_list(book[book_keys[itr_book]][1])
                print()

        elif cmd[0] == "read":
            try:
                file_address = join_string(cmd, 1, len(cmd) - 1)
                print()
                read_file(file_address)
                print()
            except (FileNotFoundError, IsADirectoryError):
                error(13)

        elif cmd[0] == "csv" and len(cmd) >= 2:
            try:
                if cmd[1] == "config":
                    if cmd[2] == "fs":
                        new_csv_fs = join_string(cmd, 3, len(cmd) - 1)
                        CSV_FS = new_csv_fs
                    elif cmd[2] == "tab":
                        CSV_SPACING = int(eval(join_string(cmd, 3, len(cmd) - 1)))
                else:
                    path = join_string(cmd, 1, len(cmd) - 1)
                    print()
                    csv(path, CSV_SPACING, CSV_FS)
                    print()
            except (FileNotFoundError, IsADirectoryError):
                error(13)

        elif cmd[0] == "book" and len(cmd) >= 4:
            try:
                path = join_string(cmd, 3, len(cmd) - 1)
                book_keys = list(book.keys())
                if cmd[1] == "csv":
                    if not(cmd[2] in book_keys):
                        print()
                        csv(path, 1, CSV_FS)
                        print()
                        book[cmd[2]] = ["csv", parse_csv(path, CSV_FS)]
                    else:
                        error(14)
                elif cmd[1] == "text":
                    if not(cmd[2] in book_keys):
                        print()
                        read_file(path)
                        print()
                        book[cmd[2]] = ["text", parse_file(path)]
                    else:
                        error(14)
            except (FileNotFoundError, IsADirectoryError):
                error(13)

        elif cmd[0] == "export" and cmd[1] == "mess" and len(cmd) >= 3:
            try:
                back_char = 1
                if starts_with(cmd[-1], "e_"):
                    back_char = 2
                    e_m_key = int(cmd[-1][2:])
                mess_export_address = join_string(cmd, 2, len(cmd) - back_char)
                mess_export_file = open(mess_export_address, "w+", encoding = "utf-8")
                if starts_with(cmd[-1], "e_"):
                    mess_export_file.write(enc_dec(mess, e_m_key))
                else:
                    mess_export_file.write(mess)
                mess_export_file.close()
            except (FileNotFoundError, IsADirectoryError):
                error(13)

        elif cmd[0] == "export" and cmd[1] == "cluster" and len(cmd) >= 3:
            try:
                back_char = 1
                if starts_with(cmd[-1], "e_"):
                    back_char = 2
                    e_c_key = int(cmd[-1][2:])
                cluster_export_address = join_string(cmd, 2, len(cmd) - back_char)
                cluster_export_file = open(cluster_export_address, "w+", encoding = "utf-8")
                if starts_with(cmd[-1], "e_"):
                    cluster_export_file.write(enc_dec(cluster, e_c_key))
                else:
                    cluster_export_file.write(cluster)
                cluster_export_file.close()
            except (FileNotFoundError, IsADirectoryError):
                error(13)

        elif cmd[0] == "import" and cmd[1] == "mess" and len(cmd) >= 4:
            try:
                back_char = 1
                if not (cmd[2] == "w" or cmd[2] == "rw"):
                    error(15)
                    pass
                if cmd[2] == "rw":
                    clean_mess()
                if starts_with(cmd[-1], "d_"):
                    back_char = 2
                    d_m_key = int(cmd[-1][2:])
                mess_import_address = join_string(cmd, 3, len(cmd) - back_char)
                mess_import_file = open(mess_import_address, "r", encoding = "utf-8")
                mess_contents = mess_import_file.read()
                if starts_with(cmd[-1], "d_"):
                    add_to_ms_directly_unsafe(enc_dec(mess_contents, d_m_key), "mess")
                else:
                    add_to_ms_directly_safe(mess_contents, "mess")
            except (FileNotFoundError, IsADirectoryError):
                error(13)

        elif cmd[0] == "import" and cmd[1] == "cluster" and len(cmd) >= 4:
            try:
                back_char = 1
                if not (cmd[2] == "w" or cmd[2] == "rw"):
                    error(15)
                    pass
                if cmd[2] == "rw":
                    clean_cluster()
                if starts_with(cmd[-1], "d_"):
                    back_char = 2
                    d_c_key = int(cmd[-1][2:])
                cluster_import_address = join_string(cmd, 3, len(cmd) - back_char)
                cluster_import_file = open(cluster_import_address, "r", encoding = "utf-8")
                cluster_contents = cluster_import_file.read()
                if starts_with(cmd[-1], "d_"):
                    add_to_ms_directly_unsafe(enc_dec(cluster_contents, d_c_key), "cluster")
                else:
                    add_to_ms_directly_safe(cluster_contents, "cluster")
            except (FileNotFoundError, IsADirectoryError):
                error(13)

        elif cmd[0] == "set" and len(cmd) >= 4:
            try:
                cluster_existing_keys = gen_cluster_keys()
                if cmd[1] in cluster_existing_keys:
                    error(16)
                    pass
                else:
                    data_set = cmd[3]
                    if cmd[2] == "num":
                        if len(cmd) == 4:
                            add_cluster(cmd[1], float(eval(data_set)), "num")
                        elif len(cmd) > 4:
                            data_set = ""
                            for set_num_data in range(3, len(cmd)):
                                data_set = data_set + del_left_zeros(cmd[set_num_data]) + " "
                            add_cluster(cmd[1], float(eval(data_set)), "num")
                    elif cmd[2] == "alpha":
                        data_set = ""
                        data_set = join_string(cmd, 3, len(cmd) - 1)
                        add_cluster(cmd[1], str(data_set), "alpha")
                    else:
                        pass
            except (NameError, ValueError):
                    error(6)

        elif cmd[0] == "getcluster":
            existing_keys = gen_cluster_keys()
            if len(existing_keys) > 0:
                # Displays the entire cluster.
                if len(cmd) == 1:
                    print("\nKey : Value\n")
                    for items in range(0, len(existing_keys)):
                        # Displays each key and value for the list "cluster_items"
                        # and is separated by " : ".
                        print(existing_keys[items], get_from_cluster(existing_keys[items]), sep = " : ")
                    print()

                # Displays only the keys from the cluster.
                elif len(cmd) == 2 and cmd[1] == "keys":
                    keys = gen_cluster_keys()
                    print("\nKey :\n")
                    for list_keys in range(0, len(keys)):
                        print(str(keys[list_keys]) + " :")
                    print()
                # Displays only the values from the cluster.
                elif len(cmd) == 2 and cmd[1] == "values":
                    keys = gen_cluster_keys()
                    print("\n: Value\n")
                    for list_values in range(0, len(keys)):
                        print(": " + str(get_from_cluster(keys[list_values])))
                    print()
                else:
                    error(9)
            else:
                pass

        elif cmd[0] == "change" and len(cmd) >= 4:
            cluster_keys = gen_cluster_keys()
            if cmd[1] in cluster_keys:
                try:
                    if cmd[2] == "num":
                        change_value = ""
                        for join_change_value in range(3, len(cmd)):
                            change_value = change_value + del_left_zeros(cmd[join_change_value]) + " "
                        change_value = change_value[:-1]
                        change_in_cluster(cmd[1], float(change_value), "num")
                    elif cmd[2] == "alpha":
                        change_value = join_string(cmd, 3, len(cmd) - 1)
                        change_in_cluster(cmd[1], change_value, "alpha")
                    else:
                        error(9)
                except ValueError:
                        error(6)
            else:
                error(2)

        elif cmd[0] == "get":
            try:
                if cmd[1] == "mess":
                    print(get_from_mess(int(cmd[2])))
                elif cmd[1] == "cluster":
                    if get_from_cluster(cmd[2]) != None:
                        print(get_from_cluster(cmd[2]))
                    else:
                        error(8)
                elif cmd[1] == "book":
                    # Gets parsed CSV data.
                    if len(cmd) == 5:
                        print(str(book[cmd[2]][1][int(cmd[3]) - 1][int(cmd[4]) - 1]))
                    elif len(cmd) == 4:
                        print(str(book[cmd[2]][1][int(cmd[3]) - 1]))
            except (IndexError, KeyError):
                error(8)

        elif cmd[0] == "rem" and len(cmd) >= 1:
            try:
                cluster_keys = gen_cluster_keys()
                # Removes the last data item from the cluster if the key is not supplied.
                if len(cmd) == 1:
                    rem_from_cluster(cluster_keys[-1])
                # Removes one or multiple data item(s) from the cluster with the key(s) supplied.
                else:
                    rem_items = cmd[1:]
                    for rem_several in range(0, len(rem_items)):
                        try:
                            rem_from_cluster(rem_items[rem_several])
                        except (KeyError, IndexError):
                            pass
            except KeyError:
                pass

        elif cmd[0] == "find" and len(cmd) >= 3:
            # Sets the variable for the item to be found to None.
            search = None
            try:
                # Sets a numeric value to be searched.
                if cmd[1] == "num":
                    search = float(cmd[2])
                elif len(cmd) >= 3 and cmd[1] == "alpha":
                    search = join_string(cmd, 2, len(cmd) - 1)
            except (ValueError, TypeError):
                error(6)
                pass
            # Generates separate lists for Cluster keys and values.
            m_values = gen_mess_list()
            c_keys = gen_cluster_keys()
            c_values = gen_cluster_key_values()
            b_data_space = list(book.keys())
            b_data_space_contents = list(book.values())

            text_file_values = []
            # print(b_data_space_contents)
            for get_text_values in range(0, len(b_data_space_contents)):
                if b_data_space_contents[get_text_values][0] == "text":
                    text_file_values.append(b_data_space_contents[get_text_values][1])

            for get_values in range(0, len(b_data_space_contents)):
                b_data_space_contents[get_values] = b_data_space_contents[get_values][1]
            
            book_all_values = []
            for all_values in range(0, len(b_data_space_contents)):
                for add_values in range(0, len(b_data_space_contents[all_values])):
                    for add_more_values in range(0, len(b_data_space_contents[all_values][add_values])):
                        book_all_values.append(b_data_space_contents[all_values][add_values][add_more_values])
            # Shows a "Not Found." message if the item is found nowhere.
            if not((search in c_keys) or (search in c_values) or (search in m_values) or (search in b_data_space) or (search in book_all_values) or (search in text_file_values[0])):
                error(17)
            else:
                data_type = None
                # Searches the item in the Mess.
                for search_mess in range(0, len(m_values)):
                    if search == m_values[search_mess]:
                        if type(search) == type(1.1):
                            data_type = "num"
                        elif type(search) == type("1.1"):
                            data_type = "alpha"
                        # Shows the detailed message about the item found.
                        found_msg = "Location: Mess\t Datatype: " + str(data_type) + "\t Position: " + str(search_mess + 1)
                        print(found_msg)
                # Searches the item in the Cluster keys.
                for search_keys in range(0, len(c_keys)):
                    if search == c_keys[search_keys]:
                        # Shows the detailed message about the item found.
                        print("Location: Cluster\t Itemtype: Key\t Value: " + str(c_values[search_keys]))
                # Searches the item in the Cluster values.
                for search_values in range(0, len(c_values)):
                    if search == c_values[search_values]:
                        data_type1 = None
                        if type(search) == type(1.1):
                            data_type1 = "num"
                        elif type(search) == type("1.1"):
                            data_type1 = "alpha"
                        # Shows the detailed message about the item found.
                        print("Location: Cluster\t Itemtype: Value\t Datatype: " + str(data_type1) + "\t Key: " + str(c_keys[search_values]))
                for search_data_space in range(0, len(b_data_space)):
                    if search == b_data_space[search_data_space]:
                        print("Location: Book\t Itemtype: Dataspace\t Position: " + str(search_data_space + 1))
                for search_text_values in range(0, len(text_file_values[0])):
                    if search == text_file_values[0][search_text_values]:
                        print("Location: Book\t Itemtype: Parsed Values\t Position: " + str(search_text_values + 1))
                # Searches for the particular data item and the data space and outputs it's information.
                for search_parsed_values in range(0, len(b_data_space_contents)):
                    for search_each_dataspace in range(0, len(b_data_space_contents[search_parsed_values])):
                        for search_each_value in range(0, len(b_data_space_contents[search_parsed_values][search_each_dataspace])):
                            if search == b_data_space_contents[search_parsed_values][search_each_dataspace][search_each_value]:
                                print("Location: Book\t Itemtype: Parsed Value\tRow: " + str(b_data_space_contents[search_parsed_values].index(b_data_space_contents[search_parsed_values][search_each_dataspace]) + 1) + "\tColumn: " + str(b_data_space_contents[search_parsed_values][search_each_dataspace].index(b_data_space_contents[search_parsed_values][search_each_dataspace][search_each_value]) + 1))
        
        elif cmd[0] == "dump":
            dump_file = open(cmd[-1], "a+")
            dump_file_text = ""
            for dump_file_loop in range(1, len(cmd) - 1):
                dump_file_text = dump_file_text + cmd[dump_file_loop] + " "
            dump_file_text = dump_file_text[:-1]
            dump_file.write(dump_file_text + "\n")
            dump_file.close()
        
        elif cmd[0] == "server":
            if cmd[1] == "connect":
                    SERVER_IP = cmd[2]
            if SERVER_IP == "" and cmd[1] != "update":
                print("No Server Connected.")
            else:
                if cmd[1] == "ip":
                    print("Connected to: " + SERVER_IP)
                elif cmd[1] == "update":
                    if cmd[2] == "mess":
                        set_data("mess")
                    elif cmd[2] == "cluster":
                        set_data("cluster")
                    elif cmd[2] == "all":
                        set_data("mess")
                        set_data("cluster")
                    else:
                        print("Memory Location Not Specified.")
                elif cmd[1] == "fetch":
                    if cmd[2] == "mess":
                        get_data(SERVER_IP, "mess")
                    elif cmd[2] == "cluster":
                        get_data(SERVER_IP, "cluster")
                    elif cmd[2] == "all":
                        get_data(SERVER_IP, "mess")
                        get_data(SERVER_IP, "cluster")
                    else:
                        print("Memory Location Not Specified.")

        elif cmd[0] == "":
            pass

        else:
            print("Invalid Command: " + str(command))

    # except NameError:
    #     pass
    except SyntaxError:
        print("Invalid Syntax.")
    except ValueError:
        print("Invalid Datatypes.")
    # except:
    #     print("Oops! Something Went Wrong.")

def del_unwanted(command_list):
    # Removes the "\n" character from each line.
    for trim_script in range(0, len(command_list) - 1):
            command_list[trim_script] = command_list[trim_script][:-1]
    # Removes leading and trailing tabs from the commands.
    for strip_tabs in range(0, len(command_list)):
            command_list[strip_tabs] = command_list[strip_tabs].strip()
    # Remove the "" character representating a blank line.
    del_spaces(command_list)
    # Deletes all the comments from the Script.
    del_comments(command_list)

# Runs an Explore Script if a valid path is specified.
def run(path):
    try:
        script = open(path, "r", encoding = "utf-8")
        contents = script.readlines()
        # Removes the unwanted characters from the Script.
        del_unwanted(contents)
        # Runs each line as an Explore command.
        for run_comm in range(0, len(contents)):
            invoke(contents[run_comm])
    except (FileNotFoundError, IsADirectoryError):
        print("Invalid File/Directory.")
    except:
        print("Oops! Something Went Wrong.")
