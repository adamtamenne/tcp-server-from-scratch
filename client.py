import socket

HOST = "127.0.0.1"
PORT = 9999

# creates a TCP socket, same as the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# three-way handshake to the server
client.connect((HOST, PORT))

# pushes the full message into the TCP send buffer
# sendall() is safer than send() because send() can silently send only part of your data if the kernel buffer is full. 
# sendall() loops until every byte is out.
message = input("Send a message: ")
client.sendall(message.encode("utf-8"))
print("Message sent.")

# TCP FIN packet to the server.
client.close()