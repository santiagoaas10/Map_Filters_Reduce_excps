#cualquier error que pase en esta parte del programa él la va a captuar 
# y podremos hacer lo que queramos con él
#y no para el programa!


#versión 1 del try: apenas encuentra un error mira sólo ese except y no revisa los otros
try:
    print(0/0)
except ZeroDivisionError as error:
    print(error)

try:
  print(0 / 0)
  assert 1 != 1, 'Uno no es igual que uno'
  age = 10
  if age < 18:
    raise Exception('No se permiten menores de edad')
except ZeroDivisionError as error:
  print(error)
except AssertionError as error:
  print(error)
except Exception as error:
  print(error)

print('Hola')
print('Hola 2')

#versión 2, por partesitas:

try:
   assert 1 != 1, 'Uno no es igual que uno'
except AssertionError as error:
    print(error)

try: 
    age = 10
    if age < 18:
        raise Exception('No se permiten menores de edad')
except Exception as error:
  print(error)  

