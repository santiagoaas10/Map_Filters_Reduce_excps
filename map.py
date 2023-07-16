
#pa hacer operaciones entre listas
numbers = [1, 2, 3, 4]
numbers_v2 = []
for i in numbers:
  numbers_v2.append(i * 2)

numbers_v3 = list(map(lambda i: i * 2, numbers)) #lamba entrada:salida, tupla a iterar

print(numbers)
print(numbers_v2)
print(numbers_v3)

numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

print(numbers_1)
print(numbers_2)
result = list(map(lambda x, y: x + y, numbers_1, numbers_2)) #entran x,y sale x+y y serán iterados esos x y en listas numbers_1 y numbers_2
print(result)




#map con diccionarios
#convertimos diccionario a lista
items = [
  {'product':'camisa',
   'price':100
  },

  {'product':'pantalones',
   'price':300
  },
  
    {'product':'pantalones',
    'price':200
    }
]

#acá se recorre el diccionario y se hace una lista a partir de los elementos que hay en la llave price
prices=list( map(lambda item: item['price'], items) ) #recibes un diccionario, devuelves ese diccionario evaluado en price, hazlo con el dicionario items
print(prices)

#ejm2
items2 = [
  {'product':'camisa',
   'price':100
  },

  {'product':'pantalones',
   'price':300
  },
  
    {'product':'pantalones',
    'price':200
    }
]

def add_taxes(item):
  
  item['taxes']=item['price']*.19
  return item

new_items = list(map(add_taxes,items2))#lambda ya no se hizo con una fnc lambda sino con una fnc normalita
print(new_items)
print(items2)#se puede apreciar que la función map me modifica también items2, el array oginal
#vamos a ver cómo quitar la referencia de memoria entre  items2 y new items
#por ello veremos map con inmutabilidad
