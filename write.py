with open('./texs.txt', 'w+') as file: #con r+ tenemos permiso de leer y escribir pero NO de modificar lo anteriormente escrito, con w+ SI
  for line in file:
    print(line)
  file.write('nuevas cosas en este archivo\n')
  file.write('otra linea\n')
  file.write(' mas linea\n')