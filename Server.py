import socket
import datetime
import time

CONT = False # login checker

# Returns comparison results of login informations
def check_permisson(userName, passWord):
    if 'CMPE322' == userName.decode() and 'bilgiuni' == passWord.decode():
        return True
    else:
        return False

def login(clientConnection):
    global CONT
    clientConnection.send(str.encode('Enter your username: '))
    userName = clientConnection.recv(1024)
    clientConnection.send(str.encode('Enter your password: '))
    passWord = clientConnection.recv(1024)
    canUserLogin = check_permisson(userName, passWord)
    if canUserLogin:
        clientConnection.send(str.encode('You are OK to ask me date, time, capTurkey, quit..'))
        clientConnection.sendall(b'\n')
        CONT = True
    else:
        clientConnection.send(str.encode('Thank you for trying to login, goodbye..'))
        clientConnection.close()
            
def get_date():
    now = datetime.datetime.now().strftime("%Y.%m.%d -- %H:%M:%S")
    clientConnection.send(str.encode("Current Date-Time: {}".format(now)))

def get_time():
     now = datetime.datetime.now().strftime("%Y.%m.%d -- %H:%M:%S")
     clientConnection.send(str.encode("Current Time:{}".format(now.split('--')[-1])))

def get_Capital():
    clientConnection.send(str.encode('Ankara'))

def quit():
    global CONT
    CONT = False
    clientConnection.send(str.encode("Bye Bye..."))

# create a socket at server side using TCP / IP protocol
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket with server and port number 
server.bind(('0.0.0.0', 555))

# allow maximum 100 connection to the socket
server.listen(100)

print("Server started")
print("Waiting for client request..")

# wait till a client accept connection
clientConnection, clientAddress = server.accept()
				
# display client address
print("Connected client:", str(clientAddress))

print(clientConnection.recv(1024).decode())

login(clientConnection)

while CONT:
    clientConnection.send(str.encode('Please enter your command: '))
    data = clientConnection.recv(1024)

    if data.decode() == 'date':
        get_date()
    elif data.decode() == 'time':
        get_time()
    elif data.decode() == 'capTurkey':
        get_Capital()
    elif data.decode() == 'quit':
        quit()

    time.sleep(0.5)