import socket
import random as gnr
from datetime import date

server_inet_address = ("127.0.0.1", 65430)

server_socket = socket.socket()
server_socket.bind(server_inet_address)
server_socket.listen()
print("Server start on "+str(server_inet_address[0])+":"+str(server_inet_address[1]))
connection, client_inet_address = server_socket.accept()
print("Client connection accepted from "+str(client_inet_address[0])+":"+str(client_inet_address[1]))

message = "AHOJ\n"
message_as_bytes = bytes(message, "utf-8")
print("Sending bytes:")
for byte in message_as_bytes:
    print(bin(byte))
connection.send(message_as_bytes)

citates = ["„Představte si to ticho, kdyby lidé říkali jen to, co vědí.“",
           "„Čtenář prožije tisíc životů, než zemře. Člověk, jenž nikdy nečte, prožije jen jeden.“",
           "„Správně vidíme jen srdcem. Co je důležité je očím neviditelné.“"]

while True:
    user_input = connection.recv(1024)
    user_input = user_input.decode("utf-8")
    if user_input == "citat":
        message = citates[gnr.randrange(2)] + "\n"
        message_as_bytes = bytes(message, "utf-8")
        connection.send(message_as_bytes)
    elif user_input == "getdate":
        message = str(date.today()) + "\n"
        message_as_bytes = bytes(message, "utf-8")
        connection.send(message_as_bytes)


connection.close()
print("Client connection closed")
server_socket.close()
print("Server is closed")
