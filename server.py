import socket
import threading

# Constants:
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

# Server Setup:
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# Setup the environments to each client:
def handle_client(conn, addr):
	print(f'[NEW CONNECTION] {addr} Connected.')
	connected = True
	while connected:
		msg_len = conn.recv(HEADER).decode(FORMAT)
		if msg_len:
			msg_len = int(msg_len)
			msg = conn.recv(msg_len).decode(FORMAT)
			if msg == "!CLOSE":
				connected = False
			print(f"[{addr}]: {msg}")
			conn.send("Msg received".encode(FORMAT))
	conn.close()

# Start the Server & Listen to each client:
def start():
	server.listen()
	print(f"[LISTENING] Server is listening on {SERVER}")
	while True:
		conn, addr = server.accept()
		thread = threading.Thread(target=handle_client, args=(conn, addr))
		thread.start()
		print(f"[ACTIVE: ] -> {threading.activeCount() - 1}")

print("Server is strating...")

start()
