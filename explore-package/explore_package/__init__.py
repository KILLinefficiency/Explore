VERSION = 1.0
CODENAME = "Prometheus"
LICENSE = "GNU General Public License v3.0"
AUTHOR = "Shreyas Sable"
REPOSITORY = "https://www.github.com/KILLinefficiency/Explore"

mess = []
cluster = {}


def sort_mess(array):
    for itr in range(0, len(array)):
        for loop in range(0, len(array) - 1):
            if array[loop] > array[loop + 1]:
                array[loop], array[loop + 1] = array[loop + 1], array[loop]


def delete_item(array, index):
    del array[index - 1]


def csv(location, spacing):
    csv_file = open(location, "r", encoding = "utf-8")
    contents = csv_file.readlines()
    for trim in range(0, len(contents)):
        contents[trim] = contents[trim][0:-1]
    first_line = contents[0].split(",")
    for first_index in range(0, len(first_line)):
        print("    " + str(first_line[first_index]), end = str("\t" * spacing))
    print()
    for val in range(1, len(contents)):
        row = contents[val].split(",")
        print(str(val) + ". ", end = " ")
        for itr in range(0, len(row)):
            print(str(row[itr]), end = str("\t" * spacing))
        print()


def starts_with(string, trimmed_string):
    if trimmed_string == string[0:len(trimmed_string)]:
        return True
    else:
        return False


def read_file(location):
    file = open(location, "r", encoding = "utf-8")
    contents = file.read()
    print(contents)
    file.close()


def del_spaces(arr):
    try:
        for trim_spaces in range(0, len(arr)):
            if arr[trim_spaces] == "":
                del arr[trim_spaces]
    except IndexError:
        del_spaces(arr)

def del_comments(commands):
    try:
        for trim_comments in range(0, len(commands)):
            if starts_with(commands[trim_comments], "..."):
                del commands[trim_comments]
    except IndexError:
        del_comments(commands)

def invoke(command):
    try:
        cmd = command.split(" ")
        del_spaces(cmd)

        for add_spaces in range(0, len(cmd)):
            for put_spaces in range(0, len(cmd[add_spaces])):
                if "|" in cmd[add_spaces]:
                    cmd[add_spaces] = cmd[add_spaces].replace("|", " ")

        if (cmd[0] == "about" or cmd[0] == "info") and len(cmd) == 1:
            return {
                "Version": VERSION,
                "Codename": CODENAME,
                "License": LICENSE,
                "Author": AUTHOR,
                "Repository": REPOSITORY
            }

        elif cmd[0] == "disp":
            try:
                disp_data = ""
                for check in range(1, len(cmd)):
                    if not (starts_with(cmd[check], "x_") or (starts_with(cmd[check], "y_"))):
                        disp_data = disp_data + str(cmd[check]) + " "
                    else:
                        if starts_with(cmd[check], "x_"):
                            disp_data = disp_data + str(mess[(int(cmd[check][2:]) - 1)]) + " "
                        elif starts_with(cmd[check], "y_"):
                            disp_data = disp_data + str(cluster[cmd[check][2:]]) + " "
                disp_data = disp_data[:-1]
                print(disp_data)
            except KeyError:
                print(" ")
            except IndexError:
                print(" ")
            except ValueError:
                print(" ")

        elif cmd[0] == "push" and cmd[1] == "num":
            try:
                num_data = ""
                if starts_with(cmd[2], "y_"):
                    num_data = cluster[cmd[2][2:]]
                elif starts_with(cmd[2], "x_"):
                    num_data = mess[int(cmd[2][2:]) - 1]
                else:
                    num_data = cmd[2]
                if len(cmd) == 3 and (starts_with(cmd[2], "x_") or starts_with(cmd[2], "y_")):
                    mess.append(num_data)
                elif len(cmd) == 3 and not (starts_with(cmd[2], "x_") or starts_with(cmd[2], "y_")):
                    mess.append(eval(num_data))
                if len(cmd) == 4 and (starts_with(cmd[2], "x_") or starts_with(cmd[2], "y_")):
                    mess.insert(int(cmd[-1]) - 1, num_data)
                elif len(cmd) == 4 and not (starts_with(cmd[2], "x_") or starts_with(cmd[2], "y_")):
                    num_data = cmd[2]
                    mess.insert(int(cmd[-1]) - 1, eval(num_data))
            except KeyError:
                print("Invalid Key.")

        elif cmd[0] == "push" and cmd[1] == "alpha" and len(cmd) >= 3:
            try:
                data_push = None
                try:
                    if starts_with(cmd[2], "y_"):
                        data_push = cluster[cmd[2][2:]]
                    elif starts_with(cmd[2], "x_"):
                        data_push = mess[int(cmd[2][2:]) - 1]
                    else:
                        data_push = cmd[2]
                except KeyError:
                    print("Invalid Key.")
                if type(int(cmd[-1])) == type(1):
                    insert_data = ""
                    if len(cmd) == 4:
                        insert_data = data_push
                    elif len(cmd) > 4:
                        for insert_data_concat in range(2, len(cmd) - 1):
                            insert_data = insert_data + cmd[insert_data_concat] + " "
                        insert_data = insert_data[:-1]
                    mess.insert(int(cmd[-1]) - 1, insert_data)
            except ValueError:
                push_data = ""
                if len(cmd) == 3:
                    push_data = data_push
                elif len(cmd) > 3:
                    for push_data_concat in range(2, len(cmd)):
                        push_data = push_data + cmd[push_data_concat] + " "
                    push_data = push_data[:-1]
                mess.append(str(push_data))

        elif cmd[0] == "pop":
            if len(cmd) == 1:
                try:
                    delete_item(mess, len(mess))
                except IndexError:
                    print("Item Not Found.")
            elif len(cmd) == 2:
                try:
                    delete_item(mess, int(cmd[1]))
                except IndexError:
                    print("Item Not Found.")

        elif cmd[0] == "mov":
            if cmd[1] == "num":
                try:
                    mov_data = None
                    if starts_with(cmd[2], "y_"):
                        mess[int(cmd[3]) - 1] = cluster[cmd[2][2:]]
                    elif starts_with(cmd[2], "x_"):
                        mess[int(cmd[3]) - 1] = mess[int(cmd[2][2:]) - 1]
                    else:
                        mess[int(cmd[3]) - 1] = eval(cmd[2])
                except IndexError:
                    print("Item Not Found.")
                except KeyError:
                    print("Invalid Key.")
            elif cmd[1] == "alpha":
                try:
                    mov_data = ""
                    if len(cmd) == 4:
                        if starts_with(cmd[2], "y_"):
                            mess[int(cmd[3]) - 1] = cluster[cmd[2][2:]]
                        elif starts_with(cmd[2], "x_"):
                            mess[int(cmd[3]) - 1] = mess[int(cmd[2][2:]) - 1]
                        else:
                            mess[int(cmd[3]) - 1] = cmd[2]
                    if len(cmd) > 4:
                        for mov_data_concat in range(2, len(cmd) - 1):
                            mov_data = mov_data + cmd[mov_data_concat] + " "
                        mov_data = mov_data[:-1]
                        mess[int(cmd[-1]) - 1] = mov_data
                except IndexError:
                    print("Item Not Found.")
                except KeyError:
                    print("Invalid Key.")
            else:
                print("Invalid Syntax.")

        elif cmd[0] == "count" and len(cmd) == 2:
            if cmd[1] == "mess":
                return len(mess)
            elif cmd[1] == "cluster":
                return len(cluster)
            else:
                print("Invalid Syntax.")

        elif cmd[0] == "clean" and len(cmd) == 2:
            if cmd[1] == "mess":
                mess.clear()
            elif cmd[1] == "cluster":
                cluster.clear()
            else:
                print("Invalid Syntax.")

        elif cmd[0] == "getmess":
            for index in range(0, len(mess)):
                print(str(index + 1) + ". " + str(mess[index]))

        elif cmd[0] == "sortmess":
            try:
                if len(cmd) == 2:
                    if cmd[1] == "a" or cmd[1] == "A":
                        sort_mess(mess)
                    elif cmd[1] == "d" or cmd[1] == "D":
                        sort_mess(mess)
                        mess.reverse()
                    else:
                        print("Invalid Argument Passed.")
                else:
                    print("Invalid Syntax.")
            except TypeError:
                print("Can't Sort num And alpha.")

        elif cmd[0] == "calc":
            try:
                equation = ""
                for check in range(1, len(cmd)):
                    if not (starts_with(cmd[check], "x_") or (starts_with(cmd[check], "y_"))):
                        equation = equation + cmd[check]
                    else:
                        if starts_with(cmd[check], "x_"):
                            equation = equation + str((
                                mess[(int(
                                    cmd[check][2:]
                                ) - 1)
                                ]
                            ))
                        elif starts_with(cmd[check], "y_"):
                            equation = equation + str(cluster[cmd[check][2:]])
                return eval(equation)
            except (KeyError, NameError, ValueError, IndexError, ZeroDivisionError, EOFError):
                return 0

        elif cmd[0] == "read":
            try:
                file_address = ""
                if len(cmd) == 2:
                    if cmd[1] == ".cipher" or cmd[1] == ".val":
                        print("Cannot Read System File.")
                    if ((cmd[len(cmd) - 1][-7:-1] + "r") == ".cipher") or (cmd[len(cmd) - 1][-4:-1] + "l" == ".val"):
                        print("Cannot Read System File.")
                    else:
                        file_address = cmd[1]
                elif len(cmd) > 2:
                    if ((cmd[len(cmd) - 1][-6:-1] + "r") == "cipher") or (cmd[len(cmd) - 1][-3:-1] + "l" == "val"):
                        print("Cannot Read System File.")
                    else:
                        for file_address_concat in range(1, len(cmd)):
                            file_address = file_address + cmd[file_address_concat] + " "
                print()
                read_file(file_address)
                print()
            except (FileNotFoundError, IsADirectoryError):
                print("Invalid File/Directory.")

        elif cmd[0] == "csv" and len(cmd) >= 2:
            try:
                csv_spacing = 4
                path = ""
                if len(cmd) == 2:
                    path = cmd[1]
                elif len(cmd) > 2:
                    for path_concat in range(2, len(cmd)):
                        path = path + cmd[path_concat] + " "
                    csv_spacing = int(cmd[1])
                print()
                csv(path, csv_spacing)
                print()
            except (FileNotFoundError, IsADirectoryError):
                print("Invalid File/Directory")

        elif cmd[0] == "export" and cmd[1] == "mess" and len(cmd) >= 3:
            try:
                export_address = ""
                if len(cmd) == 3:
                    export_address = cmd[2]
                else:
                    for itr0 in range(2, len(cmd)):
                        export_address = export_address + cmd[itr0] + " "
                gen_file = open(export_address, "w+", encoding="utf-8")
                for add_log in range(0, len(mess)):
                    if type(mess[add_log]) == type(1.1):
                        gen_file.write(str(mess[add_log]) + " num" + "\n")
                    elif type(mess[add_log]) == type("1.1"):
                        gen_file.write(str(mess[add_log]) + " alpha" + "\n")
                gen_file.close()
            except (FileNotFoundError, IsADirectoryError):
                print("Invalid File/Directory.")

        elif cmd[0] == "export" and cmd[1] == "cluster" and len(cmd) >= 3:
            try:
                cluster_export_address = ""
                if len(cmd) == 3:
                    cluster_export_address = cmd[2]
                else:
                    for cluster_itr in range(2, len(cmd)):
                        cluster_export_address = cluster_export_address + cmd[cluster_itr] + " "
                cluster_gen_file = open(cluster_export_address, "w+", encoding="utf-8")
                cluster_keys = list(cluster.keys())
                cluster_values = list(cluster.values())
                for add_cluster in range(0, len(cluster)):
                    if type(cluster_values[add_cluster]) == type(1.1):
                        cluster_gen_file.write(str(cluster_keys[add_cluster]) + " " + str(cluster_values[add_cluster]) + " num" + "\n")
                    elif type(cluster_values[add_cluster]) == type("1.1"):
                        cluster_gen_file.write(str(cluster_keys[add_cluster]) + " " + str(cluster_values[add_cluster]) + " alpha" + "\n")
                cluster_gen_file.close()
            except (FileNotFoundError, IsADirectoryError):
                print("Invalid File/Directory.")

        elif cmd[0] == "import" and cmd[1] == "mess" and len(cmd) >= 4:
            try:
                import_file_src = ""
                if len(cmd) > 4:
                    for itr in range(3, len(cmd)):
                        import_file_src = import_file_src + cmd[itr] + " "
                else:
                    import_file_src = cmd[3]
                import_file = open(import_file_src, "r", encoding="utf-8")
                contents = import_file.readlines()
                if cmd[2] == "rw":
                    mess.clear()
                if cmd[2] != "rw" and cmd[2] != "w":
                    print("Invalid Import Mode.")
                for lines in range(0, len(contents)):
                    contents[lines] = contents[lines][:-1]
                for split_lines in range(0, len(contents)):
                    types_array = contents[split_lines].split(" ")
                    if types_array[-1] == "num":
                        mess.append(float(types_array[0]))
                    elif types_array[-1] == "alpha":
                        data = ""
                        for data_concat in range(0, len(types_array) - 1):
                            data = data + types_array[data_concat] + " "
                        mess.append(data)
                import_file.close()
            except ValueError:
                print("Import File Is Corrupted.")
            except (FileNotFoundError, IsADirectoryError):
                print("Invalid File/Directory.")

        elif cmd[0] == "import" and cmd[1] == "cluster" and len(cmd) >= 4:
            try:
                cluster_import_file = ""
                if len(cmd) == 4:
                    cluster_import_file = cmd[3]
                else:
                    for itr1 in range(3, len(cmd)):
                        cluster_import_file = cluster_import_file + cmd[itr1] + " "
                c_import_file = open(cluster_import_file, "r", encoding="utf-8")
                cluster_contents = c_import_file.readlines()
                if cmd[2] == "rw":
                    cluster.clear()
                if cmd[2] != "rw" and cmd[2] != "w":
                    print("Invalid Import Mode.")
                for trim_char in range(0, len(cluster_contents)):
                    cluster_contents[trim_char] = cluster_contents[trim_char][:-1]
                for cluster_data in range(0, len(cluster_contents)):
                    cluster_lines = cluster_contents[cluster_data].split(" ")
                    if len(cluster_lines) > 3:
                        join_data = ""
                        for join_data_concat in range(1, len(cluster_lines) - 1):
                            join_data = join_data + cluster_lines[join_data_concat] + " "
                        join_data = join_data[:-1]
                        del cluster_lines[1: -1]
                        cluster_lines.insert(1, join_data)
                    if cluster_lines[-1] == "num":
                        cluster[cluster_lines[0]] = float(cluster_lines[1])
                    elif cluster_lines[-1] == "alpha":
                        cluster[cluster_lines[0]] = str(cluster_lines[1])
            except ValueError:
                print("Import File Is Corrupted.")
            except (FileNotFoundError, IsADirectoryError):
                print("Invalid File/Directory.")

        elif cmd[0] == "set" and len(cmd) >= 4:
            cluster_existing_keys = list(cluster.keys())
            if cmd[1] in cluster_existing_keys:
                print("Key Already Exists.")
            else:
                data_set = None
                try:
                    if starts_with(cmd[3], "x_"):
                        data_set = mess[int(cmd[3][2:]) - 1]
                    else:
                        data_set = cmd[3]
                except IndexError:
                    print("Item Not Found.")
                if cmd[2] == "num":
                    if len(cmd) == 4:
                        if starts_with(cmd[3], "x_"):
                            cluster[cmd[1]] = mess[int(cmd[3][2:]) - 1]
                        elif starts_with(cmd[3], "y_"):
                            cluster[cmd[1]] = cluster[cmd[3][2:]]
                        else:
                            cluster[cmd[1]] = eval(data_set)
                    elif len(cmd) > 4:
                        data_set = ""
                        for set_num_data in range(3, len(cmd)):
                            if starts_with(cmd[set_num_data], "x_"):
                                data_set = data_set + str(mess[int(cmd[set_num_data][2:]) - 1])
                            elif starts_with(cmd[set_num_data], "y_"):
                                data_set = data_set + str(cluster[cmd[set_num_data][2:]])
                            else:
                                data_set = data_set + cmd[set_num_data] + " "
                        cluster[cmd[1]] = eval(data_set)
                elif cmd[2] == "alpha":
                    if len(cmd) == 4:
                        if starts_with(cmd[3], "x_"):
                            cluster[cmd[1]] = mess[int(cmd[3][2:]) - 1]
                        elif starts_with(cmd[3], "y_"):
                            cluster[cmd[1]] = cluster[cmd[3][2:]]
                        else:
                            cluster[cmd[1]] = str(data_set)
                    elif len(cmd) > 4:
                        set_data = ""
                        for set_data_concat in range(3, len(cmd)):
                            set_data = set_data + cmd[set_data_concat] + " "
                        set_data = set_data[:-1]
                        cluster[cmd[1]] = set_data

        elif cmd[0] == "getcluster":
            if len(cluster) > 0:
                if len(cmd) == 1:
                    cluster_items = list(cluster.items())
                    print("Key : Value\n")
                    for items in range(0, len(cluster)):
                        print(cluster_items[items][0], cluster_items[items][1], sep = " : ")
                elif len(cmd) == 2 and cmd[1] == "keys":
                    keys = list(cluster.keys())
                    print("Key : \n")
                    for list_keys in range(0, len(keys)):
                        print(str(keys[list_keys]) + " : ")
                elif len(cmd) == 2 and cmd[1] == "values":
                    values = list(cluster.values())
                    print(": Value\n")
                    for list_values in range(0, len(values)):
                        print(" : " + str(values[list_values]))
                else:
                    print("Invalid Syntax.")

        elif cmd[0] == "change" and len(cmd) >= 4:
            cluster_keys = list(cluster.keys())
            if cmd[1] in cluster_keys:
                try:
                    change_value = None
                    if starts_with(cmd[3], "x_"):
                        change_value = mess[int(cmd[3][2:]) - 1]
                    elif starts_with(cmd[3], "y_"):
                        change_value = cluster[cmd[3][2:]]
                    else:
                        change_value = cmd[3]
                except IndexError:
                    print("Item Not Found.")
                except KeyError:
                    print("Invalid Key.")
                try:
                    if cmd[2] == "num":
                        cluster[cmd[1]] = float(change_value)
                    elif cmd[2] == "alpha":
                        if len(cmd) == 4:
                            cluster[cmd[1]] = change_value
                        elif len(cmd) > 4:
                            changed_data = ""
                            for changed_data_concat in range(3, len(cmd)):
                                changed_data = changed_data + cmd[changed_data_concat] + " "
                            changed_data = changed_data[:-1]
                            cluster[cmd[1]] = changed_data
                    else:
                        print("Invalid Syntax.")
                except ValueError:
                    print("Invalid Datatypes.")
            else:
                print("Invalid Key.")

        elif cmd[0] == "get":
            try:
                if cmd[1] == "cluster":
                    return cluster[cmd[2]]
                elif cmd[1] == "mess":
                    return mess[int(cmd[2]) - 1]
            except (KeyError, IndexError):
                return None

        elif cmd[0] == "rem" and len(cmd) >= 1:
            if len(cmd) == 1:
                try:
                    cluster_keys1 = list(cluster.keys())
                    del cluster[cluster_keys1[-1]]
                except IndexError:
                    pass
            else:
                try:
                    del cluster[cmd[1]]
                except KeyError:
                    print("Invalid Key.")

        elif cmd[0] == "find" and len(cmd) >= 3:
            search = None
            results = []
            try:
                if cmd[1] == "num":
                    search = float(cmd[2])
                else:
                    if len(cmd) == 3 and cmd[1] == "alpha":
                        search = str(cmd[2])
                    elif len(cmd) > 3 and cmd[1] == "alpha":
                        search_data = ""
                        for search_concat in range(2, len(cmd)):
                            search_data = search_data + cmd[search_concat] + " "
                        search = search_data[:-1]
            except (ValueError, TypeError):
                print("Invalid Datatype.")
            c_keys = list(cluster.keys())
            c_values = list(cluster.values())
            if not (search in c_keys) and not (search in c_values) and not (search in mess):
                pass
            else:
                data_type = None
                for search_mess in range(0, len(mess)):
                    if search == mess[search_mess]:
                        if type(search) == type(1.1):
                            data_type = "num"
                        elif type(search) == type("1.1"):
                            data_type = "alpha"
                        results.append({
                            "Location": "Mess",
                            "Datatype": data_type,
                            "Position": search_mess + 1
                        })
                for search_keys in range(0, len(c_keys)):
                    if search == c_keys[search_keys]:
                        results.append({
                            "Location": "Cluster",
                            "Itemtype": "Key",
                            "Value": c_values[search_keys]
                        })
                for search_values in range(0, len(c_values)):
                    if search == c_values[search_values]:
                        data_type1 = None
                        if type(search) == type(1.1):
                            data_type1 = "num"
                        elif type(search) == type("1.1"):
                            data_type1 = "alpha"
                        results.append({
                            "Location": "Cluster",
                            "Itemtype": "Value",
                            "Datatype": data_type1,
                            "Key": c_keys[search_values]
                        })
                return results

        elif cmd[0] == "":
            pass

        else:
            print("Invalid Command: " + str(command))

    except NameError:
        pass
    except SyntaxError:
        print("Invalid Syntax.")
    except:
        print("Oops! Something Went Wrong.")

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
