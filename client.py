import socket

HEADER = 64
FORMAT = "utf-8"
PORT = 5050
DISCONNECT_MSG = "!DISCONNECT"
SERVER = "127.0.1.1"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048))


while True:
    msg_send = input()
    if msg_send == "off":
        send(DISCONNECT_MSG)
        break
    send(msg_send)


