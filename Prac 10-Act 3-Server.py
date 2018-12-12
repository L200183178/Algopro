import socket

def square(s=0):
    return s*s
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50020))
s.listen(5)
print "Calculation server is ready"
data = ''
while data.lower() != 'out':
    komm, addr = s.accept()
    while data.lower() !='out':
        data = komm.recv(1024)
        print 'message:', data
        if data.find("parameter")!= -1:
            param,value= data.split("=")
            if param == "side parameter":
                s = float(value)
                b = value
                komm.send("parameter noted")
        elif data == 'count':
            komm.send('area of square with side of {} is {}'.format (b,square(s)))
        else:
            komm.send('none')