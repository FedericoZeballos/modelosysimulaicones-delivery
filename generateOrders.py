import sys
import random

"""
Orden ejemplo: {idOrder:22, time:2145, x:43, y:-23, idDelivery:4}
Consideramos el rango tanto para las cordenadas x como y entre -50 y 50
"""


""" 
Módulo que contiene la función de generar pedidos (esta funcion es un ejemplo)
"""
order = {'idOrder': 22, 'time': 2145, 'x': 43, 'y': -23, 'idDelivery': 4}
ordersList = []
sortedList = []
preparationlist = []
maxOrders = 50
openTime = 2000
closeTime = 2400
preparationTime = random.randint(10, 30)


def generateOrders(openTime, closeTime):
    for o in range(maxOrders):
        idOrder = o
        time = random.randint(openTime, closeTime)
        x = random.randint(-50, 50)
        y = random.randint(-50, 50)
        if (x < 0):

            idDelivery = 0

        else:
            idDelivery = 1
        order = {'idOrder': idOrder, 'time': time,
                 'x': x, 'y': y, 'idDelivery': idDelivery}
        ordersList.append(order)


generateOrders(2000, 2400)

sortedList = sorted(ordersList, key=lambda i: i['time'])

print(sortedList)


sys.modules[__name__] = generateOrders
