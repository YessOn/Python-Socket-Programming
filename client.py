import socket

# Constants:
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

# Clients Creation:
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# Messages Sender:
def send(msg):
	message = msg.encode(FORMAT)
	msg_len = len(message)
	send_len = str(msg_len).encode(FORMAT)
	send_len += b' ' * (HEADER - len(send_len))
	client.send(send_len)
	client.send(message)
	print(client.recv(2048).decode(FORMAT))

if __name__ == '__main__':
        
        send("Hello Dude!")
        input()
        send("You Should Consider Our Friendship Progres.")
        input()
        send("Okay Man I will.")
        input()
        send("By Yess!")


        send("!CLOSE")
