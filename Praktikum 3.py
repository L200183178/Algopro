Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ##Activity 3, Eza L200183178
>>> Name = 'Mohammad Faqih Eza Ammar'
>>> NIM = 'L200183178'
>>> X = '1' + NIM [7:]
>>> a = int(X)
>>> b = len(Name)
>>> type (a)
<class 'int'>
>>> #this means that the type of (a) is an Integer because we  classified 'X' as 'int'
>>> type (b)
<class 'int'>
>>> #this means that the type of (b) is an Integer because we classify 'b' as length of the String
>>> a / b
49.083333333333336
>>> #this is the result of 'a' divided by 'b' and the result is Float
>>> a//b
49
>>> #this is the result of 'a' divided by 'b' but the result is Rounded
>>> 10*(a-999)
1790
>>> #this is the result 10 times 'a' minus '999' and the result is Integer
>>> b ** 2
576
>>> #this is the result of square 2 of 'b'
>>> a%b
2
>>> #this is the result of 'a' modulus 'b' and the results are the remain of 'a' divided by 'b'
>>> c = 12.5
>>> #we have set 'c' with value of '12.5'
>>> type (c)
<class 'float'>
>>> #this means that the type of (c) is Float
>>> a / c
94.24
>>> #this is the result of 'a' divided by 'c'
>>> a//c
94.0
>>> #this is the result of 'a' divide by 'c' but the result is Rounded
>>> a%c
3.0
>>> #this is the result of 'a' modulus 'c' and the results are the remain of 'a' divided by 'b'
>>> c>b
False
>>> #this is a boolean that says  the statement 'c>b' is false
>>> type (c > b)
<class 'bool'>
>>> #this means that the type of 'c > b' is a Boolean
>>> a>b and b>c
True
>>> #this means that both statement of 'a>b' and 'b>c' are true
>>> a > 1100 or b < 10
True
>>> #This means that one of them or all of the statement is true
>>> 
