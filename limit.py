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

def set_limit(command, limit):
    cmd_limit[command] = limit

def rem_limit(commands):
    for rem_limits in range(0, len(commands)):
        del cmd_limit[commands[rem_limits]]
    for reset_counter in range(0, len(commands)):
        cmd_requests[commands[reset_counter]] = 0

def incr_limit_count(command):
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

