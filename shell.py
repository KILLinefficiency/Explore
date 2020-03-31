import cipher
import lib
from pathlib import Path
from random import randint

# Opens files .cipher and .val.
# .cipher and .val are the hidden system files.
login_file = Path(".cipher")
key_file = Path(".val")
log_file = Path("log.txt")

try:
    if not (login_file.is_file() or key_file.is_file() or log_file.is_file()):
        password = open(".cipher", "w+", encoding = "utf=8")
        key = open(".val", "w+", encoding = "utf-8")
        log = open("log.txt", "w+", encoding = "utf-8")
        # Closes the log.txt file I/O instance because it is not required in this file.
        # log.txt is used again.
        log.close()
        while True:
            try:
                # Asks the user to set up a new password.
                new_password = input("\nSet new Login Password: ")
                break
            except KeyboardInterrupt:
                print()
        while True:
            try:
                # Asks the user to set up a new encryption key.
                cipher_key = int(input("\nSet new Encryption Key: "))
                # Sets a random encryption key between 1 and 128 if the user enters 0.
                if cipher_key == 0:
                    cipher_key = randint(1, 129)
                    key.write(str(cipher_key))
                    lib.explore_splash()
                # Sets the user-desired key if it is not 0. 
                else:
                    key.write(str(cipher_key))
                    lib.explore_splash()
                print()
                break
            except ValueError:
                print("\nInvalid Key Entered.")
                continue
            except KeyboardInterrupt:
                print()
        key.close()
        # Encrypts the new password with the key entered by the user.
        password.write(cipher.enc(new_password, cipher_key))
        password.close()
    # Asks user to log in with password if the files cipher and val exist.
    elif login_file.is_file() or key_file.is_file():
        password = open(".cipher", "r", encoding = "utf-8")
        login_password = password.read()
        key = open(".val", "r", encoding = "utf-8")
        cipher_key = int(key.read())
        while True:
            try:
                ask_password = input("\nLogin Password: ")
                # Checks if the entered password matches the correct decrypted password.
                if ask_password == cipher.dec(login_password, cipher_key):
                    lib.explore_splash()
                    break
                else:
                    print("\nAccess Denied.")
                    continue
            except KeyboardInterrupt:
                continue
        password.close()
        key.close()
except FileNotFoundError:
    print("\nSystem Error Encountered.\n\nNavigate to Explore's directory and run:\n\n\tmake reset\n\nAlternative: Get a fresh copy of Explore from https://www.github.com/KILLinefficiency/Explore\n")
    exit()

# The code for shell begins here.

flag = True
logging = True
log = open("log.txt", "a", encoding = "utf-8")
# Declares empty list and dictionaries for the Mess, the Cluster and the Book respectively.
mess = []
cluster = {}
book = {}
# Sets up the expression that appears on the prompt.
expression = ":) > "
expressions = [":) > ", ";) > ", ":| > ", ":( > ", ":D > ", ":P > ", ":O > "]

# Starts the infinite loop where the prompt appears again and again
# for interpreting commands
while flag:
    try:
        escape_log = False
        command = input(expression)
        command = command.replace("\t", " ")
        cmd = command.split(" ")

        # For replacing the referred values from the Mess, the Cluster and the Book.
        try:
            for replace_ref in range(0, len(cmd)):
                # For referred values from the Mess.
                if lib.starts_with(cmd[replace_ref], "x_"):
                    cmd[replace_ref] = str(mess[(int(cmd[replace_ref][2:]) - 1)])
                # For referred values from the Cluster.
                elif lib.starts_with(cmd[replace_ref], "y_"):
                    cmd[replace_ref] = str(cluster[cmd[replace_ref][2:]])
                # For referred values from the Book.
                elif lib.starts_with(cmd[replace_ref], "b_"):
                    info_address = cmd[replace_ref][2:].split("->")
                    cmd[replace_ref] = str(book[info_address[0]][int(info_address[1]) - 1][int(info_address[2]) - 1])
        except (KeyError, ValueError, IndexError):
            print("Referenced Data Item(s) not found.")
            continue

        # Writes the entered command to log.txt file and does not if the command starts with a space character (" ").
        if cmd[0] == "":
            escape_log = True
        if not (len(command) == 0) and not (escape_log):
            log.write(command + "\n")

        # Removes the extra unwanted spaces from the command.
        lib.del_spaces(cmd)

        # Replaces the pipe character ("|") with space (" ").
        for add_spaces in range(0, len(cmd)):
            for put_spaces in range(0, len(cmd[add_spaces])):
                # Searches for pipe ("|").
                if "|" in cmd[add_spaces]:
                    # Replaces all the pipe characters ("|") with space characters (" ").
                    cmd[add_spaces] = cmd[add_spaces].replace("|", " ")

        # Return back to the prompt if no command is entered.
        if len(command) == 0:
            continue

        elif (cmd[0] == "exit" or cmd[0] == "bye" or cmd[0] == "exit." or cmd[0] == "bye.") and len(cmd) == 1:
            print("\nBye.\n")
            break

        elif (cmd[0] == "about" or cmd[0] == "info") and len(cmd) == 1:
            lib.explore_splash()
            print("\nExplore v2.0\nCodename: Terrific\nLicense: GNU General Public License v3.0\nAuthor: Shreyas Sable\nRepository: https://www.github.com/KILLinefficiency/Explore\n")

        elif cmd[0] == "clear" and len(cmd) == 1:
            lib.clear_screen()
        
        # Displays text and data.
        elif cmd[0] == "disp":
            try:
                disp_data = ""
                # Concatenates the data passed to "disp".
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

        # Pushes numeric data items into the mess.
        elif cmd[0] == "push" and cmd[1] == "num":
            try:
                # Pushes numeric data to the Mess.
                num_data = cmd[2]
                if len(cmd) == 3:
                    mess.append(float(num_data))
                # Pushes numeric data to the Mess at a particular position.
                if len(cmd) == 4:
                    mess.insert(int(cmd[-1]) - 1, eval(num_data))
            except ValueError:
                print("Invalid Datatypes.")
            except KeyError:
                print("Invalid Key.")

        # Pushes alphabetic data items into the mess.
        elif cmd[0] == "push" and cmd[1] == "alpha" and len(cmd) >= 3:
            try:
                try:
                    data_push = cmd[2]
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
            except ValueError:
                print("Invalid Datatypes.")
            except KeyError:
                print("Invalid Key.")

        # Deletes data items from the mess.
        elif cmd[0] == "pop":
            try:
                # Deletes the last data item of the mess using delete_item() from lib.py.
                if len(cmd) == 1:
                    lib.delete_item(mess, len(mess))
                # Deletes a particular data item of the given index using delete_item() from lib.py.
                elif len(cmd) == 2:
                    lib.delete_item(mess, int(cmd[1]))
                # Deletes multiple passed data items of the given index using delete_item() from lib.py.
                else:
                    for pop_several in range(1, len(mess)):
                        lib.delete_item(mess, int(cmd[pop_several]))
            except IndexError:
                continue

        # Replaces the current data item of the given index with the supplied numeric data item in the Mess.
        elif cmd[0] == "mov":
            if cmd[1] == "num":
                mov_data = ""
                for join_mov_data in range(2, len(cmd) - 1):
                    mov_data = mov_data + lib.del_left_zeros(cmd[join_mov_data]) + " "
                mov_data = mov_data[:-1]
                mess[int(cmd[-1]) - 1] = eval(mov_data)
            elif cmd[1] == "alpha":
                # Replaces the current data item of the given index with the supplied alphabetic data item.
                try:
                    mov_data = ""
                    # For data item with and without spaces.
                    if len(cmd) == 4:
                        mess[int(cmd[3]) - 1] = cmd[2]
                    if len(cmd) > 4:
                        # This loop will run only once if no spaces are present in the data item.
                        # And for multiple times if the data item contains spaces.
                        for mov_data_concat in range(2, len(cmd) - 1):
                            mov_data = mov_data + cmd[mov_data_concat] + " "
                        mov_data = mov_data[:-1]
                        mess[int(cmd[-1]) - 1] = mov_data
                except ValueError:
                    print("Invalid Datatypes.")
                except IndexError:
                    print("Item Not Found.")
                except KeyError:
                    print("Invalid Key.")
            else:
                print("Invalid Syntax.")

        # Displays the number of data items in the Mess, the Cluster and the Book.
        elif cmd[0] == "count" and len(cmd) == 2:
            if cmd[1] == "mess":
                print(len(mess))
            elif cmd[1] == "cluster":
                print(len(cluster))
            elif cmd[1] == "book":
                print(len(book))
            else:
                print("Invalid Syntax.")

        # Deletes all the data items of the Mess, the Cluster and the Book.
        elif cmd[0] == "clean":
            clean_list = cmd[1:]
            if "mess" in clean_list:
                mess.clear()
            if "cluster" in clean_list:
                cluster.clear()
            if "book" in clean_list:
                book.clear()

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
                        mess = lib.reverse_list(mess)
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
                print("Invalid Datatypes.")
            except IndexError:
                print("Mess Item Not Found.")
            except ZeroDivisionError:
                print("Cannot Divide By Zero.")
            except EOFError:
                print("Invalid Expression.")

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
                    print()
                    # Displays the label of the parsed data and the contents
                    # in an organized way.
                    print(str(book_keys[itr_book]) + ": ")
                    lib.disp_list(book[book_keys[itr_book]])
                print()
                
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
                        file_address = file_address[:-1]
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
                print("Invalid File/Directory.")
        
        # Writes the parsed data from a file to the Book.
        elif cmd[0] == "book" and len(cmd) >= 4:
            try:
                path = ""
                # Gets the data labels from the Book.
                book_keys = list(book.keys())
                # For parsing a CSV file.
                if cmd[1] == "csv":
                    # For address without spaces.
                    if len(cmd) == 4:
                        path = cmd[3]
                    # For address with spaces.
                    elif len(cmd) > 4:
                        for join_path in range(3, len(cmd)):
                            path = path + cmd[join_path] + " "
                        path = path[:-1]

                    # Writes the parsed data with the given key only if
                    # the provided data label does not already exist in
                    # the Book. 
                    if not(cmd[2] in book_keys):
                        print()
                        lib.csv(cmd[3], 1)
                        print()
                        book[cmd[2]] = lib.parse_csv(path)
                    else:
                        print("Data Item already exists.")
            except (FileNotFoundError, IsADirectoryError):
                print("Invalid File/Directory.")

        # Exports the Mess to a text file.
        elif cmd[0] == "export" and cmd[1] == "mess" and len(cmd) >= 3:
            try:
                export_address = ""
                # If the address does not contain spaces.
                if len(cmd) >= 3:
                    export_address = cmd[2]
                # If the address contains spaces.
                else:
                    for itr0 in range(2, len(cmd)):
                        export_address = export_address + cmd[itr0] + " "
                    export_address = export_address[:-1]
                # Opens the export file (Creates one if it does not exist).
                gen_file = open(export_address, "w+", encoding = "utf-8")
                if lib.starts_with(cmd[-1], "e_"):
                    try:
                        m_e_key = int(cmd[-1][2:])
                        if m_e_key < 0:
                            print("The Encryption Key cannot be a negative value.")
                            continue
                        for add_log in range(0, len(mess)):
                            # Specifies the type of data item in the export file.
                            # Encrypts the contents of the Mess with the provided encryption key.
                            if type(mess[add_log]) == type(1.1):
                                gen_file.write(cipher.enc(str(mess[add_log]) + " num" + "\n", m_e_key))
                            elif type(mess[add_log]) == type("1.1"):
                                gen_file.write(cipher.enc(str(mess[add_log]) + " alpha" + "\n", m_e_key))
                        gen_file.close()
                    except ValueError:
                        print("The Encryption Key must be in range of 0 to 999999.")
                else:
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
                if len(cmd) >= 3:
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
                if lib.starts_with(cmd[-1], "e_"):
                    try:
                        c_e_key = int(cmd[-1][2:])
                        if c_e_key < 0:
                            print("The Encryption Key cannot be a negative value.")
                            continue
                        for add_cluster in range(0, len(cluster)):
                            # Writes the data to the export file as float if the data type for the
                            # data item is "num". Also writes the data type next to it (num).
                            # Encrypts the contents of the Cluster with the prvided encryption key.
                            if type(cluster_values[add_cluster]) == type(1.1):
                                cluster_gen_file.write(cipher.enc(str(cluster_keys[add_cluster]) + " " + str(cluster_values[add_cluster]) + " num" + "\n", c_e_key))
                            # Writes the data to the export file as string if the data type for the
                            # data item is "alpha". Also writes the data type next to it (alpha).
                            elif type(cluster_values[add_cluster]) == type("1.1"):
                                cluster_gen_file.write(cipher.enc(str(cluster_keys[add_cluster]) + " " + str(cluster_values[add_cluster]) + " alpha" + "\n", c_e_key))
                        cluster_gen_file.close()
                    except ValueError:
                        print("The Encryption Key must be in range of 0 to 999999.")
                else:
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
                if len(cmd) >= 5:
                    for itr in range(3, len(cmd) - 1):
                        import_file_src = import_file_src + cmd[itr] + " "
                        import_file_src = import_file_src[:-1]
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
                # Decrypts the contents of the file to be imported with a decryption key.
                if lib.starts_with(cmd[-1], "d_"):
                    try:
                        # Gets the provided key.
                        m_d_key = int(cmd[-1][2:])
                        if m_d_key < 0:
                            print("The Decryption Key cannot be a negative value.")
                            continue
                        # Separates the data with the encrypted character of " ".
                        for decrypt_text in range(0, len(contents)):
                            contents[decrypt_text] = cipher.dec(contents[decrypt_text], m_d_key)
                        for lines in range(0, len(contents)):
                            if contents[lines][-1] == "\n":
                                contents[lines] = contents[lines][:-1]
                        new_contents = contents.copy()[0]
                        contents = new_contents.split("\n")
                    except ValueError:
                        print("The Decryption Key must be in range of 0 to 999999.")
                else:
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
                print("Import File Is Corrupted Or Invalid Key Passed.")
            except (FileNotFoundError, IsADirectoryError):
                print("Invalid File/Directory.")

        # Imports the data items into the Cluster from a text file.
        elif cmd[0] == "import" and cmd[1] == "cluster" and len(cmd) >= 4:
            try:
                cluster_import_file = ""
                # If the address for import file does not contain spaces.
                if len(cmd) >= 4:
                    cluster_import_file = cmd[3]
                # If the address for import file does contains spaces.
                else:
                    for itr1 in range(3, len(cmd) - 1):
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
                # Decrypts the contents of the file to be imported with a decryption key.
                if lib.starts_with(cmd[-1], "d_"):
                    try:
                        # Gets the provided key.
                        c_d_key = int(cmd[-1][2:])
                        if c_d_key < 0:
                            print("The Decryption Key cannot be a negative value.")
                            continue
                        # Separates the data with the encrypted character of " ".
                        for decrypt_text in range(0, len(cluster_contents)):
                            cluster_contents[decrypt_text] = cipher.dec(cluster_contents[decrypt_text], c_d_key)
                        for lines in range(0, len(cluster_contents)):
                            if cluster_contents[lines][-1] == "\n":
                                cluster_contents[lines] = cluster_contents[lines][:-1]
                        new_cluster_contents = cluster_contents.copy()[0]
                        cluster_contents = new_cluster_contents.split("\n")
                    except ValueError:
                        print("The Decryption Key must be in range of 0 to 999999.")
                else:
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
                print("Import File Is Corrupted Or Invalid Key Passed.")
            except (FileNotFoundError, IsADirectoryError):
                print("Invalid File/Directory.")
            except KeyboardInterrupt:
                pass

        # Sets a data item as a value to a key in the cluster
        elif cmd[0] == "set" and len(cmd) >= 4:
            try:
                # Gets the list of all the existing keys in the cluster.
                cluster_existing_keys = list(cluster.keys())
                # Does not allow the user to set a value to key which already has a value.
                if cmd[1] in cluster_existing_keys:
                    print("Key Already Exists.")
                    continue
                else:
                    data_set = cmd[3]
                    # Sets a numeric value to a key.
                    if cmd[2] == "num":
                        if len(cmd) == 4:
                            cluster[cmd[1]] = float(eval(data_set))
                        # Evaluates a mathematical expression.
                        elif len(cmd) > 4:
                            data_set = ""
                            for set_num_data in range(3, len(cmd)):
                                data_set = data_set + lib.del_left_zeros(cmd[set_num_data]) + " "
                            cluster[cmd[1]] = float(eval(data_set))
                    # Sets a alphabetic value to a key.
                    elif cmd[2] == "alpha":
                        if len(cmd) == 4:
                            cluster[cmd[1]] = str(data_set)
                        # If the value contains spaces.
                        elif len(cmd) > 4:
                            set_data = ""
                            for set_data_concat in range(3, len(cmd)):
                                set_data = set_data + cmd[set_data_concat] + " "
                            set_data = set_data[:-1]
                            cluster[cmd[1]] = set_data
                    else:
                        continue
            except (NameError, ValueError):
                print("Invalid Datatypes.")

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
                change_value = cmd[3]
                # For typecasting and for the values which contain spaces.
                try:
                    if cmd[2] == "num":
                        change_value = ""
                        for join_change_value in range(3, len(cmd)):
                            change_value = change_value + lib.del_left_zeros(cmd[join_change_value]) + " "
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

        # Gets a value from the Cluster, the Mess or the Book.
        elif cmd[0] == "get":
            try:
                if cmd[1] == "cluster":
                    print(cluster[cmd[2]])
                elif cmd[1] == "mess":
                    print(mess[int(cmd[2]) - 1])
                elif cmd[1] == "book":
                    print(str(book[cmd[2]][int(cmd[3]) - 1][int(cmd[4]) - 1]))
            except (IndexError, KeyError):
                print("Item Not Found.")

        # Removes a data item from the cluster.
        elif cmd[0] == "rem" and len(cmd) >= 1:
            try:
                cluster_keys1 = list(cluster.keys())
                # Removes the last data item from the cluster if the key is not supplied.
                if len(cmd) == 1:
                    del cluster[cluster_keys1[-1]]
                # Removes one or multile data item(s) from the cluster with the key(s) supplied.
                else:
                    for rem_several in range(1, len(cmd)):
                        try:
                            del cluster[cmd[rem_several]]
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
            b_data_space = list(book.keys())
            b_data_space_contents = list(book.values())
            book_all_values = []
            for all_values in range(0, len(b_data_space_contents)):
                for add_values in range(0, len(b_data_space_contents[all_values])):
                    for add_more_values in range(0, len(b_data_space_contents[all_values][add_values])):
                        book_all_values.append(b_data_space_contents[all_values][add_values][add_more_values])
            # Shows a "Not Found." message if the item is found nowhere.
            if not((search in c_keys) or (search in c_values) or (search in mess) or (search in b_data_space) or(search in book_all_values)):
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
                for search_data_space in range(0, len(b_data_space)):
                    if search == b_data_space[search_data_space]:
                        print("Location: Book\t Itemtype: Dataspace\t Position: " + str(search_data_space + 1))
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

    except IndexError:
        print("Missing Arguments or Extra Arguments.")

    except KeyboardInterrupt:
        print("\n\nBye.")
        break
log.close()