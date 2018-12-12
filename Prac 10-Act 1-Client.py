import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50002))
s.listen(5)
print "Communication Program - Self Identity"
data = ''
dic = {'Name':'Eza Ammar',
         'NIM':'L200183178',
         'Year':'2018',
         'Out':'Ready!!'}
while data.lower() != 'Out':
    komm, addr = s.accept()
    while data.lower() != 'Out':
        data = komm.recv(1024)
        print 'Command: ',data
        if dic.has_key(data):
            komm.send(dic[data])
        else:
            komm.send('Sorry, unknown command')
