from flask import Flask

server = Flask(__name__)

@server.post('/temperature/<float:temp>')
def post_temperature(temp):
    print(f"temp = {temp}")
    return f"{temp} is recieved"

server.run(host='0.0.0.0', port=4000, debug=True)