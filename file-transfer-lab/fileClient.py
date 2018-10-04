import sys, socket

#serv_add = ('localhost', 10000)
hostIP = socket.gethostbyname(socket.gethostname())
str(hostIP)


def put(userInput):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((hostIP, 2525))
    sock.send(userInput)
    fileName = string[1]

    try:
        with open(fileName, 'rb') as f:
            for data in f:
                sock.sendall(data)
        print(string[1] + ' sent to server.')
        sock.close()
        return
    except IOError:
        print('File not found. Cannot PUT.')
        return
def get(userInput):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((hostIP, 2525))
    sock.send(userInput)
    fileName = string[1]

    with open(fileName, 'wb') as f:
        while True:
            data = sock.recv(1024)
            if not data:
                break
            f.write(data)
    f.close()
    print(string[1] + ' successfully recieved.')
    sock.close()
    return

cmd = raw_input("Input the name of file you want to pull from server : <get/put> <filename.txt>")
temp = "temp" # place holder for the data on the file to be read

while True:
    try:
        string = cmd.split(' ', 1) # considers put and get
        if(string[0] == 'put')
            put(cmd)
        elif(str(string[0]) == 'get')
            get(cmd)
    except IndexError:
        print('Unknown Command. Goodbye.')
        break
