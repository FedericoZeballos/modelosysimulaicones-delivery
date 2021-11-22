import sys
import random

"""
Orden ejemplo: {idOrder:22, time:2145, x:43, y:-23, idDelivery:4}
Consideramos el rango tanto para las cordenadas x como y entre -50 y 50
"""


""" 
Módulo que contiene la función de generar pedidos (esta funcion es un ejemplo)
"""
# order = {'idOrder': 22, 'time': 2145, 'x': 43, 'y': -23, 'idDelivery': 4}
ordersList = []
#sortedList = []
preparationList = []
readyToDeliverList = []
maxOrders = 15
openTime = 0
closeTime = 2100


def generateOrders(openTime, closeTime):
    time = random.sample(range(openTime, closeTime), maxOrders)
    for o in range(maxOrders):
        idOrder = o
        x = random.randint(-50, 50)
        y = random.randint(-50, 50)
        if (x < 0):

            idDelivery = 0

        else:
            idDelivery = 1
        order = {'idOrder': idOrder, 'time': time[o],
                 'x': x, 'y': y, 'idDelivery': idDelivery}
        ordersList.append(order)


generateOrders(openTime, closeTime)

sortedList = sorted(ordersList, key=lambda i: i['time'])


def OrdersStateMachine(openTime, closeTime):
    for t in range(openTime, closeTime):
        # print(t)
        for o in range(len(sortedList)):
            preparationTime = random.randint(10, 30)
            if sortedList[o]['time'] == t:
                sortedList[o]['preparedTime'] = sortedList[o]['time'] + \
                    preparationTime
                preparationList.append(sortedList[o])
                # print(sortedList[o])
                del sortedList[o]
                break
        for p in range(len(preparationList)):
            if preparationList[p]['preparedTime'] == t:
                readyToDeliverList.append(preparationList[p])
                # print(preparationList[p])
                del preparationList[p]
                break
        sorted(readyToDeliverList, key=lambda i: i['preparedTime'])

    print(readyToDeliverList)


OrdersStateMachine(openTime, closeTime)

sys.modules[__name__] = generateOrders
