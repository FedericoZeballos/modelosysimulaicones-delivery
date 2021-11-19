import sys

""" 
Módulo que contiene la función de generar pedidos (esta funcion es un ejemplo)
 """

def generatePedidos(x):
    return [x]

sys.modules[__name__] = generatePedidos
