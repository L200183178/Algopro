import socket

hostname = 'localhost'
message = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname,50003))
print "Communication Program - Server"
while message.lower() != 'quit':
    message = raw_input('Command: ')
    s.send(message)
    if message.lower == 'quit':
        s.close()
        break
    elif message.lower() != 'quit':
        response = s.recv(1024)
        print 'Response:',response
s.close()