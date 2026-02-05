import socket 
import threading 

HEADER=64
PORT = 5050
DISCONNECT_MESSAGE="!DISCONNET"
SERVER=socket.gethostbyname(socket.gethostname())
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ADDR=(SERVER,PORT)
server.bind(ADDR)


def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected=True
    while connected:
        msg_length=conn.recv(HEADER).decode('utf-8')
        if msg_length:
         msg_length=int(msg_length)
         msg=conn.recv(msg_length).decode('utf-8')
         if msg == DISCONNECT_MESSAGE:
            connected=False
         print(f"[{addr}] {msg}")
    conn.close()

def start():
    server.listen() #listenning  for new connections
    print(f"[LISTENING] server is lintening on {SERVER}")
    while True:
        conn,addr=server.accept()
        thread=threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")



print("[starting] server is starting...")
start()
