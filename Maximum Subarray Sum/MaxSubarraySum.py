"""
This file solves the Maximum Subarray Sum problem in linear complexity.

Given a list of integers (positive and negative) we must find the interval with the largest weight in the list.

:author: Shikitimiau
:date: 14-08-2023
"""
from typing import List

def printList(lista: List[int]):
    print("(", end="")
    for i in range(len(lista)):
        if i != 0:  # No imprimir coma antes del primer elemento
            print(",", end=" ")
        print(str(lista[i]), end="")
    print(")")


def maxsubarraysum(lista: List[int]):
    result = ([0],0)
    longitudLista = len(lista)
    listaDePesos = [0] * (longitudLista + 1)
    listaDePesoMinimo = [0] * (longitudLista + 1)
    
    for i in range(longitudLista):
        listaDePesos[i+1] = lista[i] + listaDePesos[i]
        if listaDePesos[i+1] < listaDePesoMinimo[i]:
            listaDePesoMinimo[i+1] = listaDePesos[i+1]
        else:
            listaDePesoMinimo[i+1] = listaDePesoMinimo[i]

    for i in range(longitudLista):
        pesoMaxAux = listaDePesos[i+1] - listaDePesoMinimo[i]
        if(pesoMaxAux >= result[1]):
            for j in range(i+1):
                if listaDePesoMinimo[j] == listaDePesoMinimo[i]:
                    result = (lista[j:i + 1], pesoMaxAux)
                    break
    return result
    

# -------------------------- PRUEBAS --------------------------

#lista = [5,10,(-20), 12, 17, (-10), 5, (-12), 13, (-5), 20]
# Peso = 40 Intervalo = [12, 17, (-10), 5, (-12), 13, (-5), 20]

# lista = [5, 10, (-20), 12, 30, (-10), 5, (-12), 12, (-5), 4]
# Peso  = 42 Intervalo = [12,30]

# lista = [4, 3, (-10), 3, (-1), 2, 0, (-3), 5, 7, (-4), (-8), (-10), 4, 7, (-30), (-2), (-6), 4, 7]
# Peso = 13 Intervalo = [3, (-1), 2, 0, (-3), 5, 7]

lista = [5, 5, 5, (-10), (-10), (-10), 7, 7, 7]
# Peso = 21 Intervalo = [7, 7, 7]

resultado = maxsubarraysum(lista)
print("El intervalo con mayor peso de la lista:")
printList(lista)
print("fue el siguiente con un peso de " + str(resultado[1]))
printList(resultado[0])
