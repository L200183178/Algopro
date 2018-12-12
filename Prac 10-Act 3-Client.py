import socket

hostname = 'localhost'
message = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50020))
print "calculate square area"
while message != 'out':
    message = raw_input('message :  ')
    s.send(message)
    if message.lower() == 'out':
        response = s.recv(1024)
        print 'response: -'
        s.close()
        break
    elif message.lower() != 'out':
        response = s.recv(1024)
        print 'response:', response
s.close()