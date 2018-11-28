kam = {'N':'L200183178', 'a':'Mohammad Faqih Eza Ammar', 'A':'Jayengan, Solo','G':'57152','L':'Solo','Q':'Jawa Tengah','J':'Indonesia'}

b= ('''
    Available Options :
    b to show help
    N to show NIM
    a to show Name
    A to show Adress
    G to show Postal Code
    L to show City
    Q to show Province
    J to show Nationality
    k to Exit
    ''')
print(b)
beb=0
while b !='k':
    beb = input('Select Option : ')
    if beb in kam.keys():
        print(kam[beb])
    elif beb=='b':
        print (b)
    else :
        print ('Please select from the available list')

print ('End of Session')