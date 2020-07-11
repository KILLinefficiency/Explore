import lib
from requests import get

mess = ""
cluster = ""

data_types = ["num", "num\n", "alpha", "alpha\n"]

# Scrapes data from the Server and stores it into the Mess, the Cluster or both.
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

# Sets data from the Mess, the Cluster or both to server files.
def set_data(memory):
    global mess
    global cluster
    memory_file = open(("." + memory + "_server_file.txt"), "w+", encoding = "utf-8")
    if memory == "mess":
        memory_file.write(mess)
    elif memory == "cluster":
        memory_file.write(cluster)
    memory_file.close()

# Splits the Mess into lines and returns them as a list.
def gen_mess_values():
    global mess
    mess_values = mess.split("\n")
    mess_values = lib.del_spaces(mess_values)
    return mess_values

# Splits the Cluster into lines and returns them as a list.
def gen_cluster_values():
    global cluster
    cluster_values = cluster.split("\n")
    cluster_values = lib.del_spaces(cluster_values)
    return cluster_values

# Returns all the values of the Mess as a Python List.
def gen_mess_list():
    global mess
    true_mess = []
    mess_values = gen_mess_values()
    for add_to_true_mess in range(0, len(mess_values)):
        mess_items = mess_values[add_to_true_mess].split(" ")
        if mess_items[-1] == "num":
            true_mess.append(float(mess_items[0]))
        elif mess_items[-1] == "alpha":
            true_mess.append(str(lib.join_string(mess_items, 0, len(mess_items) - 2)))
    return true_mess

# Returns all the values of the Cluster as a Python Dictionary.
def gen_cluster_dict():
    global cluster
    true_cluster = {}
    cluster_values = gen_cluster_values()
    for add_to_true_cluster in range(0, len(cluster_values)):
        cluster_items = cluster_values[add_to_true_cluster].split(" ")
        if cluster_items[-1] == "num":
            true_cluster[cluster_items[0]] = float(lib.join_string(cluster_items, 1, len(cluster_items) - 2))
        elif cluster_items[-1] == "alpha":
            true_cluster[cluster_items[0]] = str(lib.join_string(cluster_items, 1, len(cluster_items) - 2))
    return true_cluster

# Code for operations on the Mess.

# Adds "\n" character to every string in the given array.
def add_n(items):
    for add_n in range(0, len(items)):
        if items[add_n][-1] != "\n":
            items[add_n] = items[add_n] + "\n"

# Adds value supplied with data type into the Mess
def add_mess(value, data_type):
    global mess
    mess = mess + str(value) + " " + data_type + "\n"

# Inserts the provided data with data type at a particular position in the Mess.
def insert_mess(value, data_type, position):
    global mess
    mess_values = gen_mess_values()
    add_n(mess_values)
    mess = ""
    mess_values.insert(position - 1, str(value) + " " + data_type + "\n")
    for concat_mess in range(0, len(mess_values)):
        mess = mess + mess_values[concat_mess]

# Gets a value from the Mess after providing the position of it.
def get_from_mess(position):
    global mess
    mess_items = mess.split("\n")
    mess_items = lib.del_spaces(mess_items)
    required_item = mess_items[position - 1]
    required_item = required_item.split()
    value = lib.join_string(required_item, 0, len(required_item) - 2)
    if required_item[-1] == "num":
        value = float(value)
    elif required_item[-1] == "alpha":
        value = str(value)
    if position > 0:
        return value
    else:
        pass

# Replaces an existing data item in the Mess with the provided data item.
def move_in_mess(value, data_type, position):
    global mess
    mess_values = gen_mess_values()
    add_n(mess_values)
    del mess_values[position - 1]
    mess_values.insert(position - 1, str(value) + " " + data_type + "\n")
    mess = ""
    for concat_mess in range(0, len(mess_values)):
        mess = mess + mess_values[concat_mess]

# Returns the number of items in the Mess.
def count_mess():
    mess_values = gen_mess_values()
    return len(mess_values)

# Removes all the contents of the Mess.
def clean_mess():
    global mess
    mess = ""

# Removes an item from the Mess after giving the position of it.
def pop_from_mess(items):
    global mess
    mess_values = gen_mess_values()
    add_n(mess_values)
    if items == []:
        mess_values[-1] = ""
    else:
        for del_item in range(0, len(items)):
            mess_values[int(items[del_item]) - 1] = ""
    mess_values = lib.del_spaces(mess_values)
    mess = ""
    for concat_mess in range(0, len(mess_values)):
        mess = mess + mess_values[concat_mess]

# Code for the oprations of the Cluster.

# Adds the Key and Value in the Cluster.
def add_cluster(key, value, data_type):
    global cluster
    cluster = cluster + str(key) + " " + str(value) + " " + data_type + "\n"

# Returns all the Keys from the Cluster as a list/
def gen_cluster_keys():
    cluster_items = gen_cluster_dict()
    cluster_keys = list(cluster_items.keys())
    return cluster_keys

# Returns all the Values from the Cluster as a list.
def gen_cluster_key_values():
    cluster_items = gen_cluster_dict()
    cluster_values = list(cluster_items.values())
    return cluster_values

# Changes the Value of a Key with a given Values in the Cluster.
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

# Gets the Value of a Key from the Cluster.
def get_from_cluster(key):
    global cluster
    cluster_items = cluster.split("\n")
    cluster_items = lib.del_spaces(cluster_items)
    for search_item in range(0, len(cluster_items)):
        individual_item = cluster_items[search_item].split()
        if individual_item[0] == key:
            value = lib.join_string(individual_item, 1, len(individual_item) - 2)
            if individual_item[-1] == "num":
                return float(value)
            elif individual_item[-1] == "alpha":
                return str(value)

# Removes a Key-Value pair from the Cluster.
def rem_from_cluster(key):
    global cluster
    cluster_values = gen_cluster_values()
    add_n(cluster_values)
    for rem_items in range(0, len(cluster_values)):
        if lib.starts_with(cluster_values[rem_items], key):
            cluster_values[rem_items] = ""
    cluster_values = lib.del_spaces(cluster_values)
    cluster = ""
    for cluster_concat in range(0, len(cluster_values)):
        cluster = cluster + cluster_values[cluster_concat]

# Removes all the contents of the Cluster.
def clean_cluster():
    global cluster
    cluster = ""

# Returns the number of Keys/Values in the Cluster.
def count_cluster():
    cluster_values = gen_cluster_values()
    return len(cluster_values)

# Adds a content to a Memory Structure only when a data type is specified.
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

# Adds a content to a Memory Structure whether a data type is specified or not.
def add_to_ms_directly_unsafe(value, memory_structure):
    global mess
    global cluster
    if memory_structure == "mess":
        mess = mess + value
    elif memory_structure == "cluster":
        cluster = cluster + value
