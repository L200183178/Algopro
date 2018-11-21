##Practicum 7, Act 2 - Eza Ammar

f = 'Eza'
q = input('Enter Your Password : ')

for x in range (2):
    if q==f:
        print('Login Success')
        break
    elif q!=f:
        print('Sorry, Incorrect Password')
        q=input('Enter Your Password : ')
    else:
        print('You have entered wrong password 3 times, Access Denied')