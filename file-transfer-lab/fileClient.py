import sys, socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#serv_add = ('localhost', 10000)
hostIP = socket.gethostbyname(socket.gethostname())
str(hostIP)
sock.connect((hostIP, 2525))

fileRequested = raw_input("Input the name of file you want to pull from server :  <filename.txt>")
temp = "temp" # place holder for the data on the file to be read

while True:
    sock.send(fileRequested)
    temp = sock.recv(1024) #saving the file to the temp string (buff size 1024)
    downloadFile = open(fileRequested, "wb")

    while temp:
        downloadFile.write(temp) # writing out the file
        temp = sock.recv(1024) # keep writing until EOF
    print("File Downloaded")
    break
sock.close()
