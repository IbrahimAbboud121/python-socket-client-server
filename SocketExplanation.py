import socket #socket is port + IP,this librarie allow python programs to send and receive data over the internet
import threading #allow python to run multiple tasks at the same time(because python run line by line)


HEADER=64#the maximum length is 64 digits=64 max character=512 bits
PORT = 5050 #IP Address:Identifies which device,Port:Identifies which program/service on that device
DISCONNECT_MESSAGE="!DISCONNET" #to check if any clients has been disconnected
""" 
Ports 0–1023 are reserved for system services (e.g., 80 for HTTP, 25 for email).

Port 55 may already be in use by the OS.

Using ports below 1024 often requires administrator/root permissions.

To pick a safe port:

Choose 1024 or higher to avoid system conflicts.

Common easy choices: 5000, 8000, 8080, 3000, 5050.

Avoid well-known service ports like 80 (HTTP), 443 (HTTPS), 3306 (MySQL), 5432 (PostgreSQL)
"""


SERVER="192.168.1.12"
"""
Your literal computer's local IP , windows+R,type cmd then in your cmd type ipconfig
i can also do SERVER=socket.gethostbyname(socket.gethostname()) will return 192.168.1.12
 """
 
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
"""
socket.socket() = "I want to build a mailbox"

You're telling Python to create a communication endpoint (like building a mailbox)

socket.AF_INET = "Make it for street addresses"

AF_INET means the mailbox will use IP addresses (like 192.168.1.1) and port numbers here its 192.168.1.12

It's like saying your mailbox should work with normal street addresses, not GPS coordinates

socket.SOCK_STREAM = "Make it with a reliable delivery system"

This means it will use TCP protocol

Like having a tracking number and confirmation for your mail - reliable but slower

(The alternative, SOCK_DGRAM, would be UDP - like throwing a letter and hoping it arrives)
"""
ADDR=(SERVER,PORT)
server.bind(ADDR)

"""
ADDR = (SERVER, PORT)
Think of ADDR as your mailbox's complete address label:

SERVER = Your street address (e.g., "123 Main Street")

PORT = Your apartment number (e.g., "Apartment 5050")

Together: ADDR = ("123 Main Street", "Apartment 5050")

So ADDR tells everyone exactly where to find your specific mailbox on your computer.

server.bind(ADDR)
Think of bind() as nailing your mailbox to your house:

You're physically attaching your mailbox (the server) to your specific address (ADDR).

Why nail it down (bind it)?

Without binding: Your mailbox is just floating in space - no one knows where to send mail

With binding: You're saying "This server lives at this specific IP address and port"
"""


def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected=True
    while connected:
        msg_length=conn.recv(HEADER).decode('utf-8')
        msg_length=int(msg_length)
        msg=conn.recv(msg_length).decode('utf-8')
        if msg == DISCONNECT_MESSAGE:
            connected=False
        print(f"[{addr}] {msg}")
    conn.close()
"""
conn.recv() ALWAYS returns BINARY DATA (bytes) like "5_______________" means that you will receive an message with 5 bytes 
long message,.decode Converts the received bytes to a UTF-8 string,then the string is transformed into integer 
then finnaly msg contains the exact message i want to receive









"""
def start():
    server.listen() #listenning  for new connections
    while True:
        conn,addr=server.accept()
        thread=threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
"""
def start():
Think of this as opening your pizza shop for business.

server.listen()
This is putting up your "OPEN FOR BUSINESS" sign:

You're telling the world: "I'm ready to accept customers!"

The mailbox/pizza shop is now actively waiting for people to come

while True:
This means "Stay open FOREVER, 24/7":

Without this, your shop would open for 1 customer then close

while True: = "Never stop accepting customers"

addr, conn = server.accept()
This is the actual handshake when a customer arrives:

Break it down:

server.accept() = "Wait for someone to come to my door"

Your program FREEZES here until someone connects

Like a doorman waiting for the next guest

When someone arrives:

conn = The actual connection with the customer,here the connection is TCP
so basically conn is the path where the client and server communicate

Think: A direct phone line to this specific customer

addr = That customer's home address

Their IP address and port (so you know where they're calling from)
                           
Thread Explanation - Simple Analogy:
The Problem Without Threads:
Imagine you have ONE waiter in your pizza shop:

Customer A arrives, waiter takes their order

While cooking A's pizza, Customer B arrives

Waiter says: "Sorry, I can only serve ONE person at a time!"

B has to wait until A's pizza is DONE

This is blocking - one customer blocks all others.

The Solution With Threads:
python
thread = threading.Thread(target=handle_client, args=(conn, addr))
thread.start()
What This Does:
Think of it like hiring a NEW waiter for EACH customer:

text
Customer Alice arrives → Hire Waiter 1 → Serve Alice
Customer Bob arrives   → Hire Waiter 2 → Serve Bob
Customer Carol arrives → Hire Waiter 3 → Serve Carol
Now all customers get served SIMULTANEOUSLY!

Breaking Down the Code:
python
# 1. When a client connects:
conn, addr = server.accept()  # Customer walks in

# 2. Create a thread (hire a waiter):
thread = threading.Thread(
    target=handle_client,  # WHAT the waiter should do
    args=(conn, addr)      # WHICH customer to serve
)

# 3. Start the thread (put waiter to work):
thread.start()  # "Go serve this customer!"                           
                           
                           
print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}") :   
 the number of threads-1 is the same as the number of connections (he number of clients) so we substract 1
  because our device  uses the server, so the main device is waiting , i dont want to count it,i want only to 
  count the clients
  
  
  
"""



print("[starting] server is starting...")
start()