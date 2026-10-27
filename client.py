import socket
import threading  # need a background thread to receive while we type

HOST = "127.0.0.1"
PORT = 9999

# creates a TCP socket, same as the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# three-way handshake to the server
client.connect((HOST, PORT))

# runs in a background thread, listens for messages from other clients
def receive():
    while True:
        try:
            data = client.recv(1024)
            if not data:
                break
            print(data.decode("utf-8"))
        except:
            break


# start recv thread before the input loop so we don't miss any messages
thread = threading.Thread(target=receive)
thread.daemon = True  # dies when main thread exits, no zombie threads
thread.start()

# send loop: type messages until quit
while True:
    message = input()
    if message.lower() == "quit":
        break
    client.sendall(message.encode("utf-8"))

# TCP FIN packet to the server
client.close()