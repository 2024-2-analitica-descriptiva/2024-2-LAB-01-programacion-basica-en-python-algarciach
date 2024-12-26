"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    from collections import Counter

    list_col1 = []

    with open("./files/input/data.csv", "r") as f:
        for line in f:
            line = line.replace('\n', '').strip()
            column = line.split('\t')
            list_col1.append(column[0])

    list_col1 = sorted(list(Counter(list_col1).items()))

    return(list_col1)

if __name__ == '__main__':
    print(pregunta_02())