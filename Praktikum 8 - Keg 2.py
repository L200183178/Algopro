def convertTemp(C = 0, F = 0):
    'Convert temperature from Celcius to Fahrenheit and Vice Versa'
    temp = 0
    if (C == 0) and (F == 0):
        print ('Temperature 0 Celcius is same as 32 Fahrenheit')
    elif (C == 0) and (F != 0):
        temp = (F - 32) * 5/9
        print ('Temperature', F, 'Fahrenheit is same as', int(temp), 'Celcius')
    elif (C != 0) and (F == 0):
        temp = (C * 9/5) + 32
        print ('Temperature', C, 'Celcius is same as', int(temp), 'Fahrenheit')