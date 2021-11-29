import random

# Nuestros módulos
import generateOrders


# order = {'idOrder': 22, 'time': 2145, 'x': 43, 'y': -23, 'idDelivery': 4}

# Fijo la semilla del generador random para que las corridas sean reproducibles
# durante la depuracion
random.seed(10)

# GLOBAL VARS
openTime = 0
closeTime = 180
endOfDeliveryTime = closeTime + 30 # Tiempo de margen para que termine el reparto
maxOrders = 15
maxOrdersPerDeliver = 3

# ====================================
# Variables y módulos de Órdenes (Gonza y Boris)
# ====================================
orderList = generateOrders(openTime, closeTime, maxOrders)
preparationList = []
readyToDeliverList = []
# ====================================


# ====================================
# TODO: (Prof) Variables y módulos de repartidores
# ====================================
repartidoresList = [{'id': 0, 'available': False, 'returnTime': 0}, {'id': 1, 'available': False, 'returnTime': 0}]
repartidoresOrdersList = {
  0: [],
  1: [],
}



# ====================================
# TODO: (Guille y María) Variables y módulos de repartidores
# ====================================
deliveredOrdersList = []
deliveryVelocity = 6


def Simular(openTime, closeTime):
    
    # Recorre el tiempo
    for t in range(openTime, closeTime):
    	
        # ===================================
    	#  ¿En el t actual, hay algún repartidor que complete su recorrido? (Daniel)
    	# ===================================
        for repartidorIndex in range(len(repartidoresList)):
            # Si el horario de vuelta coincide con el tiempo actual
            if repartidoresList[repartidorIndex]['returnTime'] == t:
            	print("El repartidor: ", repartidoresList[repartidorIndex]['id'], "volvió a la base y se encuentra disponible")
            	repartidoresList[repartidorIndex]['available'] = True
    	
        # ===================================
        # Recorre la lista de ordenes que entraron
        # ===================================
        for o in range(len(orderList)):
            preparationTime = random.randint(10, 30)
            # Si el horario coincide con la hora de la orden
            if orderList[o]['time'] == t:
                ## TIEMPO
                #print("=======  Tiempo: ",t, "=======")
                #print(orderList[o])
                ##
                # Crea un nuevo item en la orden que presenta el tiempo que estará listo el pedido
                orderList[o]['preparedTime'] = orderList[o]['time'] + \
                    preparationTime
                # Traspaso de lista de ordenes generadas o lista de ordenes para preparar
                preparationList.append(orderList[o])
                del orderList[o]
                break
        
        # ===================================
        # Recorre la lista de ordenes que están en preparación para ser trasladados a reparto
        # ===================================
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
        
        # Se ordenan los pedidos listos para repartir según cual termino de prepararse antes
        sorted(readyToDeliverList, key=lambda i: i['preparedTime'])

        # ===================================
        # TODO: (Prof) Recorrer la cola de repartidores disponibles y asignarle un pedido de los que estén preparados y listos.
        #  -> y hacer el resto de cosas marcadas en el word en verde
        # ===================================
        
        # ===================================
    	#  Recorremos la lista de repartidores y buscamos si hay ordenes para los que ese encuentran activos
        #  estas ordenes se agregan a la lista de ordenes hasta completar la capacidad del repartidor
    	# ===================================
        for repartidorIndex in range(len(repartidoresList)):
            
            # ¿El repartidor se encuentra activo?
            if repartidoresList[repartidorIndex]['available'] == True:
                print("El repartidor: ", repartidoresList[repartidorIndex]['id'], "se encuentra activo:")
                    
                # Recorremos la lista de ordenes para entregar y comprobamos si existe alguno asignado al repartidos actual
                for orderIndex in range(len(readyToDeliverList)):
                
                    # Comprobamos que el repartidor actual no se encuentre con la capacidad completa de ordenes
                    if len(repartidoresOrdersList[repartidoresList[repartidorIndex]['id']]) < maxOrdersPerDeliver:
                        
                        if readyToDeliverList[orderIndex]['idDelivery'] == repartidoresList[repartidorIndex]['id']:
                            print(readyToDeliverList[orderIndex])
                            
                            # Traspaso de lista de ordenes en preparacion a lista de ordenes listas para enviar
                            repartidoresOrdersList[repartidoresList[repartidorIndex]['id']].append(readyToDeliverList[orderIndex])
                            del readyToDeliverList[orderIndex]
                            breakpoint()
            	

        # ===================================
        # TODO: (Guille y María) Recorrer el diccionario de repartidores que tienen al menos un pedido para llevar y generar recorrido
        # -> funciones sugeridas
        #        getRoute(pedidosRepartidor) # retorna la ruta
        # -> y hacer el resto de cosas marcadas en el word en cyan
    	#            campos a agregar para marcar los pedidos: travelStartTime y arrivalTime
        # ===================================

    # ===================================
    # Acá se retornarán resultados una vez termine el tiempo:
    # ===================================    
    print(deliveredOrdersList)
    # FIN

# EJECUTAMOS LA SIMULACION
# DEJAMOS UN MARGEN DE TIEMPO PARA QUE REPARTA LOS ÚLTIMOS PEDIDOS EN BASE A LOS RETRASOS POR PREPARACIÓN.
Simular(openTime, endOfDeliveryTime)
