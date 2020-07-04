import cipher
import lib
import memory_structures as ms
import limit
import error as err

SERVER_IP = ""
CSV_FS = ","
CSV_SPACING = 4


exit_comms = ["exit", "exit.", "bye", "bye."]

# The code for shell begins here.

flag = True
logging = True
log = open("log.txt", "a+", encoding = "utf-8")
# Declares empty list and dictionaries for the Mess, the Cluster and the Book respectively.
book = {}
# Sets up the expression that appears on the prompt.
expression = ":) > "
expressions = [":) > ", ";) > ", ":| > ", ":( > ", ":D > ", ":P > ", ":O > "]

# Starts the infinite loop where the prompt appears again and again
# for interpreting commands
lib.explore_splash()
while flag:
    commands = list(limit.cmd_requests.keys())
    limit_commands = list(limit.cmd_limit.keys())
    try:
        escape_log = False
        command = input(expression)
        command = command.replace("\t", " ")
        if command[0] == " ":
            escape_log = True
        command = command.strip()
        cmd = command.split(" ")

        # For replacing the referred values from the Mess, the Cluster and the Book.
        try:
            for replace_ref in range(0, len(cmd)):
                # For referred values from the Mess.
                if lib.starts_with(cmd[replace_ref], "x_"):
                    cmd[replace_ref] = str(ms.get_from_mess(int(cmd[replace_ref][2:])))
                # For referred values from the Cluster.
                elif lib.starts_with(cmd[replace_ref], "y_"):
                    cmd[replace_ref] = str(ms.get_from_cluster(cmd[replace_ref][2:]))
                # For referred values from the Book.
                elif lib.starts_with(cmd[replace_ref], "b_"):
                    info_address = cmd[replace_ref][2:].split("->")
                    if book[info_address[0]][0] == "text":
                        cmd[replace_ref] = str(book[info_address[0]][1][int(info_address[1]) - 1])
                    elif book[info_address[0]][0] == "csv":
                        cmd[replace_ref] = str(book[info_address[0]][1][int(info_address[1]) - 1][int(info_address[2]) - 1])
        except (KeyError, ValueError, IndexError):
            err.error(4)
            continue

        if not (len(command) == 0) and not (escape_log):
            log.write(command + "\n")

        # Removes the extra unwanted spaces from the command.
        cmd = lib.del_spaces(cmd)

        # Replaces the pipe character ("|") with space (" ").
        for add_spaces in range(0, len(cmd)):
            for put_spaces in range(0, len(cmd[add_spaces])):
                # Searches for pipe ("|").
                if "|" in cmd[add_spaces]:
                    # Replaces all the pipe characters ("|") with space characters (" ").
                    cmd[add_spaces] = cmd[add_spaces].replace("|", " ")
        
        # Return back to the prompt if no command is entered.
        if len(cmd) == 0:
            continue

        try:
            if (cmd[0] in commands) and (cmd[0] in limit_commands) and (len(cmd) != 0):
                if limit.cmd_requests[cmd[0]] == limit.cmd_limit[cmd[0]]:
                    err.error(5)
                    continue
        except KeyError:
            continue

        if cmd[0] in limit_commands:
            limit.incr_limit_count(cmd[0])

        if cmd[0] == "limit":
            try:
                if cmd[1] == "enable":
                    if cmd[2] == "all":
                        for limit_all in range(0, len(limit.total_commands)):
                            limit.set_limit(limit.total_commands[limit_all], int(eval(lib.join_string(cmd, 3, len(cmd) - 1))))
                    elif cmd[2] != "all":
                        limit.set_limit(cmd[2], int(eval(lib.join_string(cmd, 3, len(cmd) - 1))))
                elif cmd[1] == "disable":
                    if cmd[2] == "all":
                        limit.rem_limit(list(limit.cmd_limit.keys()))
                    elif cmd[2] != "all":
                        limit.rem_limit(cmd[2:])
                elif cmd[1] == "status":
                    if cmd[2] == "all":
                        limit.limit_status(limit.total_commands)
                    elif cmd[2] != "all":
                        limit.limit_status(cmd[2:])
            except IndexError:
                continue

        elif (cmd[0] in exit_comms) and len(cmd) == 1:
            print("\nBye.\n")
            break

        elif (cmd[0] == "about" or cmd[0] == "info") and len(cmd) == 1:
            lib.explore_splash()
            print("\nExplore v3.0\nCodename: Kal-El\nLicense: GNU General Public License v3.0\nAuthor: Shreyas Sable\nRepository: https://www.github.com/KILLinefficiency/Explore\n")

        elif cmd[0] == "clear" and len(cmd) == 1:
            lib.clear_screen()
        
        # Displays text and data.
        elif cmd[0] == "disp":
            disp_data = lib.join_string(cmd, 1, len(cmd) - 1)
            print(disp_data)

        # Pushes numeric data items into the mess.
        elif cmd[0] == "push" and cmd[1] == "num":
            try:
                # Pushes numeric data to the Mess.
                num_data = cmd[2]
                if len(cmd) == 3:
                    ms.add_mess(num_data, "num")
                # Pushes numeric data to the Mess at a particular position.
                if len(cmd) == 4:
                    ms.insert_mess(eval(num_data), "num", int(cmd[-1]))
            except ValueError:
                    err.error(6)
            except KeyError:
                err.error(2)

        # Pushes alphabetic data items into the mess.
        elif cmd[0] == "push" and cmd[1] == "alpha" and len(cmd) >= 3:
            try:
                try:
                    data_push = cmd[2]
                    # Pushes the data item at a particular index in the mess.
                    if type(int(cmd[-1])) == type(1):
                        insert_data = lib.join_string(cmd, 2, len(cmd) - 2)
                        ms.insert_mess(insert_data, "alpha", int(cmd[-1]))
                # Pushes the data item at the last position in the mess.
                except ValueError:
                    push_data = lib.join_string(cmd, 2, len(cmd) - 1)
                    ms.add_mess(push_data, "alpha")
            except ValueError:
                    err.error(6)
            except KeyError:
                err.error(2)

        # Deletes data items from the mess.
        elif cmd[0] == "pop":
            try:
                ms.pop_from_mess(cmd[1:])
            except IndexError:
                continue

        # Replaces the current data item of the given index with the supplied numeric data item in the Mess.
        elif cmd[0] == "mov":
            if cmd[1] == "num":
                mov_data = ""
                for join_mov_data in range(2, len(cmd) - 1):
                    mov_data = mov_data + lib.del_left_zeros(cmd[join_mov_data]) + " "
                mov_data = mov_data[:-1]
                ms.move_in_mess(mov_data, "num", int(cmd[-1]))
            elif cmd[1] == "alpha":
                # Replaces the current data item of the given index with the supplied alphabetic data item.
                try:
                    mov_data = lib.join_string(cmd, 2, len(cmd) - 2)
                    ms.move_in_mess(mov_data, "alpha", int(cmd[-1]))
                except ValueError:
                        err.error(6)
                except IndexError:
                    err.error(8)
                except KeyError:
                    err.error(2)
            else:
                    err.error(9)

        # Displays the number of data items in the Mess, the Cluster and the Book.
        elif cmd[0] == "count" and len(cmd) == 2:
            if cmd[1] == "mess":
                print(ms.count_mess())
            elif cmd[1] == "cluster":
                print(ms.count_cluster())
            elif cmd[1] == "book":
                print(len(book))
            else:
                err.error(9)

        # Deletes all the data items of the Mess, the Cluster and the Book.
        elif cmd[0] == "clean":
            clean_list = cmd[1:]
            if "mess" in clean_list:
                ms.clean_mess()
            if "cluster" in clean_list:
                ms.clean_cluster()
            if "book" in clean_list:
                book.clear()

        # Displays all the data items fom the Mess.
        elif cmd[0] == "getmess":
            mess_values = ms.gen_mess_list()
            if len(mess_values) > 0:
                print()
                for index in range(0, len(mess_values)):
                    print(str(index + 1) + ". " + str(mess_values[index]))
                print()

        # Displays the result of the supplied mathematical expression.
        elif cmd[0] == "calc":
            try:
                equation = ""
                # Concatenates the operators and the numeric values.
                for check in range(1, len(cmd)):
                    equation = equation + lib.del_left_zeros(cmd[check])
                maths_answer = eval(equation)
                if maths_answer == True:
                    print("Yes. (1)")
                elif maths_answer == False:
                    print("No. (0)")
                else:
                    print(maths_answer)
            except ValueError:
                    err.error(6)
            except IndexError:
                err.error(8)
            except ZeroDivisionError:
                err.error(10)
            except EOFError:
                err.error(11)

        # Changes the expression of the Explore prompt.
        elif cmd[0] == "exp":
            try:
                # Lists all the Explore prompt expressions.
                if len(cmd) == 1:
                    for list_exp in range(0, len(expressions)):
                        print(str(list_exp + 1) + ". " + expressions[list_exp])
                # Sets the expression corresponding to the number passed by the user.
                else:
                    expression = expressions[int(cmd[1]) - 1]
            except IndexError:
                pass

        # Displays all of the parsed data in an organized way. 
        elif cmd[0] == "getbook" and len(cmd) == 1:
            # Gets the data labels of all the parsed data.
            book_keys = list(book.keys())
            if len(book_keys) == 0:
                continue
            else:
                for itr_book in range(0, len(book_keys)):
                    # Displays the label of the parsed data and the contents
                    # in an organized way.
                    print()
                    print(str(book_keys[itr_book]) + ": ")
                    print()
                    if book[book_keys[itr_book]][0] == "csv":
                        lib.disp_list(book[book_keys[itr_book]][1])
                    elif book[book_keys[itr_book]][0] == "text":
                        lib.read_list(book[book_keys[itr_book]][1])
                print()
                
        # Reads the log.txt file which contains the history of all previously entered commands.
        elif cmd[0] == "getlog" and len(cmd) == 1:
            lib.read_log()

        # Reads a text-containing file using read_file from lib.py.
        elif cmd[0] == "read":
            try:
                file_address = lib.join_string(cmd, 1, len(cmd) - 1)
                print()
                lib.read_file(file_address)
                print()
            except (FileNotFoundError, IsADirectoryError):
                err.error(13)

        # Reads a .csv file using csv() from lib.py
        elif cmd[0] == "csv" and len(cmd) >= 2:
            try:
                if cmd[1] == "config":
                    if cmd[2] == "fs":
                        new_csv_fs = lib.join_string(cmd, 3, len(cmd) - 1)
                        CSV_FS = new_csv_fs
                    elif cmd[2] == "tab":
                        CSV_SPACING = int(eval(lib.join_string(cmd, 3, len(cmd) - 1)))
                else:
                    path = lib.join_string(cmd, 1, len(cmd) - 1)
                    print()
                    lib.csv(path, CSV_SPACING, CSV_FS)
                    print()
            except (FileNotFoundError, IsADirectoryError):
                err.error(13)
        
        # Writes the parsed data from a file to the Book.
        elif cmd[0] == "book" and len(cmd) >= 4:
            try:
                path = lib.join_string(cmd, 3, len(cmd) - 1)
                # Gets the data labels from the Book.
                book_keys = list(book.keys())
                # For parsing a CSV file.
                if cmd[1] == "csv":
                    # Writes the parsed data with the given key only if
                    # the provided data label does not already exist in
                    # the Book. 
                    if not(cmd[2] in book_keys):
                        print()
                        lib.csv(path, 1, CSV_FS)
                        print()
                        book[cmd[2]] = ["csv", lib.parse_csv(path, CSV_FS)]
                    else:
                        err.error(14)
                elif cmd[1] == "text":
                    if not(cmd[2] in book_keys):
                        print()
                        lib.read_file(path)
                        print()
                        book[cmd[2]] = ["text", lib.parse_file(path)]
                    else:
                        err.error(14)
            except (FileNotFoundError, IsADirectoryError):
                err.error(13)

        elif cmd[0] == "export" and cmd[1] == "mess" and len(cmd) >= 3:
            try:
                back_char = 1
                if lib.starts_with(cmd[-1], "e_"):
                    back_char = 2
                    e_m_key = int(cmd[-1][2:])
                mess_export_address = lib.join_string(cmd, 2, len(cmd) - back_char)
                mess_export_file = open(mess_export_address, "w+", encoding = "utf-8")
                if lib.starts_with(cmd[-1], "e_"):
                    mess_export_file.write(cipher.enc_dec(ms.mess, e_m_key))
                else:
                    mess_export_file.write(ms.mess)
                mess_export_file.close()
            except (FileNotFoundError, IsADirectoryError):
                err.error(13)

        elif cmd[0] == "export" and cmd[1] == "cluster" and len(cmd) >= 3:
            try:
                back_char = 1
                if lib.starts_with(cmd[-1], "e_"):
                    back_char = 2
                    e_c_key = int(cmd[-1][2:])
                cluster_export_address = lib.join_string(cmd, 2, len(cmd) - back_char)
                cluster_export_file = open(cluster_export_address, "w+", encoding = "utf-8")
                if lib.starts_with(cmd[-1], "e_"):
                    cluster_export_file.write(cipher.enc_dec(ms.cluster, e_c_key))
                else:
                    cluster_export_file.write(ms.cluster)
                cluster_export_file.close()
            except (FileNotFoundError, IsADirectoryError):
                err.error(13)

        elif cmd[0] == "import" and cmd[1] == "mess" and len(cmd) >= 4:
            try:
                back_char = 1
                if not (cmd[2] == "w" or cmd[2] == "rw"):
                    err.error(15)
                    continue
                if cmd[2] == "rw":
                    ms.clean_mess()
                if lib.starts_with(cmd[-1], "d_"):
                    back_char = 2
                    d_m_key = int(cmd[-1][2:])
                mess_import_address = lib.join_string(cmd, 3, len(cmd) - back_char)
                mess_import_file = open(mess_import_address, "r", encoding = "utf-8")
                mess_contents = mess_import_file.read()
                if lib.starts_with(cmd[-1], "d_"):
                    ms.add_to_ms_directly_unsafe(cipher.enc_dec(mess_contents, d_m_key), "mess")
                else:
                    ms.add_to_ms_directly_safe(mess_contents, "mess")
            except (FileNotFoundError, IsADirectoryError):
                err.error(13)

        elif cmd[0] == "import" and cmd[1] == "cluster" and len(cmd) >= 4:
            try:
                back_char = 1
                if not (cmd[2] == "w" or cmd[2] == "rw"):
                    err.error(15)
                    continue
                if cmd[2] == "rw":
                    ms.clean_cluster()
                if lib.starts_with(cmd[-1], "d_"):
                    back_char = 2
                    d_c_key = int(cmd[-1][2:])
                cluster_import_address = lib.join_string(cmd, 3, len(cmd) - back_char)
                cluster_import_file = open(cluster_import_address, "r", encoding = "utf-8")
                cluster_contents = cluster_import_file.read()
                if lib.starts_with(cmd[-1], "d_"):
                    ms.add_to_ms_directly_unsafe(cipher.enc_dec(cluster_contents, d_c_key), "cluster")
                else:
                    ms.add_to_ms_directly_safe(cluster_contents, "cluster")
            except (FileNotFoundError, IsADirectoryError):
                err.error(13)

        # Sets a data item as a value to a key in the cluster
        elif cmd[0] == "set" and len(cmd) >= 4:
            try:
                # Gets the list of all the existing keys in the cluster.
                cluster_existing_keys = ms.gen_cluster_keys()
                # Does not allow the user to set a value to key which already has a value.
                if cmd[1] in cluster_existing_keys:
                    err.error(16)
                    continue
                else:
                    data_set = cmd[3]
                    # Sets a numeric value to a key.
                    if cmd[2] == "num":
                        if len(cmd) == 4:
                            ms.add_cluster(cmd[1], float(eval(data_set)), "num")
                        # Evaluates a mathematical expression.
                        elif len(cmd) > 4:
                            data_set = ""
                            for set_num_data in range(3, len(cmd)):
                                data_set = data_set + lib.del_left_zeros(cmd[set_num_data]) + " "
                            ms.add_cluster(cmd[1], float(eval(data_set)), "num")
                    # Sets a alphabetic value to a key.
                    elif cmd[2] == "alpha":
                        data_set = ""
                        data_set = lib.join_string(cmd, 3, len(cmd) - 1)
                        ms.add_cluster(cmd[1], str(data_set), "alpha")
                    else:
                        continue
            except (NameError, ValueError):
                    err.error(6)

        elif cmd[0] == "getcluster":
            existing_keys = ms.gen_cluster_keys()
            if len(existing_keys) > 0:
                # Displays the entire cluster.
                if len(cmd) == 1:
                    print("\nKey : Value\n")
                    for items in range(0, len(existing_keys)):
                        # Displays each key and value for the list "cluster_items"
                        # and is separated by " : ".
                        print(existing_keys[items], ms.get_from_cluster(existing_keys[items]), sep = " : ")
                    print()

                # Displays only the keys from the cluster.
                elif len(cmd) == 2 and cmd[1] == "keys":
                    keys = ms.gen_cluster_keys()
                    print("\nKey :\n")
                    for list_keys in range(0, len(keys)):
                        print(str(keys[list_keys]) + " :")
                    print()
                # Displays only the values from the cluster.
                elif len(cmd) == 2 and cmd[1] == "values":
                    keys = ms.gen_cluster_keys()
                    print("\n: Value\n")
                    for list_values in range(0, len(keys)):
                        print(": " + str(ms.get_from_cluster(keys[list_values])))
                    print()
                else:
                    err.error(9)
            else:
                continue

        # Changes the value of the supplied key.
        elif cmd[0] == "change" and len(cmd) >= 4:
            cluster_keys = ms.gen_cluster_keys()
            # Checks if the supplied key exists or not.
            if cmd[1] in cluster_keys:
                # For typecasting and for the values which contain spaces.
                try:
                    if cmd[2] == "num":
                        change_value = ""
                        for join_change_value in range(3, len(cmd)):
                            change_value = change_value + lib.del_left_zeros(cmd[join_change_value]) + " "
                        change_value = change_value[:-1]
                        ms.change_in_cluster(cmd[1], float(change_value), "num")
                    elif cmd[2] == "alpha":
                        change_value = lib.join_string(cmd, 3, len(cmd) - 1)
                        ms.change_in_cluster(cmd[1], change_value, "alpha")
                    else:
                        err.error(9)
                except ValueError:
                        err.error(6)
            else:
                err.error(2)

        # Gets a value from the Cluster, the Mess or the Book.
        elif cmd[0] == "get":
            try:
                if cmd[1] == "mess":
                    print(ms.get_from_mess(int(cmd[2])))
                elif cmd[1] == "cluster":
                    if ms.get_from_cluster(cmd[2]) != None:
                        print(ms.get_from_cluster(cmd[2]))
                    else:
                        err.error(8)
                elif cmd[1] == "book":
                    # Gets parsed CSV data.
                    if len(cmd) == 5:
                        print(str(book[cmd[2]][1][int(cmd[3]) - 1][int(cmd[4]) - 1]))
                    elif len(cmd) == 4:
                        print(str(book[cmd[2]][1][int(cmd[3]) - 1]))
            except (IndexError, KeyError):
                err.error(8)

        # Removes a data item from the cluster.
        elif cmd[0] == "rem" and len(cmd) >= 1:
            try:
                cluster_keys = ms.gen_cluster_keys()
                # Removes the last data item from the cluster if the key is not supplied.
                if len(cmd) == 1:
                    ms.rem_from_cluster(cluster_keys[-1])
                # Removes one or multiple data item(s) from the cluster with the key(s) supplied.
                else:
                    rem_items = cmd[1:]
                    for rem_several in range(0, len(rem_items)):
                        try:
                            ms.rem_from_cluster(rem_items[rem_several])
                        except (KeyError, IndexError):
                            continue
            except KeyError:
                continue

        elif cmd[0] == "find" and len(cmd) >= 3:
            # Sets the variable for the item to be found to None.
            search = None
            try:
                # Sets a numeric value to be searched.
                if cmd[1] == "num":
                    search = float(cmd[2])
                elif len(cmd) >= 3 and cmd[1] == "alpha":
                    search = lib.join_string(cmd, 2, len(cmd) - 1)
            except (ValueError, TypeError):
                err.error(6)
                continue
            # Generates separate lists for Cluster keys and values.
            m_values = ms.gen_mess_list()
            c_keys = ms.gen_cluster_keys()
            c_values = ms.gen_cluster_key_values()
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
                err.error(17)
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
                try:
                    for search_text_values in range(0, len(text_file_values[0])):
                        if search == text_file_values[0][search_text_values]:
                            print("Location: Book\t Itemtype: Parsed Value\t Position: " + str(search_text_values + 1))
                except IndexError:
                    problems = None
                # Searches for the particular data item and the data space and outputs it's information.
                for search_parsed_values in range(0, len(b_data_space_contents)):
                    for search_each_dataspace in range(0, len(b_data_space_contents[search_parsed_values])):
                        for search_each_value in range(0, len(b_data_space_contents[search_parsed_values][search_each_dataspace])):
                            if search == b_data_space_contents[search_parsed_values][search_each_dataspace][search_each_value]:
                                print("Location: Book\t Itemtype: Parsed Value\tRow: " + str(b_data_space_contents[search_parsed_values].index(b_data_space_contents[search_parsed_values][search_each_dataspace]) + 1) + "\tColumn: " + str(b_data_space_contents[search_parsed_values][search_each_dataspace].index(b_data_space_contents[search_parsed_values][search_each_dataspace][search_each_value]) + 1))
        # Return back to the prompt if no command is entered.
        elif len(command) == 0:
            continue

        # Writes custom text to a file. (Does not overwrites the text if something is already written)
        elif cmd[0] == "dump":
            # Opens the file in "append" mode.
            dump_file = open(cmd[-1], "a+")
            dump_file_text = ""
            # Concatenates all the text to be written.
            for dump_file_loop in range(1, len(cmd) - 1):
                dump_file_text = dump_file_text + cmd[dump_file_loop] + " "
            # Removes the extra unwanted space character (" ") from the end.
            dump_file_text = dump_file_text[:-1]
            # Writes with a new line.
            dump_file.write(dump_file_text + "\n")
            dump_file.close()

        elif cmd[0] == "server":
            if cmd[1] == "connect":
                    SERVER_IP = cmd[2]
            if SERVER_IP == "" and cmd[1] != "update":
                err.error(18)
            else:
                if cmd[1] == "ip":
                    print("Connected to: " + SERVER_IP)
                elif cmd[1] == "update":
                    if cmd[2] == "mess":
                        ms.set_data("mess")
                    elif cmd[2] == "cluster":
                        ms.set_data("cluster")
                    elif cmd[2] == "all":
                        ms.set_data("mess")
                        ms.set_data("cluster")
                    else:
                        err.error(19)
                elif cmd[1] == "fetch":
                    if cmd[2] == "mess":
                        ms.get_data(SERVER_IP, "mess")
                    elif cmd[2] == "cluster":
                        ms.get_data(SERVER_IP, "cluster")
                    elif cmd[2] == "all":
                        ms.get_data(SERVER_IP, "mess")
                        ms.get_data(SERVER_IP, "cluster")
                    else:
                        err.error(19)

        # Show a "Invalid Command" message if wrong command is entered.
        else:
            print("Invalid Command: " + str(command))
            continue

    except EOFError:
        err.error(9)
        continue

    except ValueError:
        err.error(6)
        continue

    except IndexError:
        print("Missing Arguments or Extra Arguments.")

    except ConnectionError:
        err.error(18)

    except KeyboardInterrupt:
        print("\n\nBye.")
        break
    except:
        print("-1")
        continue
log.close()