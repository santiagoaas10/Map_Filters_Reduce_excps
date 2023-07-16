'''
En este desafío, se te presenta una lista de objetos que representan órdenes de compra con los siguientes atributos:

customer_name: string
total: number
delivered: boolean
Tu reto es utilizar el concepto de módulos de Python para retornar la suma total de todas las órdenes de compra.
Para resolver el ejercicio, debes trabajar en el archivo main.py, donde se encuentra la función get_total. Esta 
función recibe como parámetro la lista de órdenes de compra.

Debes retornar la suma total de todas las órdenes haciendo 
uso de las funciones definidas en el archivo my_functions.py.my_functions.py.
'''
def get_total(orders):
    preciototal=0
    listaasumar=[]
    for i in orders:
        precios=i["total"]
        listaasumar.append(precios)
        preciototal=preciototal+i["total"]
    return preciototal


