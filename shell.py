import login
import lib

flag = True
logging = True
log = open("log.txt", "a", encoding = "utf-8")
# Declares empty list and dictionary for mess and cluster respectively.
mess = []
cluster = {}
# Sets up the expression that appears on the prompt.
expression = ":) > "

# Starts the infinite loop where the prompt appears again and again
# for interpreting commands
while flag:
    try:
        command = input(expression)
        cmd = command.split(" ")

        # Removes the extra unwanted spaces from the command.
        lib.del_spaces(cmd)

        # Replaces the pipe character ("|") with space (" ").
        for add_spaces in range(0, len(cmd)):
            for put_spaces in range(0, len(cmd[add_spaces])):
                # Searches for pipe ("|").
                if "|" in cmd[add_spaces]:
                    # Replaces all the pipe characters ("|") with space characters (" ").
                    cmd[add_spaces] = cmd[add_spaces].replace("|", " ")

        # Writes the entered command to log.txt file.
        if not (len(command) == 0):
            log.write(command + "\n")

        # Return back to the prompt if no command is entered.
        if len(command) == 0:
            continue

        elif (cmd[0] == "exit" or cmd[0] == "bye" or cmd[0] == "exit." or cmd[0] == "bye.") and len(cmd) == 1:
            print("\nBye.\n")
            break

        elif (cmd[0] == "about" or cmd[0] == "info") and len(cmd) == 1:
            print("\nExplore v1.0\nCodename: Prometheus\nLicense: GNU General Public License v3.0\nAuthor: Shreyas Sable\nRepository: https://www.github.com/KILLinefficiency/Explore\n")

        elif cmd[0] == "disp":
            try:
                disp_data = ""
                for check in range(1, len(cmd)):
                    # Concatenates the entered text which is not a reference a mes or cluster value.
                    if not(lib.starts_with(cmd[check], "x_") or (lib.starts_with(cmd[check], "y_"))):
                        disp_data = disp_data + str(cmd[check]) + " "
                    # Concatenates the values of the mess and cluster items.
                    else:
                        if lib.starts_with(cmd[check], "x_"):
                            # Concatenates the item from mess of the index followed by "x_".
                            disp_data = disp_data + str(mess[(int(
                                                        cmd[check][2:]
                                                            ) - 1)
                                                    ]) + " "

                        # Concatenates the item from cluster of the key followed by "y_".
                        elif lib.starts_with(cmd[check], "y_"):
                            disp_data = disp_data + str(cluster[cmd[check][2:]]) + " "
                disp_data = disp_data[:-1]
                print(disp_data)
            except KeyError:
                print(" ")
            except IndexError:
                print(" ")
            except ValueError:
                print(" ")

        # Pushes numeric data items into the mess.
        elif cmd[0] == "push" and cmd[1] == "num":
            try:
                num_data = ""
                if lib.starts_with(cmd[2], "y_"):
                    num_data = cluster[cmd[2][2:]]
                elif lib.starts_with(cmd[2], "x_"):
                    num_data = mess[int(cmd[2][2:]) - 1]
                else:
                    num_data = cmd[2]
                # Pushes the number passed.
                if len(cmd) == 3 and (lib.starts_with(cmd[2], "x_") or lib.starts_with(cmd[2], "y_")):
                    mess.append(num_data)
                elif len(cmd) == 3 and not(lib.starts_with(cmd[2], "x_") or lib.starts_with(cmd[2], "y_")):
                    mess.append(eval(num_data))
                # Pushes the result of the expression passed.
                if len(cmd) == 4 and (lib.starts_with(cmd[2], "x_") or lib.starts_with(cmd[2], "y_")):
                    mess.insert(int(cmd[-1]) - 1, num_data)
                elif len(cmd) == 4 and not(lib.starts_with(cmd[2], "x_") or lib.starts_with(cmd[2], "y_")):
                    num_data = cmd[2]
                    mess.insert(int(cmd[-1]) - 1, eval(num_data))
            except KeyError:
                print("Invalid Key.")

        # Pushes alphabetic data items into the mess.
        elif cmd[0] == "push" and cmd[1] == "alpha" and len(cmd) >= 3:
            try:
                # Sets the variable for the data to be pushed to None.
                data_push = None
                try:
                    # Checks of the value passed is a reference to a data item in the Cluster.
                    if lib.starts_with(cmd[2], "y_"):
                        # Sets the value of the data_push variable to the referred value in the Cluster.
                        data_push = cluster[cmd[2][2:]]
                    elif lib.starts_with(cmd[2], "x_"):
                        # Sets the value of the data_push variable to the referred value in the Mess.
                        data_push = mess[int(cmd[2][2:]) - 1]
                    else:
                        # Sets the value to the passed in value.
                        data_push = cmd[2]
                except KeyError:
                    print("Invalid Key.")
                    continue
                # Pushes the data item at a particular index in the mess.
                if type(int(cmd[-1])) == type(1):
                    insert_data = ""
                    # For data without spaces.
                    if len(cmd) == 4:
                        insert_data = data_push
                    # For data with spaces
                    elif len(cmd) > 4:
                        for insert_data_concat in range(2, len(cmd) - 1):
                            insert_data = insert_data + cmd[insert_data_concat] + " "
                        # Removes the extra space (" ") at the end.
                        insert_data = insert_data[:-1]
                    mess.insert(int(cmd[-1]) - 1, insert_data)
            # Pushes the data item at the last position in the mess.
            except ValueError:
                push_data = ""
                # For data without spaces.
                if len(cmd) == 3:
                    push_data = data_push
                # For data with spaces.
                elif len(cmd) > 3:
                    for push_data_concat in range(2, len(cmd)):
                        push_data = push_data + cmd[push_data_concat] + " "
                    # Removes the extra space (" ") at the end.
                    push_data = push_data[:-1]
                mess.append(str(push_data))

        # Deletes data items from the mess.
        elif cmd[0] == "pop":
            # Deletes the last data item of the mess using delete_item() from lib.py.
            if len(cmd) == 1:
                try:
                    lib.delete_item(mess, len(mess))
                except IndexError:
                    continue
            # Deletes a particular data item of the given index using delete_item() from lib.py.
            elif len(cmd) == 2:
                try:
                    lib.delete_item(mess, int(cmd[1]))
                except IndexError:
                    print("Item Not Found.")

        # Replaces the current data item of the given index with the supplied numeric data item in the Mess.
        elif cmd[0] == "mov":
            if cmd[1] == "num":
                try:
                    mov_data = None
                    if lib.starts_with(cmd[2], "y_"):
                        mess[int(cmd[3]) - 1] = cluster[cmd[2][2:]]
                    elif lib.starts_with(cmd[2], "x_"):
                        mess[int(cmd[3]) - 1] = mess[int(cmd[2][2:]) - 1]
                    else:
                        mess[int(cmd[3]) - 1] = eval(cmd[2])
                except IndexError:
                    print("Item Not Found.")
                except KeyError:
                    print("Invalid Key.")
            elif cmd[1] == "alpha":
                # Replaces the current data item of the given index with the supplied alphabetic data item.
                try:
                    mov_data = ""
                    # For data item with and without spaces.
                    if len(cmd) == 4:
                        if lib.starts_with(cmd[2], "y_"):
                            mess[int(cmd[3]) - 1] = cluster[cmd[2][2:]]
                        elif lib.starts_with(cmd[2], "x_"):
                            mess[int(cmd[3]) - 1] = mess[int(cmd[2][2:]) - 1]
                        else:
                            mess[int(cmd[3]) - 1] = cmd[2]
                    if len(cmd) > 4:
                        # This loop will run only once if no spaces are present in the data item.
                        # And for multiple times if the data item contains spaces.
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


        # Displays the number of data items in Mess and Cluster.
        elif cmd[0] == "count" and len(cmd) == 2:
            if cmd[1] == "mess":
                print(len(mess))
            elif cmd[1] == "cluster":
                print(len(cluster))
            else:
                print("Invalid Syntax.")

        # Deletes all the data items of the Mess and the Cluster.
        elif cmd[0] == "clean" and len(cmd) == 2:
            if cmd[1] == "mess":
                mess.clear()
            elif cmd[1] == "cluster":
                cluster.clear()
            else:
                print("Invalid Syntax.")

        # Displays all the data items fom the Mess.
        elif cmd[0] == "getmess":
            for index in range(0, len(mess)):
                print(str(index + 1) + ". " + str(mess[index]))

        # Sorts the data items of the mess in ascending or descending order using sort_mess() from ib.py.
        # It will raise a handled error if the Mess has numeric as well as alphabetic data items.
        elif cmd[0] == "sortmess":
            try:
                if len(cmd) == 2:
                    # Sorts in ascending order.
                    if cmd[1] == "a" or cmd[1] == "A":
                        lib.sort_mess(mess)
                    # Sorts in descending order.
                    elif cmd[1] == "d" or cmd[1] == "D":
                        lib.sort_mess(mess)
                        mess.reverse()
                    else:
                        print("Invalid Argument Passed.")
                else:
                    print("Invalid Syntax.")
            except TypeError:
                print("Can't Sort num And alpha.")

        # Displays the result of the supplied mathematical expression.
        elif cmd[0] == "calc":
            try:
                equation = ""
                for check in range(1, len(cmd)):
                    # If the expression does not contain any reference from the Mess or the Cluster.
                    if not(lib.starts_with(cmd[check], "x_") or (lib.starts_with(cmd[check], "y_"))):
                        equation = equation + cmd[check]
                    else:
                        # If the expression contains one or multiple references from the Mess.
                        if lib.starts_with(cmd[check], "x_"):
                            # Getting the data item from the mess from the index supplied
                            # after "x_" and concatenating it with the variable "equation".
                            equation = equation + str((
                                mess[(int(
                                    cmd[check][2:]
                                ) - 1)
                                ]
                            ))
                        # If the expression contains one or multiple references from the Cluster.
                        elif lib.starts_with(cmd[check], "y_"):
                            # Getting the data item from the cluster from the key supplied
                            # after "y_" and concatenating it with the variable "equation".
                            equation = equation + str(cluster[cmd[check][2:]])
                print(eval(equation))
            except KeyError:
                print("Cluster Item Not Found.")
            except NameError:
                print("Invalid Datatypes.")
            except ValueError:
                print("Invalid Datatypes.")
            except IndexError:
                print("Mess Item Not Found.")
            except ZeroDivisionError:
                print("Cannot Divide By Zero.")
            except EOFError:
                print("Invalid Expression.")

        #### Commands for changing expression for the prompt  ####

        elif cmd[0] == "exp":
            if len(cmd) == 1:
                list_expressions = "1. :)\n2. ;)\n3. :|\n4. :("
                print(list_expressions)
            elif cmd[1] == "1":
                expression = ":) > "
            elif cmd[1] == "2":
                expression = ";) > "
            elif cmd[1] == "3":
                expression = ":| > "
            elif cmd[1] == "4":
                expression = ":( > "
            else:
                continue

        ####                                                  ####

        # Reads the log.txt file which contains the history of all previously entered commands.
        elif cmd[0] == "getlog" and len(cmd) == 1:
            lib.read_log()

        # Reads a text-containing file using read_file from lib.py.
        elif cmd[0] == "read":
            try:
                # If the address of the file does not contain spaces.
                file_address = ""
                if len(cmd) == 2:
                    # Raises a handled error if the user tries to read the system files.
                    if cmd[1] == ".cipher" or cmd[1] == ".val":
                        print("Cannot Read System File.")
                        continue
                    if ((cmd[len(cmd) - 1][-7:-1] + "r") == ".cipher") or (cmd[len(cmd) - 1][-4:-1] + "l" == ".val"):
                        print("Cannot Read System File.")
                        continue
                    # If not a system file, sets the variable "file_address" to the supplied address.
                    else:
                        file_address = cmd[1]

                # If the address of the file contains spaces.
                elif len(cmd) > 2:
                    # Raises a handled error if the user tries to read the system files.
                    if ((cmd[len(cmd) - 1][-6:-1] + "r") == "cipher") or (cmd[len(cmd) - 1][-3:-1] + "l" == "val"):
                        print("Cannot Read System File.")
                        continue
                    # If not a system file, sets the variable "file_address" to the supplied address
                    # after concatenation.
                    else:
                        for file_address_concat in range(1, len(cmd)):
                            file_address = file_address + cmd[file_address_concat] + " "
                print()
                lib.read_file(file_address)
                print()
            except (FileNotFoundError, IsADirectoryError):
                print("Invalid File/Directory.")

        # Reads a .csv file using csv() from lib.py
        elif cmd[0] == "csv" and len(cmd) >= 2:
            try:
                # Sets the default spacing for CVS Reader to 4 spacings.
                csv_spacing = 4
                path = ""
                # If custom spacing is not supplied and the file address does not contain spaces.
                if len(cmd) == 2:
                    path = cmd[1]
                # If custom spacing is supplied and the file address contains spaces.
                elif len(cmd) > 2:
                    # Concatenates the path which contains spaces.
                    for path_concat in range(2, len(cmd)):
                        path = path + cmd[path_concat] + " "
                    path = path[:-1]
                    # Sets the custom spacing.
                    csv_spacing = int(cmd[1])
                print()
                lib.csv(path, csv_spacing)
                print()
            except (FileNotFoundError, IsADirectoryError):
                print("Invalid File/Directory")

        # Exports the Mess to a text file.
        elif cmd[0] == "export" and cmd[1] == "mess" and len(cmd) >= 3:
            try:
                export_address = ""
                # If the address does not contain spaces.
                if len(cmd) == 3:
                    export_address = cmd[2]
                # If the address contains spaces.
                else:
                    for itr0 in range(2, len(cmd)):
                        export_address = export_address + cmd[itr0] + " "
                    export_address = export_address[:-1]
                # Opens the export file (Creates one if it does not exist).
                gen_file = open(export_address, "w+", encoding = "utf-8")
                for add_log in range(0, len(mess)):
                    # Specifies the type of data item in the export file.
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
                # If the address does not contain spaces.
                if len(cmd) == 3:
                    cluster_export_address = cmd[2]
                # If the address contains spaces.
                else:
                    for cluster_itr in range(2, len(cmd)):
                        cluster_export_address = cluster_export_address + cmd[cluster_itr] + " "
                # Opens the export file (Creates one if it does not exist).
                cluster_gen_file = open(cluster_export_address, "w+", encoding = "utf-8")
                # Generate lists containing Keys and Values from the cluster.
                cluster_keys = list(cluster.keys())
                cluster_values = list(cluster.values())
                for add_cluster in range(0, len(cluster)):
                    # Writes the data to the export file as float if the data type for the
                    # data item is "num". Also writes the data type next to it (num).
                    if type(cluster_values[add_cluster]) == type(1.1):
                        cluster_gen_file.write(str(cluster_keys[add_cluster]) + " " + str(cluster_values[add_cluster]) + " num" + "\n")
                    # Writes the data to the export file as string if the data type for the
                    # data item is "alpha". Also writes the data type next to it (alpha).
                    elif type(cluster_values[add_cluster]) == type("1.1"):
                        cluster_gen_file.write(str(cluster_keys[add_cluster]) + " " + str(cluster_values[add_cluster]) + " alpha" + "\n")
                cluster_gen_file.close()
            except (FileNotFoundError, IsADirectoryError):
                print("Invalid File/Directory.")

        # Imports the data items into the Mess from a text file.
        elif cmd[0] == "import" and cmd[1] == "mess" and len(cmd) >= 4:
            try:
                import_file_src = ""
                # If the address for import file contains spaces.
                if len(cmd) > 4:
                    for itr in range(3, len(cmd)):
                        import_file_src = import_file_src + cmd[itr] + " "
                # If the address for the import file does not contain spaces.
                else:
                    import_file_src = cmd[3]
                # Opens the import file in read mode.
                import_file = open(import_file_src, "r", encoding = "utf-8")
                contents = import_file.readlines()
                # Clears the Mess if the user wishes to re-write the Mess
                # with the data items from the import file.
                if cmd[2] == "rw":
                    mess.clear()
                # Shows a message if the import mode is not specified.
                if cmd[2] != "rw" and cmd[2] != "w":
                    print("Invalid Import Mode.")
                    continue
                # Removes the "\n" character from the end of every line.
                for lines in range(0, len(contents)):
                    contents[lines] = contents[lines][:-1]
                # Pushes the data items in the Mess with their respective data types
                # specified in the import file.
                for split_lines in range(0, len(contents)):
                    types_array = contents[split_lines].split(" ")
                    if types_array[-1] == "num":
                        mess.append(float(types_array[0]))
                    elif types_array[-1] == "alpha":
                        data = ""
                        # If the alphabetic data item contains or do not contain spaces.
                        for data_concat in range(0, len(types_array) - 1):
                            data = data + types_array[data_concat] + " "
                        data = data[:-1]
                        mess.append(data)
                import_file.close()
            except ValueError:
                print("Import File Is Corrupted.")
            except (FileNotFoundError, IsADirectoryError):
                print("Invalid File/Directory.")

        # Imports the data items into the Cluster from a text file.
        elif cmd[0] == "import" and cmd[1] == "cluster" and len(cmd) >= 4:
            try:
                cluster_import_file = ""
                # If the address for import file does not contain spaces.
                if len(cmd) == 4:
                    cluster_import_file = cmd[3]
                # If the address for import file does contains spaces.
                else:
                    for itr1 in range(3, len(cmd)):
                        cluster_import_file = cluster_import_file + cmd[itr1] + " "
                # Opens the import file in read mode.
                c_import_file = open(cluster_import_file, "r", encoding = "utf-8")
                cluster_contents = c_import_file.readlines()
                # Clears the cluster if the user wishes to re-write the cluster
                # with the data items from the import file.
                if cmd[2] == "rw":
                    cluster.clear()
                # Shows message if the import mode is not specified.
                if cmd[2] != "rw" and cmd[2] != "w":
                    print("Invalid Import Mode.")
                    continue
                # Removes the "\n" character from the end of every line.
                for trim_char in range(0, len(cluster_contents)):
                    cluster_contents[trim_char] = cluster_contents[trim_char][:-1]
                for cluster_data in range(0, len(cluster_contents)):
                    # Sets the data items in the Cluster with their respective data types
                    # specified in the import file.
                    cluster_lines = cluster_contents[cluster_data].split(" ")
                    # For the data items with spaces.
                    if len(cluster_lines) > 3:
                        join_data = ""
                        for join_data_concat in range(1, len(cluster_lines) - 1):
                            join_data = join_data + cluster_lines[join_data_concat] + " " 
                        join_data = join_data[:-1]
                        # Removes all the elements except for the first one and the last one.
                        del cluster_lines[1: -1]
                        # Inserts the concatenated data at index 1.
                        cluster_lines.insert(1, join_data)                    
                    if cluster_lines[-1] == "num":
                        cluster[cluster_lines[0]] = float(cluster_lines[1])
                    elif cluster_lines[-1] == "alpha":
                        cluster[cluster_lines[0]] = str(cluster_lines[1])
                c_import_file.close()
            except ValueError:
                print("Import File Is Corrupted.")
            except (FileNotFoundError, IsADirectoryError):
                print("Invalid File/Directory.")

        # Sets a data item as a value to a key in the cluster
        elif cmd[0] == "set" and len(cmd) >= 4:
            # Gets the list of all the existing keys in the cluster.
            cluster_existing_keys = list(cluster.keys())
            # Does not allow the user to set a value to key which already has a value.
            if cmd[1] in cluster_existing_keys:
                print("Key Already Exists.")
                continue
            else:
                # Sets the variable for the data to be set to None
                data_set = None
                try:
                    # Checks if the value passed is a reference to a data item in the Mess.
                    if lib.starts_with(cmd[3], "x_"):
                        # Sets the data_set variable to the reference to the data item in the Mess.
                        data_set = mess[int(cmd[3][2:]) - 1]
                    else:
                        # Sets the passed value.
                        data_set = cmd[3]
                except IndexError:
                    print("Item Not Found.")
                    continue
                # Sets a numeric value to a key.
                if cmd[2] == "num":
                    if len(cmd) == 4:
                        # Gets the referred data items from the Mess and the Cluster.
                        if lib.starts_with(cmd[3], "x_"):
                            cluster[cmd[1]] = mess[int(cmd[3][2:]) - 1]
                        elif lib.starts_with(cmd[3], "y_"):
                            cluster[cmd[1]] = cluster[cmd[3][2:]]
                        else:
                            cluster[cmd[1]] = eval(data_set)
                    elif len(cmd) > 4:
                        # Forms and evaluates an mathematical expression from numeric and referred values
                        data_set = ""
                        for set_num_data in range(3, len(cmd)):
                            if lib.starts_with(cmd[set_num_data], "x_"):
                                data_set = data_set + str(mess[int(cmd[set_num_data][2:]) - 1])
                            elif lib.starts_with(cmd[set_num_data], "y_"):
                                data_set = data_set + str(cluster[cmd[set_num_data][2:]])
                            else:
                                data_set = data_set + cmd[set_num_data] + " "
                        cluster[cmd[1]] = eval(data_set)
                # Sets a alphabetic value to a key.
                elif cmd[2] == "alpha":
                    if len(cmd) == 4:
                        # Gets the referred data items from the Mess and the Cluster.
                        if lib.starts_with(cmd[3], "x_"):
                            cluster[cmd[1]] = mess[int(cmd[3][2:]) - 1]
                        elif lib.starts_with(cmd[3], "y_"):
                            cluster[cmd[1]] = cluster[cmd[3][2:]]
                        else:
                            cluster[cmd[1]] = str(data_set)
                    elif len(cmd) > 4:
                        set_data = ""
                        for set_data_concat in range(3, len(cmd)):
                            set_data = set_data + cmd[set_data_concat] + " "
                        set_data = set_data[:-1]
                        cluster[cmd[1]] = set_data
                else:
                    continue

        elif cmd[0] == "getcluster":
            if len(cluster) > 0:
                # Displays the entire cluster.
                if len(cmd) == 1:
                    # Generates a list of tuples containing keys and values.
                    cluster_items = list(cluster.items())
                    print("Key : Value\n")
                    for items in range(0, len(cluster)):
                        # Displays each key and value for the list "cluster_items"
                        # and is separated by " : ".
                        print(cluster_items[items][0], cluster_items[items][1], sep = " : ")

                # Displays only the keys from the cluster.
                elif len(cmd) == 2 and cmd[1] == "keys":
                    keys = list(cluster.keys())
                    print("Key :\n")
                    for list_keys in range(0, len(keys)):
                        print(str(keys[list_keys]) + " :")
                # Displays only the values from the cluster.
                elif len(cmd) == 2 and cmd[1] == "values":
                    values = list(cluster.values())
                    print(": Value\n")
                    for list_values in range(0, len(values)):
                        print(": " + str(values[list_values]))
                else:
                    print("Invalid Syntax.")
            else:
                continue

        # Changes the value of the supplied key.
        elif cmd[0] == "change" and len(cmd) >= 4:
            cluster_keys = list(cluster.keys())
            # Checks if the supplied key exists or not.
            if cmd[1] in cluster_keys:
                try:
                    # Sets the variable for the value to be changed to None.
                    change_value = None
                    # Checks if the value is a reference to a data item from the Mess.
                    if lib.starts_with(cmd[3], "x_"):
                        # Sets the value to the referred data item from the Mess.
                        change_value = mess[int(cmd[3][2:]) - 1]
                    elif lib.starts_with(cmd[3], "y_"):
                        # Sets the value to the referred data item in the Cluster.
                        change_value = cluster[cmd[3][2:]]
                    else:
                        # Sets the passed in value.
                        change_value = cmd[3]
                    # Changes the value of the supplied key to alphabetic or numeric value.
                except IndexError:
                    print("Item Not Found.")
                    continue
                except KeyError:
                    print("Invalid Key.")
                # For the values which are not referred from the Mess or the Cluster.
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

        # Gets the value of the key passed from the cluster.
        elif cmd[0] == "get":
            if cmd[1] == "cluster":
                try:
                    print(cluster[cmd[2]])
                except KeyError:
                    print("Invalid Key.")
                except IndexError:
                    print("Invalid Command.")
            elif cmd[1] == "mess":
                try:
                    print(mess[int(cmd[2]) - 1])
                except IndexError:
                    print("Item Not Found.")
                except KeyError:
                    print("Invalid Command.")

        # Removes a data item from the cluster.
        elif cmd[0] == "rem" and len(cmd) >= 1:
            # Removes the last data item from the cluster if the key is not supplied.
            if len(cmd) == 1:
                try:
                    cluster_keys1 = list(cluster.keys())
                    del cluster[cluster_keys1[-1]]
                except IndexError:
                    continue
            # Removes the specific data item from the cluster when the key is supplied.
            else:
                try:
                    del cluster[cmd[1]]
                except KeyError:
                    print("Invalid Key.")

        elif cmd[0] == "find" and len(cmd) >= 3:
            # Sets the variable for the item to be found to None.
            search = None
            try:
                # Sets a numeric value to be searched.
                if cmd[1] == "num":
                    search = float(cmd[2])
                else:
                    # Sets an alphabetic value to be searched.
                    if len(cmd) == 3 and cmd[1] == "alpha":
                        search = str(cmd[2])
                    # Sets an alphabetic value containing spaces to be searched.
                    elif len(cmd) > 3 and cmd[1] == "alpha":
                        search_data = ""
                        for search_concat in range(2, len(cmd)):
                            search_data = search_data + cmd[search_concat] + " "
                        # Removes the extra space (" ") at the end.
                        search = search_data[:-1]
            except (ValueError, TypeError):
                print("Invalid Datatype.")
                continue
            # Generates separate lists for Cluster keys and values.
            c_keys = list(cluster.keys())
            c_values = list(cluster.values())
            # Shows a "Not Found." message if the item is found nowhere.
            if not(search in c_keys) and not(search in c_values) and not(search in mess):
                print("Not Found.")
            else:
                data_type = None
                # Searches the item in the Mess.
                for search_mess in range(0, len(mess)):
                    if search == mess[search_mess]:
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

        # Return back to the prompt if no command is entered.
        elif len(command) == 0:
            continue

        # Show a "Invalid Command" message if wrong command is entered.
        else:
            print("Invalid Command: " + str(command))
            continue

    except EOFError:
        print("Invalid Syntax.")
        continue

    except ValueError:
        print("Invalid Datatypes.")
        continue

    except KeyboardInterrupt:
        print("\n\nBye.")
        break
    except:
        print("Oops! Something Went Wrong.")
log.close()