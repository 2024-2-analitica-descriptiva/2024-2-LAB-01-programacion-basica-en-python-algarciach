"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    sum_col2 = 0

    with open("./files/input/data.csv", "r") as f:
        for line in f:
            line = line.replace('\n', '').strip()
            column = line.split('\t')
            sum_col2 += int(column[1])

    return(sum_col2)
    
if __name__ == '__main__':
    print(pregunta_01())

