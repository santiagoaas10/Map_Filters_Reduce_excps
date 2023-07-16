import sys 
print(sys.path)

import re #modulo de expresiones regulares
text='mi numero de telefono es 31342424, el codigo del pais es 57, mi num dela suerte es 2'
result=re.findall('[0-9]+', text)


import time
timestamp= time.time()
print(time)
local = time.localtime()
result = time.asctime(local)
print(result)


import collections
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers)#da la frecuencia de cada uno de los elementos de la lista en forma de dict
print(counter)
