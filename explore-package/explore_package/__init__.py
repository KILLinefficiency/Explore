VERSION = 2.0
CODENAME = "Terrific"
LICENSE = "GNU General Public License v3.0"
AUTHOR = "Shreyas Sable"
REPOSITORY = "https://www.github.com/KILLinefficiency/Explore"

mess = []
cluster = {}
book = {}

def enc(text, key):
    enc_text = ""
    for itr in range(0, len(text)):
        enc_text = enc_text + chr(ord(text[itr]) + key)
    return enc_text

def dec(text, key):
    dec_text = ""
    for itr in range(0, len(text)):
        dec_text = dec_text + chr(ord(text[itr]) - key)
    return dec_text

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

def parse_csv(location):
    parsed_list = []
    csv_parse_file = open(location, "r", encoding = "utf-8")
    parse_contents = csv_parse_file.readlines()
    for trim_n in range(0, len(parse_contents)):
        if parse_contents[trim_n][-1] == "\n":
            parse_contents[trim_n] = parse_contents[trim_n][:-1]
    for add_cell in range(0, len(parse_contents)):
        info_cells = parse_contents[add_cell].split(",")
        parsed_list.append(info_cells)
    return parsed_list

def starts_with(string, trimmed_string):
    if trimmed_string == string[0:len(trimmed_string)]:
        return True
    else:
        return False

def read_file(location):
    rfile = open(location, "r", encoding = "utf-8")
    contents = rfile.read()
    rfile.close()
    return contents

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

def clear_screen():
    if platform() == "Linux" or platform() == "Darwin":
        system("clear")
    elif platform() == "Windows":
        system("cls")
    else:
        print("Unable to clear screen.")

def disp_list(arr):
    for itr_item in range(0, len(arr)):
        for itr_content in range(0, len(arr[itr_item])):
            print("", end = "    ")
            print(arr[itr_item][itr_content], end = "    ")
        print()

def del_left_zeros(text):
    zero_counter = 0
    while text[zero_counter] == "0":
        zero_counter = zero_counter + 1
    return text[zero_counter:]

def reverse_list(arr):
    rev_arr = []
    for rev_list_count in range(len(arr) - 1, -1, -1):
        rev_arr.append(arr[rev_list_count])
    return rev_arr

"""
Comments will also be present on the same line as that of
the Explore command statement. The following function
detects and deletes these comments. The detection is done
by checking if a individual word is or starts with "...".
If yes, then the function deletes the word and all the words
onwards to than word.
"""
def del_line_comm(commands):
    try:
        for del_comm in range(0, len(commands)):
            if commands[del_comm] == "..." or starts_with(commands[del_comm], "..."):
                del commands[commands.index(commands[del_comm]):]
    except IndexError:
        del_line_comm(commands)

def invoke(command):
    try:
        command = command.replace("\t", " ")
        cmd = command.split(" ")
        del_spaces(cmd)
        # Deletes all the comments present with the Explore command.
        del_line_comm(cmd)

        for add_spaces in range(0, len(cmd)):
            for put_spaces in range(0, len(cmd[add_spaces])):
                if "|" in cmd[add_spaces]:
                    cmd[add_spaces] = cmd[add_spaces].replace("|", " ")
        
        try:
            for replace_ref in range(0, len(cmd)):
                if starts_with(cmd[replace_ref], "x_"):
                    cmd[replace_ref] = str(mess[(int(cmd[replace_ref][2:]) - 1)])
                elif starts_with(cmd[replace_ref], "y_"):
                    cmd[replace_ref] = str(cluster[cmd[replace_ref][2:]])
                elif starts_with(cmd[replace_ref], "b_"):
                    info_address = cmd[replace_ref][2:].split("->")
                    cmd[replace_ref] = str(book[info_address[0]][int(info_address[1]) - 1][int(info_address[2]) - 1])
        except (NameError, KeyError, ValueError, IndexError):
            print("Referenced Data Item(s) not found.")
            pass

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
                    disp_data = disp_data + str(cmd[check]) + " "
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
                num_data = cmd[2]
                if len(cmd) == 3:
                    mess.append(float(num_data))
                if len(cmd) == 4:
                    mess.insert(int(cmd[-1]) - 1, float(eval(num_data)))
            except ValueError:
                print("Invalid Datatypes.")
            except KeyError:
                print("Invalid Key.")

        elif cmd[0] == "push" and cmd[1] == "alpha" and len(cmd) >= 3:
            try:
                try:
                    data_push = cmd[2]
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
            except ValueError:
                print("Invalid Datatypes.")

        elif cmd[0] == "pop":
            try:
                if len(cmd) == 1:
                    delete_item(mess, len(mess))
                elif len(cmd) == 2:
                    delete_item(mess, int(cmd[1]))
                else:
                    for pop_several in range(1, len(mess)):
                        try:
                            delete_item(mess, int(cmd[pop_several]))
                        except IndexError:
                            continue
            except IndexError:
                pass

        elif cmd[0] == "mov":
            if cmd[1] == "num":
                mov_data = ""
                for join_mov_data in range(2, len(cmd) - 1):
                    mov_data = mov_data + lib.del_left_zeros(cmd[join_mov_data]) + " "
                mov_data = mov_data[:-1]
                mess[int(cmd[-1]) - 1] = eval(mov_data)
            elif cmd[1] == "alpha":
                try:
                    mov_data = ""
                    if len(cmd) == 4:
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
            elif cmd[1] == "book":
                return len(book)
            else:
                return None

        elif cmd[0] == "clean":
            clean_list = cmd[1:]
            if "mess" in clean_list:
                mess.clear()
            if "cluster" in clean_list:
                cluster.clear()
            if "book" in clean_list:
                book.clear()

        elif cmd[0] == "getmess":
            return mess

        elif cmd[0] == "sortmess":
            try:
                if len(cmd) == 2:
                    if cmd[1] == "a" or cmd[1] == "A":
                        sort_mess(mess)
                    elif cmd[1] == "d" or cmd[1] == "D":
                        sort_mess(mess)
                        mess = reverse_list(mess)
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
                    equation = equation + del_left_zeros(cmd[check])
                maths_answer = eval(equation)
                if maths_answer == True:
                    return True
                elif maths_answer == False:
                    return False
                else:
                    return maths_answer
            except (ValueError, IndexError, ZeroDivisionError, EOFError):
                return None

        elif cmd[0] == "getbook" and len(cmd) == 1:
            book_keys = list(book.keys())
            if len(book_keys) == 0:
                pass
            else:
                for itr_book in range(0, len(book_keys)):
                    print()
                    print(str(book_keys[itr_book]) + ": ")
                    disp_list(book[book_keys[itr_book]])
                print()

        elif cmd[0] == "read":
            try:
                file_address = ""
                if len(cmd) == 2:
                    if cmd[1] == ".cipher" or cmd[1] == ".val":
                        print("Cannot Read System File.")
                        pass
                    if ((cmd[len(cmd) - 1][-7:-1] + "r") == ".cipher") or (cmd[len(cmd) - 1][-4:-1] + "l" == ".val"):
                        print("Cannot Read System File.")
                        pass
                    else:
                        file_address = cmd[1]

                elif len(cmd) > 2:
                    if ((cmd[len(cmd) - 1][-6:-1] + "r") == "cipher") or (cmd[len(cmd) - 1][-3:-1] + "l" == "val"):
                        print("Cannot Read System File.")
                        pass
                    else:
                        for file_address_concat in range(1, len(cmd)):
                            file_address = file_address + cmd[file_address_concat] + " "
                        file_address = file_address[:-1]
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
                    path = path[:-1]
                    csv_spacing = int(cmd[1])
                print()
                csv(path, csv_spacing)
                print()
            except (FileNotFoundError, IsADirectoryError):
                print("Invalid File/Directory.")

        elif cmd[0] == "book" and len(cmd) >= 4:
            try:
                path = ""
                book_keys = list(book.keys())
                if cmd[1] == "csv":
                    if len(cmd) == 4:
                        path = cmd[3]
                    elif len(cmd) > 4:
                        for join_path in range(3, len(cmd)):
                            path = path + cmd[join_path] + " "
                        path = path[:-1]

                    if not(cmd[2] in book_keys):
                        book[cmd[2]] = parse_csv(path)
                    else:
                        print("Data Item already exists.")
            except (FileNotFoundError, IsADirectoryError):
                print("Invalid File/Directory.")

        elif cmd[0] == "export" and cmd[1] == "mess" and len(cmd) >= 3:
            try:
                export_address = ""
                if len(cmd) >= 3:
                    export_address = cmd[2]
                else:
                    for itr0 in range(2, len(cmd)):
                        export_address = export_address + cmd[itr0] + " "
                    export_address = export_address[:-1]
                gen_file = open(export_address, "w+", encoding = "utf-8")
                if starts_with(cmd[-1], "e_"):
                    try:
                        m_e_key = int(cmd[-1][2:])
                        if m_e_key < 0:
                            print("The Encryption Key cannot be a negative value.")
                            pass
                        for add_log in range(0, len(mess)):
                            if type(mess[add_log]) == type(1.1):
                                gen_file.write(enc(str(mess[add_log]) + " num" + "\n", m_e_key))
                            elif type(mess[add_log]) == type("1.1"):
                                gen_file.write(enc(str(mess[add_log]) + " alpha" + "\n", m_e_key))
                        gen_file.close()
                    except ValueError:
                        print("The Encryption Key must be in range of 0 to 999999.")
                else:
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
                if len(cmd) >= 3:
                    cluster_export_address = cmd[2]
                else:
                    for cluster_itr in range(2, len(cmd)):
                        cluster_export_address = cluster_export_address + cmd[cluster_itr] + " "
                cluster_gen_file = open(cluster_export_address, "w+", encoding = "utf-8")
                cluster_keys = list(cluster.keys())
                cluster_values = list(cluster.values())
                if starts_with(cmd[-1], "e_"):
                    try:
                        c_e_key = int(cmd[-1][2:])
                        if c_e_key < 0:
                            print("The Encryption Key cannot be a negative value.")
                            pass
                        for add_cluster in range(0, len(cluster)):
                            if type(cluster_values[add_cluster]) == type(1.1):
                                cluster_gen_file.write(enc(str(cluster_keys[add_cluster]) + " " + str(cluster_values[add_cluster]) + " num" + "\n", c_e_key))
                            elif type(cluster_values[add_cluster]) == type("1.1"):
                                cluster_gen_file.write(enc(str(cluster_keys[add_cluster]) + " " + str(cluster_values[add_cluster]) + " alpha" + "\n", c_e_key))
                        cluster_gen_file.close()
                    except ValueError:
                        print("The Encryption Key must be in range of 0 to 999999.")
                else:
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
                if len(cmd) >= 5:
                    for itr in range(3, len(cmd) - 1):
                        import_file_src = import_file_src + cmd[itr] + " "
                        import_file_src = import_file_src[:-1]
                else:
                    import_file_src = cmd[3]
                import_file = open(import_file_src, "r", encoding = "utf-8")
                contents = import_file.readlines()
                if cmd[2] == "rw":
                    mess.clear()
                if cmd[2] != "rw" and cmd[2] != "w":
                    print("Invalid Import Mode.")
                    pass
                if starts_with(cmd[-1], "d_"):
                    try:
                        m_d_key = int(cmd[-1][2:])
                        if m_d_key < 0:
                            print("The Decryption Key cannot be a negative value.")
                            pass
                        for decrypt_text in range(0, len(contents)):
                            contents[decrypt_text] = dec(contents[decrypt_text], m_d_key)
                        for lines in range(0, len(contents)):
                            if contents[lines][-1] == "\n":
                                contents[lines] = contents[lines][:-1]
                        new_contents = contents.copy()[0]
                        contents = new_contents.split("\n")
                    except ValueError:
                        print("The Decryption Key must be in range of 0 to 999999.")
                else:
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
                        data = data[:-1]
                        mess.append(data)
                import_file.close()
            except ValueError:
                print("Import File Is Corrupted Or Invalid Key Passed.")
            except (FileNotFoundError, IsADirectoryError):
                print("Invalid File/Directory.")

        elif cmd[0] == "import" and cmd[1] == "cluster" and len(cmd) >= 4:
            try:
                cluster_import_file = ""
                if len(cmd) >= 4:
                    cluster_import_file = cmd[3]
                else:
                    for itr1 in range(3, len(cmd) - 1):
                        cluster_import_file = cluster_import_file + cmd[itr1] + " "
                c_import_file = open(cluster_import_file, "r", encoding = "utf-8")
                cluster_contents = c_import_file.readlines()
                if cmd[2] == "rw":
                    cluster.clear()
                if cmd[2] != "rw" and cmd[2] != "w":
                    print("Invalid Import Mode.")
                    pass
                if starts_with(cmd[-1], "d_"):
                    try:
                        c_d_key = int(cmd[-1][2:])
                        if c_d_key < 0:
                            print("The Decryption Key cannot be a negative value.")
                            pass
                        for decrypt_text in range(0, len(cluster_contents)):
                            cluster_contents[decrypt_text] = dec(cluster_contents[decrypt_text], c_d_key)
                        for lines in range(0, len(cluster_contents)):
                            if cluster_contents[lines][-1] == "\n":
                                cluster_contents[lines] = cluster_contents[lines][:-1]
                        new_cluster_contents = cluster_contents.copy()[0]
                        cluster_contents = new_cluster_contents.split("\n")
                    except ValueError:
                        print("The Decryption Key must be in range of 0 to 999999.")
                else:
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
                c_import_file.close()
            except ValueError:
                print("Import File Is Corrupted Or Invalid Key Passed.")
            except (FileNotFoundError, IsADirectoryError):
                print("Invalid File/Directory.")
            except KeyboardInterrupt:
                pass

        elif cmd[0] == "set" and len(cmd) >= 4:
            try:
                cluster_existing_keys = list(cluster.keys())
                if cmd[1] in cluster_existing_keys:
                    print("Key Already Exists.")
                    pass
                else:
                    data_set = cmd[3]
                    if cmd[2] == "num":
                        if len(cmd) == 4:
                            cluster[cmd[1]] = float(eval(data_set))
                        elif len(cmd) > 4:
                            data_set = ""
                            for set_num_data in range(3, len(cmd)):
                                data_set = data_set + del_left_zeros(cmd[set_num_data]) + " "
                            cluster[cmd[1]] = eval(data_set)
                    elif cmd[2] == "alpha":
                        if len(cmd) == 4:
                            cluster[cmd[1]] = str(data_set)
                        elif len(cmd) > 4:
                            set_data = ""
                            for set_data_concat in range(3, len(cmd)):
                                set_data = set_data + cmd[set_data_concat] + " "
                            set_data = set_data[:-1]
                            cluster[cmd[1]] = set_data
                    else:
                        pass
            except(NameError, ValueError):
                print("Invalid Datatypes.")

        elif cmd[0] == "getcluster":
            if len(cluster) > 0:
                if len(cmd) == 1:
                    return cluster
                elif len(cmd) == 2 and cmd[1] == "keys":
                    keys = list(cluster.keys())
                    return keys
                elif len(cmd) == 2 and cmd[1] == "values":
                    values = list(cluster.values())
                    return values
                else:
                    return None

        elif cmd[0] == "change" and len(cmd) >= 4:
            cluster_keys = list(cluster.keys())
            if cmd[1] in cluster_keys:
                change_value = cmd[3]
                try:
                    if cmd[2] == "num":
                        change_value = ""
                        for join_change_value in range(3, len(cmd)):
                            change_value = change_value + del_left_zeros(cmd[join_change_value]) + " "
                        change_value = change_value[:-1]
                        cluster[cmd[1]] = eval(change_value)
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
                elif cmd[1] == "book":
                    return str(book[cmd[2]][int(cmd[3]) - 1][int(cmd[4]) - 1])
            except (IndexError, KeyError):
                return None

        elif cmd[0] == "rem" and len(cmd) >= 1:
            try:
                cluster_keys1 = list(cluster.keys())
                if len(cmd) == 1:
                    del cluster[cluster_keys1[-1]]
                else:
                    for rem_several in range(1, len(cmd)):
                        try:
                            del cluster[cmd[rem_several]]
                        except (KeyError, IndexError):
                            continue
            except KeyError:
                pass

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
                pass
            c_keys = list(cluster.keys())
            c_values = list(cluster.values())
            b_data_space = list(book.keys())
            b_data_space_contents = list(book.values())
            book_all_values = []
            for all_values in range(0, len(b_data_space_contents)):
                for add_values in range(0, len(b_data_space_contents[all_values])):
                    for add_more_values in range(0, len(b_data_space_contents[all_values][add_values])):
                        book_all_values.append(b_data_space_contents[all_values][add_values][add_more_values])
            if not((search in c_keys) or (search in c_values) or (search in mess) or (search in b_data_space) or(search in book_all_values)):
                print("Not Found.")
            else:
                data_type = None
                for search_mess in range(0, len(mess)):
                    if search == mess[search_mess]:
                        if type(search) == type(1.1):
                            data_type = "num"
                        elif type(search) == type("1.1"):
                            data_type = "alpha"
                        results.append(
                            {
                                "Location": "Mess",
                                "Datatype": data_type,
                                "Position": search_mess + 1
                            }
                        )
                for search_keys in range(0, len(c_keys)):
                    if search == c_keys[search_keys]:
                        results.append(
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
                        results.append(
                            {
                                "Location": "Cluster",
                                "Itemtype": "Value",
                                "Datatype": data_type1,
                                "Key": c_keys[search_values]
                            }
                        )
                for search_data_space in range(0, len(b_data_space)):
                    if search == b_data_space[search_data_space]:
                        results.append(
                            {
                                "Location": "Book",
                                "Itemtype": "Dataspace",
                                "Position": search_data_space + 1
                            }
                        )
                for search_parsed_values in range(0, len(b_data_space_contents)):
                    for search_each_dataspace in range(0, len(b_data_space_contents[search_parsed_values])):
                        for search_each_value in range(0, len(b_data_space_contents[search_parsed_values][search_each_dataspace])):
                            if search == b_data_space_contents[search_parsed_values][search_each_dataspace][search_each_value]:
                                results.append(
                                    {
                                        "Location": "Book",
                                        "Itemtype": "Parsed Value",
                                        "Row": b_data_space_contents[search_parsed_values].index(b_data_space_contents[search_parsed_values][search_each_dataspace]) + 1,
                                        "Column": b_data_space_contents[search_parsed_values][search_each_dataspace].index(b_data_space_contents[search_parsed_values][search_each_dataspace][search_each_value]) + 1
                                    }
                                )
            return results
        
        elif cmd[0] == "dump":
            dump_file = open(cmd[-1], "a+")
            dump_file_text = ""
            for dump_file_loop in range(1, len(cmd) - 1):
                dump_file_text = dump_file_text + cmd[dump_file_loop] + " "
            dump_file_text = dump_file_text[:-1]
            dump_file.write(dump_file_text + "\n")
            dump_file.close()
        
        elif cmd[0] == "":
            pass

        else:
            print("Invalid Command: " + str(command))

    except NameError:
        pass
    except SyntaxError:
        print("Invalid Syntax.")
    except ValueError:
        print("Invalid Datatypes.")
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
