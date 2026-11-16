import socket
import threading
import json

host = '0.0.0.0'
port = 8080

def send_username(uname):
    data = {
        "type": "username",
        "value": uname
    }
    return json.dumps(data)

s = socket.socket()
s.connect((host, port))

print("connected to server")
username = input("Enter a username: ")
data = send_username(username).encode()
s.send(data)

def send_message(msg):
    data = {
        "type": "message",
        "value": msg
    }
    return json.dumps(data)



def recieve_messages():
    while True:
        message = s.recv(1024)
        
        if not message:
            break
        
        print(message.decode())
        print("> ", end="", flush=True)
        
t = threading.Thread(target=recieve_messages)
t.start()

while True:
    message = input("> ")
    data = send_message(message)
    s.send(data.encode())