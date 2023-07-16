'''
Para resolver este desafío, tu reto 
es utilizar la función map de Python y una función lambda 
para transformar una lista de números. Debes retornar una lista
en la que cada número de la lista original sea multiplicado
por dos.
La función multiply_numbers recibirá como entrada una lista 
con números. Finalmente, la función retornará la lista 
transformada.
'''


#forma1
numbers = [1, 2, 3, 4]
numbers_v1= list(map(lambda i:i*2, numbers))
print(numbers_v1)

#forma 2
def multiplica (i):
    return 2*i
numbers_v2=list(map(multiplica,numbers))
print(numbers_v2)

#forma 3

def multiply_numbers(numbers):
    # Escribe tu solución 👇
    result = list(map(lambda number: number * 2, numbers))
    return result

numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)
