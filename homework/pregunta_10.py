"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    list_cols_145 = []
    result = []

    with open('./files/input/data.csv', 'r') as f:
        for line in f:
            line = line.replace('\n', '').strip()
            column = line.split('\t')
            list_cols_145.append((column[0], column[3].split(','), column[4].split(',')))

    result = [(x[0], len(x[1]), len(x[2])) for x in list_cols_145]

    return(result)





if __name__ == '__main__':
    print(pregunta_10())