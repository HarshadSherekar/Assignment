from flask import Flask

server = Flask(__name__)

@server.get('/')
def homepage():
    return "This is a home page"

@server.get('/welcome')
def welcome():
    return "<html><body><h1>Welcome to Student Management System</h1></body></html>"

server.run(host='0.0.0.0', port=4000, debug=True)