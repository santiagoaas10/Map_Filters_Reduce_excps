'''
sets
'''

numbers=[1,2,4,5,6,81,25,3]
print(numbers)
set_numbers=set(numbers)

print(set_numbers)
unique_numbers_in_list=list(set_numbers)
print(unique_numbers_in_list)




'''
list comprehension
'''
numbers=[]
for i in range(1,11):
    if i %2 ==0:
        numbers.append(i*2)
print(numbers)

numbers_v2=[i*2 for i in range(1,11) if i%2==0]
print(numbers_v2)

'''
dictionary comprehension
'''
import random
dict = {}
for i in range(1,11):
    dict[i]=i*2
print(dict)


dict_v2 = { i: i*2 for i in range(1,11) }
print(dict_v2)

countries= ['col','mex','bol','pe']
population ={}
for country in countries:
    population[country] = random.randint(1,100)
print(population)

population_v2 = {country: random.randint(1,100) for country in countries}
print(population_v2)

'''

'''
names=['nico','zule','santi']
ages = [12,56,98]

mydictionari={
    'nico':12,
    'zule':56,
    'santi':98
}

print(mydictionari)
print(list(zip(names,ages))) #unimos 2 listas
print(zip(names,ages))

newdic= {name: age for(name,age) in zip(names,ages)}
print(newdic)

newdic2 = {names[i]:ages[i] for i in range(len(names))}
print(newdic2)

#new_dict3= dict(zip(names,ages))

population_v2 = {country: random.randint(1,100) for country in countries}
print(population_v2)

#queremos generar diccionario con paises cuya población sea mayor o igual a 10

result = {country: population for (country,population) in population_v2.items() if population>50}
print (result)

text="hola, soy santi"
unique ={c:c.upper() for c in text if c in 'aeiou'}
print(unique)


numbers = [35, 16, 10, 34, 37, 25]

even_numbers = []
for number in numbers:
  if number % 2 == 0:
    even_numbers.append(number)
print('v1 =>', even_numbers)

even_numbersv2= [i for i in numbers if i%2==0]



