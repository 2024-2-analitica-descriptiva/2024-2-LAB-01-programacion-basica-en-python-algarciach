"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    result = {}

    with open('./files/input/data.csv', 'r') as f:
        for line in f:
            line = line.replace('\n', '').strip()
            column = line.split('\t')

            keys = column[3].split(',')
            values = column[1]

            total = sum(int(item) for item in values)

            for key in keys:
                if key in result:
                    result[key] += total
                else:
                    result[key] = total

    result = dict(sorted(result.items()))

    return(result)
        
if __name__ == '__main__':
    print(pregunta_11())