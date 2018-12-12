import socket

hostname = 'localhost'
message = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname,50002))
print "Communication Program - Self Identity"

while message.lower() != 'q':
    message = raw_input('Command: ')
    s.send(message)
    if message.lower() == 'Out':
        response = s.recv(1024)
        print 'Answer:', response
        s.close()
        break
    elif message.lower() != 'Out':
        response = s.recv(1024)
        print 'Answer:', response
s.close()
