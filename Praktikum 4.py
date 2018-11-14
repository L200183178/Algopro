Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Name = 'Mohammad Faqih Eza Ammar'
>>> NIM = 178
>>> Height = 1.65
>>> Weight = 52
>>> BirthYear = 2000
>>> Me = (BirthYear, Weight, Height, NIM, Name)
>>> Data = [BirthYear, Weight, Height, NIM, Name]
>>> type(Me)
<class 'tuple'>
>>> #This means that that the type of 'Me' is Tuple which like a list but with '(' and ')'
>>> Me[0]
2000
>>> #this shows the result of 'Me' but with slicing '0' which is 'BirthYear'
>>> a = NIM%4; Me[a]
1.65
>>> #this shows the slicing of 'Me' but with slicing value of 'NIM' Modulus 4
>>> type (Me[a])
<class 'int'>
>>> #this means that the type of 'Me[a]' is an integer
>>> Me[a:4]
(1.65, 178)
>>> #this shows slicing of Me that shows Height and NIM
>>> type(Me[4])
<class 'str'>
>>> #This shows the type of 'Me[4]' is string
>>> Me[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    Me[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> #this shows that we cannot change it because it is a tuple
>>> type(Data)
<class 'list'>
>>> #this shows that the type of 'Data' is List
>>> type (Data[4])
<class 'str'>
>>> #this shows that the type of 'Data[4]' or slicing of Data in 4th number is a string
>>> Data [4] [5]
'm'
>>> #this shows the result of the data slice
>>> Data [4][a:6]
'hamm'
>>> #this shows the result of the data slice
>>> Data [0] = 'ok';Data
['ok', 52, 1.65, 178, 'Mohammad Faqih Eza Ammar']
>>> #the result of changing a slice of the data to 'ok'
>>> Data[-a]
'178'
>>> #this is the result of reversed slicing of 'a'
>>> range (a)
range(0, 2)
>>> #this shows the range from data 'a' and the result is 2 from 0
