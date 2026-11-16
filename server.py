import socket
import threading
import json

clients = []

def handle_client(conn, addr):
    print("[thread] starting")
    
    while True:
        #recv message
        message = conn.recv(1024)
               
        if not message:
            break
        
        data = json.loads(message.decode())
        type = data["type"]
        
        if type == "username":
            username = data["value"]
            continue
        
        
        if type == "message":
            message = data["value"]
            
        broadcast = f"{username}: {message}"
         
        for client in clients:
            if client != conn:
                client.sendall(broadcast.encode()) 
                
  
        print("[thread] client:", addr, "recv:", message)

host = "0.0.0.0"
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#soluton for "[Error 89] Address already in use". Use before bind()
s.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_REUSEADDR,
    1
)
s.bind((host, port))
s.listen(1)

threads = []

while True:
    print("Waiting for client")
    conn, addr = s.accept()
    clients.append(conn)
    
    print("Client:", addr)
    
    t = threading.Thread(target=handle_client, args=(conn, addr))
    t.start()

    threads.append(t)
