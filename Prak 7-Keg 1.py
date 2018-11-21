##Practicum 7, Act 1 - Eza Ammar

f = {'triangle' : 'L = 0.5 * a * t', 'square' : 'L = s ** 2', 'rectangle' : 'L = p * l', 'circle' : 'L = pi * r ** 2', 'parallelogram' : 'L = a * t'}

print ('''
        No  |   Nama Bangun         |   Rumus Luas
      ------|-----------------------|----------------
      1     |   triangle            | %s
      2     |   square              | %s
      3     |   rectangle     	     | %s
      4     |   circle              | %s
      5     |   parallelogram       | %s)

'''%(f['triangle'], f['square'], f['rectangle'], f['circle'], f['parallelogram']))