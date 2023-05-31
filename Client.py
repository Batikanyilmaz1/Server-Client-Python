import socket
# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect(('127.0.0.1', 555))
client.send(str.encode("Client says Welcome"))
response = client.recv(1024)

while True:
    # get Input's
    name = input(response.decode())
    client.send(str.encode(name))
    response = client.recv(1024)
client.close()
