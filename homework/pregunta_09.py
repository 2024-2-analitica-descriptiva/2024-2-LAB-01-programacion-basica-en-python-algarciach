"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    from collections import Counter

    col5 = []
    newlist_col5 = []
    key_list = []
    result = {}

    with open('./files/input/data.csv', 'r') as f:
        for line in f:
            line = line.replace('\n', '').strip()
            column = line.split('\t')
            col5.append(column[4].replace(':', ' ').split(','))

    newlist_col5 = [(item.split()[0], int(item.split()[1])) for sublist in col5 for item in sublist]

    result = dict(sorted(list(Counter([key for key, _ in newlist_col5]).items())))

    return(result)

if __name__ == '__main__':
    print(pregunta_09())