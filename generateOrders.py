import sys
import random

"""
Orden ejemplo: {idOrder:22, time:2145, x:43, y:-23, idDelivery:4}
Consideramos el rango tanto para las cordenadas x como y entre -50 y 50
"""

""" 
Módulo que contiene la función de generar pedidos (esta funcion es un ejemplo)
"""
ordersList = []

# Genera una lista de diccionarios que contiene las ordenes


def generateOrders(openTime, closeTime, maxOrders):
    time = random.sample(range(openTime, closeTime), maxOrders)
    for o in range(maxOrders):
        idOrder = o
        x = random.randint(-50, 50)
        y = random.randint(-50, 50)
        if (x < 0 and y < 0):
            idDelivery = 0
        else:
            if (x < 0 and y > 0):
                idDelivery = 1
            else:
                if (x > 0 and y > 0):
                    idDelivery = 2
                else:
                    idDelivery = 3
        order = {'idOrder': idOrder, 'time': time[o],
                 'x': x, 'y': y, 'idDelivery': idDelivery}
        ordersList.append(order)
    # Ordena la lista de ordenes
    sortedList = sorted(ordersList, key=lambda i: i['time'])
    return sortedList


sys.modules[__name__] = generateOrders
