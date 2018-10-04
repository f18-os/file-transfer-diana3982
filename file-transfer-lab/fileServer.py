import sys, socket, os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create socket
host = ''
#serv_add = ('localhost', 10000)
sock.bind((host,2525))
sock.listen(10) # listens for up to 10 incoming connections
print('Server Active')
ifFileFound = 0

while True:
    print('... waiting to connect ...')
    connection, client_add = sock.accept()
    recievedFile = connection.recv(1024)
    currDir = os.getcwd()
    for file in os.listdir(currDir):
        if file == recievedFile:
            recievedFile = 1
            break
    if recievedFile == 0:
        print recievedFile + (" could not be found on the server")
    else:
        print(str(recievedFile)+ " was found!")
        uploadFile = open(currDirrecievedFile,"rb")
        readFile = uploadFile.read(1024)
        while readFile:
            connection.send(readFile)
            readFile = uploadFile.read(1024)
        print("File sent")
    break
connection.close() # to make sure the connection is closed
sock.close() # to make sure the socket is closed
