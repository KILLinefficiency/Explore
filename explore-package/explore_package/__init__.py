from requests import get
INFO = {
    "VERSION": 3.0,
    "CODENAME": "Kal-El",
    "LICENSE": "GNU General Public License v3.0",
    "AUTHOR": "Shreyas Sable",
    "REPOSITORY": "https://www.github.com/KILLinefficiency/Explore"
}

# Code that runs the Explore Server.
server_code = """
const http = require("http");
const fs = require("fs");

const SERVER_PORT = 2166;

const index_page = `<html>
	<head>
		<title>Explore Server</title>
	</head>

	<body>
		<h1 align = "center">Explore Sever</h1>
		<br>
		<h3>Routes for Explore Server:</h3>
			<code>/mess</code>
			<br><br>
			<code>/cluster</code>
	</body>

	</html>
`;

const mess_file = ".mess_server_file.txt";
const cluster_file = ".cluster_server_file.txt";

server = http.createServer((req, res) => {
	if(req.url == "/") {
		res.write(index_page);
		res.end();
	}
	if(req.url == "/mess") {
		fs.readFile(mess_file, (err, mess_contents) => {
			if(err) {
				console.log("Error: Update the server from your Explore instance.")
			}
			else {
				res.write(mess_contents);
				res.end();
			}
		});
	}
	if(req.url == "/cluster") {
		fs.readFile(cluster_file, (err, cluster_contents) => {
			if(err) {
				console.log("Error: Update the server from your Explore instance.")
			}
			else {
				res.write(cluster_contents);
				res.end();
			}
		});
	}
});

var reqs = 1;
server.on("connection", (socket) => {
	console.log(`Request recieved... (${reqs})`);
	reqs = reqs + 1;
});

server.listen(SERVER_PORT, "0.0.0.0", () => { console.log(`\\nServer running on port ${SERVER_PORT}...\\n`); });

"""

# Spwans a server.js file in the same directory as that of the Python program using the Explore Package.
server_file = open("server.js", "w+", encoding = "utf-8")
server_file.write(server_code)
server_file.close()

explore_errors = [
    "Reserved Place for System Error",
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
    "Not Found.",
    "Server Not Found.",
    "Memory Location Not Specified."
]

def starts_with(string, trimmed_string):
    return (trimmed_string == string[0:len(trimmed_string)])

def join_string(arr, start, end):
    complete_string = ""
    for join_str in range(start, end + 1):
        complete_string = complete_string + arr[join_str] + " "
    complete_string = complete_string[:-1]
    return complete_string

def del_spaces(arr):
    new_arr = []
    for check_arr in range(0, len(arr)):
        if arr[check_arr] != "":
            new_arr.append(arr[check_arr])
    return new_arr

def del_comments(commands):
    try:
        for trim_comments in range(0, len(commands)):
            if starts_with(commands[trim_comments], "..."):
                del commands[trim_comments]
    except IndexError:
        del_comments(commands)

"""
Comments will also be present on the same line as that of
the Explore command statement. The following function
detects and deletes these comments. The detection is done
by checking if a individual word is or starts with "...".
If yes, then the function deletes the word and all the words
onwards to than word.
"""
def del_line_comm(command):
    clean_arr = []
    command = command.split()
    for del_line_comments in range(0, len(command)):
        if command[del_line_comments] == "..." or starts_with(command[del_line_comments], "..."):
            break
        else:
            clean_arr.append(command[del_line_comments])
    clean_command = join_string(clean_arr, 0, len(clean_arr) - 1)
    """for del_comm in range(0, len(commands)):
        if not(command[del_comm] == "..." or starts_with(command[del_comm], "...")):
            clean_arr.append(command[del_comm])"""
    return clean_command

def del_unwanted(command_list):
    for strip_tabs in range(0, len(command_list)):
            command_list[strip_tabs] = command_list[strip_tabs].strip()
    # Remove the "" character representating a blank line.
    command_list = del_spaces(command_list)
    # Deletes all the comments from the Script.
    del_comments(command_list)
    return command_list

def error(error_code):
    global explore_errors
    print(explore_errors[int(error_code) - 1])

def enc_dec(text, key):
    enc_dec_text = ""
    for encrypt in range(0, len(text)):
        enc_dec_text = enc_dec_text + chr(ord(text[encrypt]) ^ key)
    return enc_dec_text

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

def read_file(location):
    rfile = open(location, "r", encoding = "utf-8")
    file_contents = rfile.readlines()
    file_contents = trim_n(file_contents)
    rfile.close()
    return file_contents

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

class Explore:
    __mess = ""
    __cluster = ""
    __book = {}

    __SERVER_IP = ""
    __CSV_FS = ","
    __CSV_SPACING = 4

    __cmd_requests = {
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

    __cmd_limit = {}

    __total_commands = list(__cmd_requests.keys())

    __data_types = ["num", "num\n", "alpha", "alpha\n"]

    def __set_limit(self, command, limit):
        self.__cmd_limit[command] = limit

    def __rem_limit(self, commands):
        for rem_limits in range(0, len(commands)):
            del self.__cmd_limit[commands[rem_limits]]
        for reset_counter in range(0, len(commands)):
            self.__cmd_requests[commands[reset_counter]] = 0

    def __incr_limit_count(self, command):
        self.__cmd_requests[command] = self.__cmd_requests[command] + 1

    def __limit_status(self, commands):
        global total_commands
        limit_commands = list(self.__cmd_limit.keys())
        statuses = []
        for status in range(0, len(commands)):
            limit_enabled = False
            requests = None
            limit = 0
            if commands[status] in limit_commands:
                limit_enabled = True
                limit = self.__cmd_limit[commands[status]]
            requests = self.__cmd_requests[commands[status]]
            statuses.append(
                {
                    "Command": commands[status],
                    "Limit Enabled": limit_enabled,
                    "Requests": requests,
                    "Limit": limit
                }
            )
        return statuses

    def __get_data(self, ip, memory):
        try:
            global mess
            global cluster
            address = "http://" + ip + ":2166/" + memory
            data = get(address)
            if memory == "mess":
                self.__mess = data.text[0:-1]
            elif memory == "cluster":
                self.__cluster = data.text[0:-1]
        except KeyboardInterrupt:
            pass
            print()
        except ConnectionError:
            print("Server Not Running.")

    def __set_data(self, memory):
        global mess
        global cluster
        memory_file = open(("." + memory + "_server_file.txt"), "w+", encoding = "utf-8")
        if memory == "mess":
            memory_file.write(self.__mess)
        elif memory == "cluster":
            memory_file.write(self.__cluster)
        memory_file.close()

    def __gen_mess_values(self):
        global mess
        mess_values = self.__mess.split("\n")
        mess_values = del_spaces(mess_values)
        return mess_values

    def __gen_cluster_values(self):
        global cluster
        cluster_values = self.__cluster.split("\n")
        cluster_values = del_spaces(cluster_values)
        return cluster_values

    def __gen_mess_list(self):
        global mess
        true_mess = []
        mess_values = self.__gen_mess_values()
        for add_to_true_mess in range(0, len(mess_values)):
            mess_items = mess_values[add_to_true_mess].split(" ")
            if mess_items[-1] == "num":
                true_mess.append(float(mess_items[0]))
            elif mess_items[-1] == "alpha":
                true_mess.append(str(join_string(mess_items, 0, len(mess_items) - 2)))
        return true_mess

    def __gen_cluster_dict(self):
        global cluster
        true_cluster = {}
        cluster_values = self.__gen_cluster_values()
        for add_to_true_cluster in range(0, len(cluster_values)):
            cluster_items = cluster_values[add_to_true_cluster].split(" ")
            if cluster_items[-1] == "num":
                true_cluster[cluster_items[0]] = float(join_string(cluster_items, 1, len(cluster_items) - 2))
            elif cluster_items[-1] == "alpha":
                true_cluster[cluster_items[0]] = str(join_string(cluster_items, 1, len(cluster_items) - 2))
        return true_cluster

    def __add_n(self, items):
        for add_n in range(0, len(items)):
            if items[add_n][-1] != "\n":
                items[add_n] = items[add_n] + "\n"

    def __add_mess(self, value, data_type):
        global mess
        self.__mess = self.__mess + str(value) + " " + data_type + "\n"

    def __insert_mess(self, value, data_type, position):
        global mess
        mess_values = self.__gen_mess_values()
        self.__add_n(mess_values)
        self.__mess = ""
        mess_values.insert(position - 1, str(value) + " " + data_type + "\n")
        for concat_mess in range(0, len(mess_values)):
            self.__mess = self.__mess + mess_values[concat_mess]

    def __get_from_mess(self, position):
        global mess
        mess_items = self.__mess.split("\n")
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

    def __move_in_mess(self, value, data_type, position):
        global mess
        mess_values = self.__gen_mess_values()
        self.__add_n(mess_values)
        del mess_values[position - 1]
        mess_values.insert(position - 1, str(value) + " " + data_type + "\n")
        self.__mess = ""
        for concat_mess in range(0, len(mess_values)):
            self.__mess = self.__mess + mess_values[concat_mess]

    def __count_mess(self):
        mess_values = self.__gen_mess_values()
        return len(mess_values)

    def __clean_mess(self):
        global mess
        self.__mess = ""

    def __pop_from_mess(self, items):
        global mess
        mess_values = self.__gen_mess_values()
        self.__add_n(mess_values)
        if items == []:
            mess_values[-1] = ""
        else:
            for del_item in range(0, len(items)):
                mess_values[int(items[del_item]) - 1] = ""
        mess_values = del_spaces(mess_values)
        self.__mess = ""
        for concat_mess in range(0, len(mess_values)):
            self.__mess = self.__mess + mess_values[concat_mess]

    def __add_cluster(self, key, value, data_type):
        global cluster
        self.__cluster = self.__cluster + str(key) + " " + str(value) + " " + data_type + "\n"

    def __gen_cluster_keys(self):
        cluster_items = self.__gen_cluster_dict()
        cluster_keys = list(cluster_items.keys())
        return cluster_keys

    def __gen_cluster_key_values(self):
        cluster_items = self.__gen_cluster_dict()
        cluster_values = list(cluster_items.values())
        return cluster_values

    def __change_in_cluster(self, key, new_value, data_type):
        global cluster
        cluster_values = self.__gen_cluster_values()
        self.__add_n(cluster_values)
        cluster_keys = self.__gen_cluster_keys()
        key_index = cluster_keys.index(key)
        del cluster_values[key_index]
        cluster_values.insert(key_index, str(key) + " " + str(new_value) + " " + data_type + "\n")
        self.__cluster = ""
        for concat_cluster in range(0, len(cluster_values)):
            self.__cluster = self.__cluster + cluster_values[concat_cluster]

    def __get_from_cluster(self, key):
        global cluster
        cluster_items = self.__cluster.split("\n")
        cluster_items = del_spaces(cluster_items)
        for search_item in range(0, len(cluster_items)):
            individual_item = cluster_items[search_item].split()
            if individual_item[0] == key:
                value = join_string(individual_item, 1, len(individual_item) - 2)
                if individual_item[-1] == "num":
                    return float(value)
                elif individual_item[-1] == "alpha":
                    return str(value)

    def __rem_from_cluster(self, key):
        global cluster
        cluster_values = self.__gen_cluster_values()
        self.__add_n(cluster_values)
        for rem_items in range(0, len(cluster_values)):
            if starts_with(cluster_values[rem_items], key):
                cluster_values[rem_items] = ""
        cluster_values = del_spaces(cluster_values)
        self.__cluster = ""
        for cluster_concat in range(0, len(cluster_values)):
            self.__cluster = self.__cluster + cluster_values[cluster_concat]

    def __clean_cluster(self):
        global cluster
        self.__cluster = ""

    def __count_cluster(self):
        cluster_values = self.__gen_cluster_values()
        return len(cluster_values)

    def __add_to_ms_directly_safe(self, value, memory_structure):
        global data_types
        global mess
        global cluster
        split_array = value.split(" ")
        if split_array[-1] in self.__data_types: 
            if memory_structure == "mess":
                self.__mess = self.__mess + value
            elif memory_structure == "cluster":
                self.__cluster = self.__cluster + value

    def invoke(self, command):
        commands = list(self.__cmd_requests.keys())
        limit_commands = list(self.__cmd_limit.keys())
        command = command.strip()
        cmd = command.split(" ")
        try:
            for replace_ref in range(0, len(cmd)):
                if starts_with(cmd[replace_ref], "x_"):
                    cmd[replace_ref] = str(self.__get_from_mess(int(cmd[replace_ref][2:])))
                elif starts_with(cmd[replace_ref], "y_"):
                    cmd[replace_ref] = str(self.__get_from_cluster(cmd[replace_ref][2:]))
                elif starts_with(cmd[replace_ref], "b_"):
                    info_address = cmd[replace_ref][2:].split("->")
                    if self.__book[info_address[0]][0] == "text":
                        cmd[replace_ref] = str(self.__book[info_address[0]][1][int(info_address[1]) - 1])
                    elif self.__book[info_address[0]][0] == "csv":
                        cmd[replace_ref] = str(self.__book[info_address[0]][1][int(info_address[1]) - 1][int(info_address[2]) - 1])
        except (KeyError, ValueError, IndexError):
            error(4)
            pass

        cmd[0] = cmd[0].lower()

        cmd = del_spaces(cmd)
        for add_spaces in range(0, len(cmd)):
            for put_spaces in range(0, len(cmd[add_spaces])):
                if "|" in cmd[add_spaces]:
                    cmd[add_spaces] = cmd[add_spaces].replace("|", " ")

        try:
            if (cmd[0] in commands) and (cmd[0] in limit_commands) and (len(cmd) != 0):
                if self.__cmd_requests[cmd[0]] >= self.__cmd_limit[cmd[0]]:
                    error(5)
                    return None
        except KeyError:
            problems = None

        if cmd[0] in limit_commands:
            self.__incr_limit_count(cmd[0])

        if cmd[0] == "limit":
            try:
                if cmd[1] == "enable":
                    if cmd[2] == "all":
                        for limit_all in range(0, len(self.__total_commands)):
                            self.__set_limit(self.__total_commands[limit_all], int(eval(join_string(cmd, 3, len(cmd) - 1))))
                    elif cmd[2] != "all":
                        self.__set_limit(cmd[2], int(eval(join_string(cmd, 3, len(cmd) - 1))))
                elif cmd[1] == "disable":
                    if cmd[2] == "all":
                        self.__rem_limit(list(self.__cmd_limit.keys()))
                    elif cmd[2] != "all":
                        self.__rem_limit(cmd[2:])
                elif cmd[1] == "status":
                    if cmd[2] == "all":
                        return self.__limit_status(self.__total_commands)
                    elif cmd[2] != "all":
                        return self.__limit_status(cmd[2:])
            except IndexError:
                problems = None

        elif (cmd[0] == "about" or cmd[0] == "info") and len(cmd) == 1:
            return INFO

        elif cmd[0] == "disp":
            disp_data = join_string(cmd, 1, len(cmd) - 1)
            print(disp_data)

        elif cmd[0] == "push" and cmd[1] == "num":
            try:
                num_data = cmd[2]
                if len(cmd) == 3:
                    self.__add_mess(num_data, "num")
                if len(cmd) == 4:
                    self.__insert_mess(eval(num_data), "num", int(cmd[-1]))
            except ValueError:
                error(6)
            except KeyError:
                error(2)
        
        elif cmd[0] == "push" and cmd[1] == "alpha" and len(cmd) >= 3:
            try:
                try:
                    data_push = cmd[2]
                    if type(int(cmd[-1])) == type(1):
                        insert_data = join_string(cmd, 2, len(cmd) - 2)
                        self.__insert_mess(insert_data, "alpha", int(cmd[-1]))
                except ValueError:
                    push_data = join_string(cmd, 2, len(cmd) - 1)
                    self.__add_mess(push_data, "alpha")
            except ValueError:
                error(6)
            except KeyError:
                error(2)

        elif cmd[0] == "pop":
            try:
                self.__pop_from_mess(cmd[1:])
            except IndexError:
                problems = None

        elif cmd[0] == "mov":
            if cmd[1] == "num":
                mov_data = ""
                for join_mov_data in range(2, len(cmd) - 1):
                    mov_data = mov_data + del_left_zeros(cmd[join_mov_data]) + " "
                mov_data = mov_data[:-1]
                self.__move_in_mess(float(eval(mov_data)), "num", int(cmd[-1]))
            elif cmd[1] == "alpha":
                try:
                    mov_data = join_string(cmd, 2, len(cmd) - 2)
                    self.__move_in_mess(mov_data, "alpha", int(cmd[-1]))
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
                return self.__count_mess()
            elif cmd[1] == "cluster":
                return self.__count_cluster()
            elif cmd[1] == "book":
                len(self.__book)
            else:
                error(9)

        elif cmd[0] == "clean":
            clean_list = cmd[1:]
            if "mess" in clean_list:
                self.__clean_mess()
            if "cluster" in clean_list:
                self.__clean_cluster()
            if "book" in clean_list:
                book.clear()

        elif cmd[0] == "getmess":
            return self.__gen_mess_list()

        elif cmd[0] == "calc":
            try:
                equation = ""
                for check in range(1, len(cmd)):
                    equation = equation + del_left_zeros(cmd[check])
                maths_answer = eval(equation)
                return maths_answer
            except (ValueError, IndexError, ZeroDivisionError, EOFError):
                return None

        elif cmd[0] == "getbook":
            return self.__book

        elif cmd[0] == "read":
            try:
                return read_file(join_string(cmd, 1, len(cmd) - 1))
            except(FileNotFoundError, IsADirectoryError):
                error(13)

        elif cmd[0] == "csv" and len(cmd) >= 2:
            try:
                if cmd[1] == "config":
                    if cmd[2] == "fs":
                        new_csv_fs = join_string(cmd, 3, len(cmd) - 1)
                        self.__CSV_FS = new_csv_fs
                    elif cmd[2] == "tab":
                        self.__CSV_SPACING = int(eval(join_string(cmd, 3, len(cmd) - 1)))
                else:
                    path = join_string(cmd, 1, len(cmd) - 1)
                    print()
                    csv(path, self.__CSV_SPACING, self.__CSV_FS)
                    print()
            except (FileNotFoundError, IsADirectoryError):
                error(13)

        elif cmd[0] == "book" and len(cmd) >= 4:
            try:
                path = join_string(cmd, 3, len(cmd) - 1)
                book_keys = list(self.__book.keys())
                if cmd[1] == "csv": 
                    if not(cmd[2] in book_keys):
                        self.__book[cmd[2]] = ["csv", parse_csv(path, self.__CSV_FS)]
                    else:
                        error(14)
                elif cmd[1] == "text":
                    if not(cmd[2] in book_keys):
                        self.__book[cmd[2]] = ["text", parse_file(path)]
                    else:
                        error(14)
            except (FileNotFoundError, IsADirectoryError):
                error(13)

        elif cmd[0] == "export" and cmd[1] == "mess" and len(cmd) >= 3:
            try:
                mess_export_address = join_string(cmd, 2, len(cmd) - 1)
                mess_export_file = open(mess_export_address, "w+", encoding = "utf-8")
                mess_export_file.write(self.__mess)
                mess_export_file.close()
            except (FileNotFoundError, IsADirectoryError):
                error(13)

        elif cmd[0] == "export" and cmd[1] == "cluster" and len(cmd) >= 3:
            try:
                cluster_export_address = join_string(cmd, 2, len(cmd) - 1)
                cluster_export_file = open(cluster_export_address, "w+", encoding = "utf-8")
                cluster_export_file.write(self.__cluster)
                cluster_export_file.close()
            except (FileNotFoundError, IsADirectoryError):
                error(13)

        elif cmd[0] == "import" and cmd[1] == "mess" and len(cmd) >= 4:
            try:
                if not (cmd[2] == "w" or cmd[2] == "rw"):
                    error(15)
                    pass
                if cmd[2] == "rw":
                    self.__clean_mess()
                mess_import_address = join_string(cmd, 3, len(cmd) - 1)
                mess_import_file = open(mess_import_address, "r", encoding = "utf-8")
                mess_contents = mess_import_file.read()
                self.__add_to_ms_directly_safe(mess_contents, "mess")
            except (FileNotFoundError, IsADirectoryError):
                error(13)

        elif cmd[0] == "import" and cmd[1] == "cluster" and len(cmd) >= 4:
            try:
                if not (cmd[2] == "w" or cmd[2] == "rw"):
                    error(15)
                    pass
                if cmd[2] == "rw":
                    self.__clean_cluster()
                cluster_import_address = join_string(cmd, 3, len(cmd) - 1)
                cluster_import_file = open(cluster_import_address, "r", encoding = "utf-8")
                cluster_contents = cluster_import_file.read()
                self.__add_to_ms_directly_safe(cluster_contents, "cluster")
            except (FileNotFoundError, IsADirectoryError):
                error(13)
        
        elif cmd[0] == "set" and len(cmd) >= 4:
            try:
                cluster_existing_keys = self.__gen_cluster_keys()
                if cmd[1] in cluster_existing_keys:
                    error(16)
                    pass
                else:
                    data_set = cmd[3]
                    if cmd[2] == "num":
                        if len(cmd) == 4:
                            self.__add_cluster(cmd[1], float(eval(data_set)), "num")
                        elif len(cmd) > 4:
                            data_set = ""
                            for set_num_data in range(3, len(cmd)):
                                data_set = data_set + del_left_zeros(cmd[set_num_data]) + " "
                            self.__add_cluster(cmd[1], float(eval(data_set)), "num")
                    elif cmd[2] == "alpha":
                        data_set = ""
                        data_set = join_string(cmd, 3, len(cmd) - 1)
                        self.__add_cluster(cmd[1], str(data_set), "alpha")
                    else:
                        pass
            except (NameError, ValueError):
                error(6)
            

        elif cmd[0] == "getcluster":
            if len(cmd) == 1:
                return self.__gen_cluster_dict()
            elif cmd[1] == "keys":
                return self.__gen_cluster_keys()
            elif cmd[1] == "values":
                return self.__gen_cluster_key_values()

        elif cmd[0] == "change" and len(cmd) >= 4:
            cluster_keys = self.__gen_cluster_keys()
            if cmd[1] in cluster_keys:
                try:
                    if cmd[2] == "num":
                        change_value = ""
                        for join_change_value in range(3, len(cmd)):
                            change_value = change_value + del_left_zeros(cmd[join_change_value]) + " "
                        change_value = change_value[:-1]
                        self.__change_in_cluster(cmd[1], float(eval(change_value)), "num")
                    elif cmd[2] == "alpha":
                        change_value = join_string(cmd, 3, len(cmd) - 1)
                        self.__change_in_cluster(cmd[1], change_value, "alpha")
                    else:
                        error(9)
                except ValueError:
                        error(6)
            else:
                error(2)
        
        elif cmd[0] == "get":
            try:
                if cmd[1] == "mess":
                    return self.__get_from_mess(int(cmd[2]))
                elif cmd[1] == "cluster":
                    if self.__get_from_cluster(cmd[2]) != None:
                        return self.__get_from_cluster(cmd[2])
                    else:
                        error(8)
                elif cmd[1] == "book":
                    if len(cmd) == 5:
                        return self.__book[cmd[2]][1][int(cmd[3]) - 1][int(cmd[4]) - 1]
                    elif len(cmd) == 4:
                        return self.__book[cmd[2]][1][int(cmd[3]) - 1]
            except (IndexError, KeyError):
                error(8)

        elif cmd[0] == "rem" and len(cmd) >= 1:
            try:
                cluster_keys = self.__gen_cluster_keys()
                if len(cmd) == 1:
                    self.__rem_from_cluster(cluster_keys[-1])
                else:
                    rem_items = cmd[1:]
                    for rem_several in range(0, len(rem_items)):
                        try:
                            self.__rem_from_cluster(rem_items[rem_several])
                        except (KeyError, IndexError):
                            continue
            except KeyError:
                pass

        elif cmd[0] == "find" and len(cmd) >= 3:
            result = []
            search = None
            try:
                if cmd[1] == "num":
                    search = float(cmd[2])
                elif len(cmd) >= 3 and cmd[1] == "alpha":
                    search = join_string(cmd, 2, len(cmd) - 1)
            except (ValueError, TypeError):
                error(6)
                pass
            m_values = self.__gen_mess_list()
            c_keys = self.__gen_cluster_keys()
            c_values = self.__gen_cluster_key_values()
            b_data_space = list(self.__book.keys())
            b_data_space_contents = list(self.__book.values())

            text_file_values = []
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
            if not((search in c_keys) or (search in c_values) or (search in m_values) or (search in b_data_space) or (search in book_all_values) or (search in text_file_values[0])):
                error(17)
            else:
                data_type = None
                for search_mess in range(0, len(m_values)):
                    if search == m_values[search_mess]:
                        if type(search) == type(1.1):
                            data_type = "num"
                        elif type(search) == type("1.1"):
                            data_type = "alpha"
                        result.append(
                            {
                                "Location": "Mess",
                                "Datatype": data_type,
                                "Position": (search_mess + 1)
                            }
                        )
                for search_keys in range(0, len(c_keys)):
                    if search == c_keys[search_keys]:
                        result.append(
                            {
                                "Location": "Cluster",
                                "Itemtype": "Key",
                                "Value": c_values[search_keys]
                            }
                        )
                for search_values in range(0, len(c_values)):
                    if search == c_values[search_values]:
                        data_type1 = None
                        if type(search) == type(1.1):
                            data_type1 = "num"
                        elif type(search) == type("1.1"):
                            data_type1 = "alpha"
                        result.append(
                            {
                                "Location": "Cluster",
                                "Itemtype": "Value",
                                "Datatype": data_type1,
                                "Key": c_keys[search_values]
                            }
                        )
                for search_data_space in range(0, len(b_data_space)):
                    if search == b_data_space[search_data_space]:
                        result.append(
                            {
                                "Location": "Book",
                                "Itemtype": "Dataspace",
                                "Position": (search_data_space + 1)
                            }
                        )
                try:
                    for search_text_values in range(0, len(text_file_values[0])):
                        if search == text_file_values[0][search_text_values]:
                            result.append(
                                {
                                    "Location": "Book",
                                    "Itemtype": "Parsed Value",
                                    "Position": (search_text_values + 1)
                                }
                            )
                except IndexError:
                    problems = None
                for search_parsed_values in range(0, len(b_data_space_contents)):
                    for search_each_dataspace in range(0, len(b_data_space_contents[search_parsed_values])):
                        for search_each_value in range(0, len(b_data_space_contents[search_parsed_values][search_each_dataspace])):
                            if search == b_data_space_contents[search_parsed_values][search_each_dataspace][search_each_value]:
                                print("Location: Book\t Itemtype: Parsed Value\tRow: " + str(b_data_space_contents[search_parsed_values].index(b_data_space_contents[search_parsed_values][search_each_dataspace]) + 1) + "\tColumn: " + str(b_data_space_contents[search_parsed_values][search_each_dataspace].index(b_data_space_contents[search_parsed_values][search_each_dataspace][search_each_value]) + 1))
                                result.append(
                                    {
                                        "Location": "Book",
                                        "Itemtype": "Parsed Value",
                                        "Row": (b_data_space_contents[search_parsed_values].index(b_data_space_contents[search_parsed_values][search_each_dataspace]) + 1),
                                        "Column": (b_data_space_contents[search_parsed_values][search_each_dataspace].index(b_data_space_contents[search_parsed_values][search_each_dataspace][search_each_value]) + 1)
                                    }
                                )
            return result

        elif cmd[0] == "dump":
            dump_file = open(cmd[-1], "a+")
            dump_file_text = ""
            for dump_file_loop in range(1, len(cmd) - 1):
                dump_file_text = dump_file_text + cmd[dump_file_loop] + " "
            dump_file_text = dump_file_text[:-1]
            dump_file.write(dump_file_text + "\n")
            dump_file.close()

        elif cmd[0] == "server":
            try:
                if cmd[1] == "connect":
                        self.__SERVER_IP = cmd[2]
                if self.__SERVER_IP == "" and cmd[1] != "update":
                    error(18)
                else:
                    if cmd[1] == "ip":
                        return self.__SERVER_IP
                    elif cmd[1] == "update":
                        if cmd[2] == "mess":
                            self.__set_data("mess")
                        elif cmd[2] == "cluster":
                            self.__set_data("cluster")
                        elif cmd[2] == "all":
                            self.__set_data("mess")
                            self.__set_data("cluster")
                        else:
                            error(19)
                    elif cmd[1] == "fetch":
                        if cmd[2] == "mess":
                            self.__get_data(self.__SERVER_IP, "mess")
                        elif cmd[2] == "cluster":
                            self.__get_data(self.__SERVER_IP, "cluster")
                        elif cmd[2] == "all":
                            self.__get_data(self.__SERVER_IP, "mess")
                            self.__get_data(self.__SERVER_IP, "cluster")
                        else:
                            error(19)
            except:
                error(18)
    # Runs an Explore Script if a valid path is specified.
    def run(self, path):
        try:
            script = open(path, "r", encoding = "utf-8")
            contents = script.readlines()
            # Removes the unwanted characters from the Script.
            contents = del_unwanted(contents)
            for del_line_comments in range(0, len(contents)):
                contents[del_line_comments] = del_line_comm(contents[del_line_comments])
            # Runs each line as an Explore command.
            for run_comm in range(0, len(contents)):
                self.invoke(contents[run_comm])
        except (FileNotFoundError, IsADirectoryError):
            print("Invalid File/Directory.")
        except:
            print("-1")
