from flask import Flask
from flask import request
import werkzeug.serving
import thread

server = Flask(__name__)

def startServer():
    thread.start_new_thread(serverThread,())

def serverThread():
    server.run(host='0.0.0.0',port=8000)

@server.route('/packages', methods=['POST'])
def postpackage():
    return "postpackage - ok"

@server.route('/', methods=['GET'])
def endpoints():
    return "endpoints - ok"

@server.route('/api-doc', methods=['GET'])
def apidoc():
    return "apidoc - ok"

