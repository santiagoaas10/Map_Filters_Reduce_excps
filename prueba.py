import functools
orders= [
  {
    "customer_name": "Nicolas",
    "total": 100,
    "delivered": True,
  },
  {
    "customer_name": "Zulema",
    "total": 120,
    "delivered": False,
  },
  {
    "customer_name": "Santiago",
    "total": 20,
    "delivered": False,
  }
]
preciototal=0
listaasumar=[]
for i in orders:
    precios=print(i["total"])
    listaasumar.append(precios)
    preciototal=preciototal+i["total"]

print(preciototal)



