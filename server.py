from flask import Flask
from requests import get
import memory_structures as ms

def get_data(ip, memory):
    address = "http://" + ip + ":5000/" + memory
    data = get(address)
    return data.text

def launch_server():
    server = Flask(__name__)

    @server.route("/")
    def index():
        return "hey."

    @server.route("/mess")
    def mess():
        return ms.mess
    
    @server.route("/cluster")
    def cluster():
        return ms.cluster
    
    if __name__ == "__main__":
        server.run(debug = True, host = "0.0.0.0")

launch_server()