from flask import Flask
import memory_structures as ms

server = Flask(__name__)

index_page = """
    <h1 align = 'center'>Explore Server</h1>
    <br>
    <h3>Raw Data can be found at the following routes of this IP address:</h3>
    <h3><code>/mess</code></h3>
    <h3><code>/cluster</code></h3>
"""

@server.route("/")
def index():
    return index_page

@server.route("/mess")
def mess():
    mess_raw_data = open("mess_file.txt", "r", encoding = "utf-8")
    return mess_raw_data.read()
    
@server.route("/cluster")
def cluster():
    cluster_raw_data = open("cluster_file.txt", "r", encoding = "utf-8")
    return cluster_raw_data.read()
    
if __name__ == "__main__":
    server.run(host = "0.0.0.0")
