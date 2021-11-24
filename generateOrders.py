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
maxOrders = 15  # Cantidad de pedidos durante el día
openTime = 0
closeTime = 180

# Genera una lista de diccionarios que contiene las ordenes


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

# Ordena la lista de ordenes
sortedList = sorted(ordersList, key=lambda i: i['time'])


def OrdersStateMachine(openTime, closeTime):
    # Recursiona sobre el horario de funcion del delivery
    for t in range(openTime, closeTime):
        ##
        print(t)
        ##
        # Recursiona sobre la lista de ordenes ordenadas
        for o in range(len(sortedList)):
            preparationTime = random.randint(10, 30)
            # Si el horario coincide con la hora de la orden
            if sortedList[o]['time'] == t:
                ##
                print(sortedList[o])
                ##
                # Crea un nuevo item en la horden que presenta el tiempo que estará listo el pedido
                sortedList[o]['preparedTime'] = sortedList[o]['time'] + \
                    preparationTime
                # Traspaso de lista de ordenes generadas o lista de ordenes para preparar
                preparationList.append(sortedList[o])
                del sortedList[o]
                break
        # Recursiona sobre la lista de pedidos en preparación
        for p in range(len(preparationList)):
            # Si el horario coincide con la hora de preparado de la orden
            if preparationList[p]['preparedTime'] == t:
                ##
                print(preparationList[p])
                ##
                # Traspaso de lista de ordenes en preparacion a lista de ordenes listas para enviar
                readyToDeliverList.append(preparationList[p])
                del preparationList[p]
                break
        sorted(readyToDeliverList, key=lambda i: i['preparedTime'])

    print(readyToDeliverList)


OrdersStateMachine(openTime, closeTime)

sys.modules[__name__] = generateOrders
