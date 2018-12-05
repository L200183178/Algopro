##Practicum 9 - Activity 1 - Eza Ammar

berkas = open('L200183178','w')
berkas.write('L200183178 \n')
berkas.write("30-05-2000 \n')
berkas.write('Mohammad Faqih Eza Ammar \n')
berkas.close()
             
##Practicum 9 - Activity 2 - Eza Ammar

berkas = open('L200183178','w')
berkas.write('L200183178 \n')
berkas.write('30/05/2000 \n')
berkas.write('Mohammad Faqih Eza Ammar \n')
berkas.write('Solo \n')
berkas.close()
             
import shelve
a = open('L200183178','r')
NIM = a.readline()
Dob = a.readline()
Name = a.readline()
City = a.readline()
a.close()
             
a = shelve.open('Eza')
a['b'] = [Name, City, Dob, NIM]
a.close()

a = shelve.open('Eza')

print (a['b'][0])
print (a['b'][1])
print (a['b'][2])
print (a['b'][3])
             
##Practicum 9 - Activity 3 - Eza Ammar

import shelve
a = open('L200183178','r')
NIM = a.readline()
Dob = a.readline()
Name = a.readline()
City = a.readline()
a.close()

a = shelve.open('Eza')
a['b'] = [Name, City, Dob, NIM]
a.close()
             
##Practicum 9 - Activity 4 - Eza Ammar

import shelve
a = shelve.open('Eza')
print ('Name :' , a['b'][0])
print ('City :' , a['b'][1])
print ('Dob   :" , a['b'][2])
print ('NIM  :' , a['b'][3])