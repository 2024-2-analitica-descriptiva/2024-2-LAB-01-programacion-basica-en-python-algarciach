"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    col1 = []
    list_col1_col2 = []
    result = []

    with open('./files/input/data.csv', 'r') as f:
        for line in f:
            line = line.replace('\n', '').strip()
            column = line.split('\t')
            list_col1_col2.append((column[0], int(column[1])))

    col1 = sorted(set([key for key, _ in list_col1_col2 ]))

    for i in col1:
        tmp = [x for x in list_col1_col2 if x[0] == i]
        result.append((i, max(tmp)[1], min(tmp)[1]))

    return(result)

if __name__ == '__main__':
    print(pregunta_05())