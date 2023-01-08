import time
import socket
import threading

PORT = 9999
SERVER = "192.168.1.87"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

def send(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)

def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client

def recv(connection, username):
    while True:
        msg = connection.recv(1024).decode(FORMAT)
        if f"[{username}]" not in msg:
            print(f"\r{msg}                         ")
            print("Message (q for quit): ", end="")

def start():
    answer = input("Would you like to connect (yes/no)? ")
    if answer.lower() != "yes":
        return
   
    connection = connect()
    username = input("What is your name? ")
    send(connection, username)

    thread = threading.Thread(target=recv, args=(connection, username), daemon=True)
    thread.start()

    while True:
        msg = input("Message (q for quit): ")

        if msg == "q":
            break

    send(connection, DISCONNECT_MESSAGE)
    time.sleep(1)
    print("Disconnected")

start()