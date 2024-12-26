"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    col1 = []
    list_col1_col2 = []
    result = []

    with open('./files/input/data.csv', 'r') as f:
        for line in f:
            line = line.replace('\n', '').strip()
            column = line.split('\t')
            list_col1_col2.append((column[0], int(column[1])))

    col1 = sorted(set([key for key, _ in list_col1_col2]))  

    for i in col1:
        tmp = [x for x in list_col1_col2 if x[0] == i]
        total = sum(x[1] for x in tmp)
        result.append((i, total))

    return(result)

if __name__ == '__main__':
    print(pregunta_03())