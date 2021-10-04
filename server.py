import socket
import threading

ip_address = '159.28.22.5'
port_number = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip_address, port_number))
server.listen()

users = []
usernames = []

def broadcast(message):
    for user in users:
        user.send(message)
        
def handle(user):
    while True:
        try:
            message = user.recv(1024)
            broadcast(message)
        except:
            index = users.index(user)
            users.remove(user)
            user.close()
            username = usernames[index]
            broadcast('{} left!'.format(username).encode('ascii'))
            usernames.remove(username)
            break
            
def receive():
    while True:
        user, address = server.accept()
        print("Connected with {}".format(str(address)))

        user.send('USER'.encode('ascii'))
        username = user.recv(1024).decode('ascii')
        usernames.append(username)
        users.append(user)

        print("{} Joined".format(username))
        broadcast("{} joined!".format(username).encode('ascii'))
        user.send('Connected to server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(user,))
        thread.start()
             
receive()