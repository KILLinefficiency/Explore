from flask import Flask
import memory_structures as ms

server = Flask(__name__)

@server.route("/")
def index():
    return "hey."

@server.route("/mess")
def mess():
    return open("mess_file.txt", "r").read()
    
@server.route("/cluster")
def cluster():
    return open("cluster_file.txt", "r").read()
    
if __name__ == "__main__":
    server.run(debug = True, host = "0.0.0.0")
