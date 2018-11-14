##Account Program
##Made by Eza L200183178

import random

Name = 'Mohammad Faqih Eza Ammar'
Date_of_Birth = '30 Mei 2000'
Nickname = 'Eza'

Shortname = Name[0] + '.' + Name[6] + '.' + Name[12] + '.' + Name[-7:]
Username = Name[0] + Date_of_Birth[9-11] + Date_of_Birth[-4:]
Password = Name[0:4] + str(random.randint(0,1000))

print ('Shortname =',Shortname+'\n'+'Username =',Username+'\n'+'Password =',Password)