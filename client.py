import socket


HEADER=64
PORT = 5050
DISCONNECT_MESSAGE="!DISCONNET"
SERVER="192.168.1.12"
ADDR=(SERVER,PORT)
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode('utf-8')
    msg_length=len(message)
    send_length=str(msg_length).encode('utf-8')
    send_length+= b' '*(HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    
def Disconnect():
    send(DISCONNECT_MESSAGE)
    client.close()

send("HELLO WORLD") 
Disconnect()
