import sys, socket, os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create socket
host = ''
#serv_add = ('localhost', 10000)
sock.bind((host,2525))
sock.listen(10) # listens for up to 10 incoming connections
print('Server Active')

while True:
    print('... waiting to connect ...')
    connection, client_add = sock.accept()
    cmd = connection.recv(1024)
    print('connection esablished from ', repr(client_add))
    print('Client $', (cmd))
    if(cmd == 'quit'):
        break
    else:
        try:
            string = cmd.split(' ', 1) # considers put and get
            fileName = string[1]

            if(string[0] == 'put'):
                with open(fileName,'wb') as f:
                    while True:
                        print('... recieving file ...')
                        data = sock.recv(1024)
                        if not data:
                            break
                        f.write(data)
                    f.close()
                    print('File recieved')

            elif(string[0] == 'get'):
                try:
                    with open(fileName, 'rb') as f:
                        for data in f:
                            connection.sendall(data)
                    print('Successfully sent')
                except IOError:
                    print('File is not found on server!')
                    break
            else:
                print('Unknown Command. Goodbye.')
                break
        except IndexError:
            print('Unknown Command. Goodbye.')
            break
connection.close() # to make sure the connection is closed
sock.close() # to make sure the socket is closed
