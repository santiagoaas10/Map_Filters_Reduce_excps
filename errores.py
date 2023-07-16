# print(0 / 0)
# print(result)
print('Hola')

suma = lambda x,y: x + y
#este assert es como un  un if, que si se cumple continúa la ejecucion del programa y si no muestra un error assert
assert suma(2,2) == 4

print('Hola 2')

age = 10
if age < 18:
  #este es un error cuyo mensaje manejo yo y si entra a este raise muestra el error y para el programa
  raise Exception('No se permiten menores de edad')

print('Hola 2')

