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