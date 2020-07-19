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
    "Memory Location Not Specified.",
    "Cannot enable limit to multiple commands at once."
]

def error(error_code):
    global explore_errors
    print(explore_errors[int(error_code) - 1])