file = open('./text.txt')
# print(file.read())
# print(file.readline()) #esto es un iterable que me imprime el archivo linea por linea
# print(file.readline())
# print(file.readline())
# print(file.readline())

#esto es una forma ineficiente de hacerlo
for line in file:
  print(line)
file.close()

#acá lo que hago es que con el with no tengo que 
#abrir ni cerrar el archivo

with open('./text.txt') as file:
  for line in file:
    print(line)