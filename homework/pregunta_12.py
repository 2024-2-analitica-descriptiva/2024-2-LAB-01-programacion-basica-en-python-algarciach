"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    result = {}

    with open("./files/input/data.csv", "r") as f:
        for line in f:
            line = line.replace('\n', '').strip()
            column = line.split('\t')

            key = column[0]
            values = column[4].split(',')

            total = sum(int(item.split(':')[1]) for item in values)

            if key in result:
                result[key] += total
            else:
                result[key] = total

    result = dict(sorted(result.items()))

    return(result)

if __name__ == '__main__':
    print(pregunta_12())