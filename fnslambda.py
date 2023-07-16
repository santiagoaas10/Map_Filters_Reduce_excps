def increment(x):
  return x + 1
#es la misma fnc de arriba ssolo que de tipo lambda que es entradas1, entrada2....entradan:salida1,salida2, ...salidan
increment_v2 = lambda x: x +1

def high_ord_func(x, func):
  return x + func(x)

high_ord_func_v2 = lambda x, func: x + func(x) #fnc lambda, mando a : x y a la func y me retorna: x+f(x) 

result = high_ord_func(2, increment)
# 2 + (2 + 1)
print(result)

result = high_ord_func_v2(2, increment_v2)
print(result)
result = high_ord_func_v2(2, lambda x: x + 2)
print(result)
## change
result = high_ord_func_v2(2, lambda x: x * 5)
print(result)