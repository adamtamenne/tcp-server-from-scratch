import socket

HOST = "127.0.0.1"
PORT = "9999"


# Creates the socket object with 2 arguments:
# AF_INET means use IPv4 then SOCK_STREAM says use TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# tells the OS "let me rebind immediately", no time wait needed
server.setsockopt(socket.SOL_SOCKET, socket.so_REUSEADDR, 1)

# associates your socket with a specific IP and port
server.bind((HOST, PORT))

# switches the socket from "active" (for connecting out) to "passive" (for receiving connections)
# after this, the OS starts a queue of incoming connection requests and print confirmation
server.listen()
print(f"Server listening on {HOST}:{PORT}")

# stops and waits. accept() blocks until a client connects. When one does, it returns 2 things:
# a brand new socket just for talking to this one client. Your original server socket stays open to accept more connections (we'll use that later)
# a tuple like ("127.0.0.1", 52431) with the clients IP and their ephemeral port (a random high port the OS assigned them)
client_socket, address = server.accept()

# logs who connected
print(f"Connection from {address[0]}:{address[1]}")

# instead of reading once and quitting, the server now loops forever
# client calls close(), the OS sends a FIN packet. On the server side, recv() returns b"" empty bytes which is falsy in Python 
# that is your signal that the client hung up. Without this check, the loop would spin forever on empty reads
while True:                                
    data = client_socket.recv(1024)
    if not data:
        break
    print(f"address[0]: {data.decode('utf-8')}")

# reads up to 1024 bytes from the client. recv() returns raw bytes, 1024 is buffer size, blocks until data arrives
data = client_socket.recv(1024)

# converts the raw bytes back into a Python string so we can print it
print(f"Received: {data.decode('utf-8')}")

# Closes the connection to the client. TCP FIN packet sent.
client_socket.close()

# Closes the listening socket itself. releases port 9999.
server.close()