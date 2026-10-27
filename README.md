# TCP Chat Server

Minimal TCP chat server built from scratch in Python using raw sockets and threading.

Step-by-step portfolio project covering socket programming, protocol design, and concurrent client handling.

## Progress

### Step 1: Bare minimum TCP server (`server.py`)
Single-connection server that binds to a port, accepts one client, reads one message, and exits. Covers `socket()`, `bind()`, `listen()`, `accept()`, `recv()`, and `SO_REUSEADDR`.

### Step 2: Bare minimum TCP client (`client.py`)
Connects to the server, sends one message, and exits. Covers `connect()`, `sendall()`, and the TCP three-way handshake.

### Step 3: Persistent connections (`server.py`, `client.py`)
Added `while True` loops so the connection stays alive for multiple messages. Server detects client disconnect via empty `recv()` (TCP FIN). Client catches `ConnectionRefusedError` and supports graceful exit with `quit`.

### Step 4: Threading and multi-client broadcast (`server.py`)
Server now accepts multiple clients concurrently using `threading.Thread`. Each client gets its own thread running a `handle_client` function. Messages are broadcast to all other connected clients via a shared `clients` list. Cleanup removes disconnected sockets from the list.