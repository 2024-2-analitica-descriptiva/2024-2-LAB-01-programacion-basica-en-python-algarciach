"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    col5 = []
    newlist_col5 = []
    key_list = []
    result = []

    with open('./files/input/data.csv', 'r') as f:
        for line in f:
            line = line.replace('\n', '').strip()
            column = line.split('\t')
            col5.append(column[4].replace(':', ' ').split(','))

    newlist_col5 = [(item.split()[0], int(item.split()[1])) for sublist in col5 for item in sublist]
        
    key_list = sorted(set([key for key, _ in newlist_col5]))  

    for i in key_list:
        tmp = [x for x in newlist_col5 if x[0] == i] 
        result.append((i, min(tmp)[1], max(tmp)[1]))

    return(result)

if __name__ == '__main__':
    print(pregunta_06())