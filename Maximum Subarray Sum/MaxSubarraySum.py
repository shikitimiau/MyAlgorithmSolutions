"""
This file solves the Maximum Subarray Sum problem in linear complexity.

Given a list of integers (positive and negative) we must find the interval with the largest weight in the list.

:author: Shikitimiau
:date: 14-08-2023
"""
from typing import List

def printList(lista: List[int]):
    print("[", end="")
    for i in range(len(lista)):
        if i != 0:  # No imprimir coma antes del primer elemento
            print(",", end=" ")
        print(str(lista[i]), end="")
    print("]")


def maxsubarraysum(lista: List[int]):
    result = ([0],0)
    longitudLista = len(lista)
    listaDePesos = [0] * (longitudLista + 1)
    listaDePesoMinimo = [0] * (longitudLista + 1)
    indexInicioPesoMinimo = 0
    for i in range(longitudLista):
        listaDePesos[i+1] = lista[i] + listaDePesos[i]
        if listaDePesos[i+1] < listaDePesoMinimo[i]:
            listaDePesoMinimo[i+1] = listaDePesos[i+1]
            indexInicioPesoMinimo = i+1
        else:
            listaDePesoMinimo[i+1] = listaDePesoMinimo[i]
        pesoMaxAux = listaDePesos[i+1] - listaDePesoMinimo[i]
        if(pesoMaxAux >= result[1]):
            result = (lista[indexInicioPesoMinimo:i + 1], pesoMaxAux)
    printList(listaDePesos)
    printList(listaDePesoMinimo)
    return result
    

# -------------------------- PRUEBAS --------------------------

lista = [5,10,(-20), 12, 17, (-10), 5, (-12), 13, (-5), 20]
# Peso = 40 Intervalo = [12, 17, (-10), 5, (-12), 13, (-5), 20]

# lista = [5, 10, (-20), 12, 30, (-10), 5, (-12), 12, (-5), 4]
# Peso  = 42 Intervalo = [12,30]

# lista = [4, 3, (-10), 3, (-1), 2, 0, (-3), 5, 7, (-4), (-8), (-10), 4, 7, (-30), (-2), (-6), 4, 7]
# Peso = 13 Intervalo = [3, (-1), 2, 0, (-3), 5, 7]

# lista = [5, 5, 5, (-10), (-10), (-10), 7, 7, 7]
# Peso = 21 Intervalo = [7, 7, 7]

resultado = maxsubarraysum(lista)
print("El intervalo con mayor peso de la lista:")
printList(lista)
print("fue el siguiente con un peso de " + str(resultado[1]))
printList(resultado[0])

# -------------------------- EXPLICACIÓN ALGORITMO --------------------------
"""
    Para este Algoritmo usamos dos listas auxiliares. La primera "listaDePesos" 
    nos ayudará a calcular el peso de un intervalo de forma constante.
    Y la lista de "listaDePesoMinimo" nos servirá para llevar un registro del peso
    más pequeño registrado conforme vamos recorriendo la lista y calculando sus pesos
    en "listaDePesos".

                                    POR EJEMPLO
    Tendremos la lista: [5,10,-20, 12, 17, -10, 5, -12, 13, -5, 20]
    La listaDePesos que se genera al final es esta: [0, 5, 15, -5, 7, 24, 14, 19, 7, 20, 15, 35]
    Entonces, si quisieramos saber el peso de un intervalo, digamos el intervalo (i,j).
    Hacemos la siguiente operación sobre la listaDePesos:
        listaDePesos[j-1] - listaDePesos[i]
    Si lo vemos gráficamente sería esto:  

                     i                             j
        [5, 10,-20, 12, 17, -10,  5, -12, 13, -5, 20] -- Lista original
    [0, 5, 15, -5,   7, 24,  14, 19,   7, 20, 15, 35] -- Lista de pesos
    listaDePesos[j] - listaDePesos[i-1] = 35 - (-5) = 40 <- Peso del intervalo (i,j)

    Notemos que la Lista de Pesos inicia en 0 para el caso donde el intervalo considere el primer
    elemento de la lista, es decir, tengamos el intervalo (0,j).


    Ahora, lo anterior nos permite saber los pesos de los intervalos de forma lineal,
    pero igual querríamos obtener el intervalo con mayor peso de forma lineal o bien,
    a la vez que hacemos el calculo anterior.
    Para eso 'imaginamos' una lista auxiliar más que será la listaDePesoMinimo, donde
    iríamos guardando el peso más pequeño visto en la lista de pesos, y así sabríamos
    en que punto inicia el intervalo de mayor peso.

                                    POR EJEMPLO
                     i                             j
        [5, 10,-20, 12, 17, -10,  5, -12, 13, -5, 20] -- Lista original
    [0, 5, 15, -5,   7, 24,  14, 19,   7, 20, 15, 35] -- Lista de pesos
    [0, 0,  0, -5,  -5, -5,  -5, -5,  -5, -5, -5, -5] -- Lista de peso mínimo
                x

    listaDePesos[j] - listaDePesos[i-1] = 35 - (-5) = 40 <- Peso del intervalo (i,j)

    listaDePesoMinimo[x] <- Aquí es donde apareció por primera vez el peso más pequeño
    registrado en la lista.
    
    ¿De que nos sirve esta nueva lista y saber donde empezó a aparecer el peso más pequeño?
    Recordemos que el peso se calculaba con esto: listaDePesos[j] - listaDePesos[i-1].
    Si fueramos recorriendo nuestra lista original, tendríamos un 'j' indice que nos ayudaría a movernos a través de los elementos de la lista, y para cada uno ir reflejando su peso en Lista de Pesos, así, mediante este recorrido y este calculo ya podríamos saber cual es el peso máximo. ¿Pero como sabemos a partir de que elemento se conforma el intervalo que tiene ese peso? ya sabemos el final, que es el que está en la posición j, ¿pero el que está en la posición (i-1)?
    Pues fijandonos en que momento obtuvimos antes el peso más pequeño.
    ¿Por qué el mas pequeño? Por que es allí donde podemos obtener la mayor distancia entre nuestro peso más grande encontrado y el más pequeño encontrado, así, ya encontramos el intervalo asociado a ese peso máximo encontrado hasta ese momento.

"""
