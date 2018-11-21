##Practicum 7, Act 3 - Eza Ammar

f = input('Whats your name? : ')
q = float(input('What time is it? : '))

if q >= 21.00 and q <=23.59 :
    q = 'Night'
elif q >= 17.30 and D <=20.59:
    q = 'Evening'
elif q >= 12.01 and D <=17.29:
    q = 'Afternoon'
elif q >= 11.00 and q <=12.00:
    q = 'Noon'
elif q >= 0.00 and q <=10.59:
    q = 'Morning'

print('Good ' + q + ' ' + f + '!')
