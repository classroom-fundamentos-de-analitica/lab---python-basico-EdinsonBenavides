"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    File = open("data.csv", "r").readlines()
    File = [z.replace("\n", "") for z in File]
    File = [z.split() for z in File]
    Col_2 = [int(z[1]) for z in File]
    Sum_c2 = sum(Col_2)
       
    return Sum_c2
    


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    File = open("data.csv", "r").readlines()
    File = [z.replace("\n", "") for z in File]
    File = [z.split() for z in File]
    Letter = [i[0] for i in File]
    Letter = list(set(Letter))
    Letter.sort()

    Col_1 = [z[0] for z in File]
    val = [Col_1.count(z) for z in Letter]
    tuppla = list(zip(Letter, val))
    
    return tuppla


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    File = open("data.csv", "r").readlines()
    File = [z.replace("\n", "") for z in File]
    File = [z.split() for z in File]
    Letter = [i[0] for i in File]
    Letter = list(set(Letter))
    Letter.sort()
    Total = []
    
    col12 = [(z[0], z[1]) for z in File]
    for j in Letter:
        suma =0
        for i in range(len(col12)):
            if col12[i][0] == j:
                suma += int(col12[i][1]) 
        elemento = (j, suma)
        Total.append(elemento)
    return Total


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    File = open("data.csv", "r").readlines()
    File = [z.replace("\n", "") for z in File]
    File = [z.split() for z in File]
    fecha = [z[2] for z in File]
    Month = [fecha[z][5:7] for z in range(len(fecha))]
    Month = list(set(Month))
    Month.sort()

    Total_M=[fecha[z][5:7] for z in range(len(fecha))]

    val=[Total_M.count(z) for z in Month]

    registros= list(zip(Month, val))
    
    return registros


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """

    File = open("data.csv", "r").readlines()
    File = [z.replace("\n", "") for z in File]
    File = [z.split() for z in File]
    Letter = [i[0] for i in File]
    Letter = list(set(Letter))
    Letter.sort()

    minimo = []
    maximo =[]
    col12 = [(z[0], z[1]) for z in File]
    
    for i in Letter:
        total=[]
        for j in range(len(col12)):
            if col12[j][0] == i:
                val= col12[j][1]
                total.append((val))
        minimo.append(int(min(total)))
        maximo.append(int(max(total)))
    Total = list(zip(Letter, maximo, minimo))
    
    return Total


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    File = open("data.csv", "r").readlines()
    File = [z.replace("\n", "") for z in File]
    File = [z.split() for z in File]
    clave = [z[4] for z in File]
    listase = [clave[z].split(",") for z in range(len(clave))]
    listafin=[[listase[i][j].split(":") for j in range(len(listase[i]))] for i in range(len(listase))]
    claves = list(set([z[0:3] for z in clave]))
    claves.sort()

    a =listafin[:][0]
    for i in range(1,len(listafin)):
        b =listafin[:][i]
        a.extend(b)
    
    
    minimo = []
    maximo =[]
    
    for i in range(len(claves)):
        total=[]
        for j in range(len(a)):
            if a[j][0] == claves[i]:
                val= a[j][1]
                total.append((int(val)))
        minimo.append(min(total))
        maximo.append(max(total))
    total = list(zip(claves, minimo, maximo))
    
    return total


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    
    File = open("data.csv", "r").readlines()
    File = [z.replace("\n", "") for z in File]
    File = [z.split() for z in File]
    col2= [(int(z[1]), z[0]) for z in File]
    num = list(set([int(z[1]) for z in File]))
    num.sort()

    letraf =[]
    for i in num:
        letra= [col2[j][1] for j in range(len(col2)) if i == col2[j][0]]
        letraf.append(letra)

    Total = list(zip(num, letraf))   

    return Total


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    File = open("data.csv", "r").readlines()
    File = [z.replace("\n", "") for z in File]
    File = [z.split() for z in File]
    col2= [(int(z[1]), z[0]) for z in File]
    num = list(set([int(z[1]) for z in File]))
    num.sort()

    letraf =[]
    for i in num:
        letra= [col2[j][1] for j in range(len(col2)) if i == col2[j][0]]
        a=list(set(letra))
        a.sort()
        letraf.append(a)

    Total = list(zip(num, letraf))
    return Total


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    File = open("data.csv", "r").readlines()
    File = [z.replace("\n", "") for z in File]
    File = [z.split() for z in File]
    clave = [z[4] for z in File]
    listase = [clave[z].split(",") for z in range(len(clave))]
    listafin=[[listase[i][j].split(":") for j in range(len(listase[i]))] for i in range(len(listase))]
   
    a =listafin[:][0]
    for i in range(1,len(listafin)):
        b =listafin[:][i]
        a.extend(b)
    
    claves_all=[a[i][0] for i in range(len(a))]
    cl=list(set([a[i][0] for i in range(len(a))]))

    val=[claves_all.count(z) for z in cl]

    claves={}
    for i in range(len(val)):
        n=dict({cl[i]:val[i]})
        claves.update(n)

    claves =dict(sorted(claves.items())) 
    
    return claves


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    File = open("data.csv", "r").readlines()
    File = [z.replace("\n", "") for z in File]
    File = [z.split() for z in File]
    Col_1= [z[0] for z in File] # col1 = [ col1[i][0] for i in range(len(archivo))]
    col3= [len(z[3].split(",")) for z in File]
    col4= [len(z[4].split(",")) for z in File]
    total = [(Col_1[i], col3[i], col4[i]) for i in range(len(Col_1))]
    
    return total

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    File = open("data.csv", "r").readlines()
    File = [z.replace("\n", "") for z in File]
    File = [z.split() for z in File]
    col24= [(z[1], z[3].split(",")) for z in File] 
    
    col4= [z[3].split(",") for z in File]
    a =col4[:][0]
    for i in range(1,len(col4)):
        b =col4[:][i]
        a.extend(b)
    Letters =sorted(list(set(a)))
    zeros = [ 0 for _ in Letters]
    dic = dict(zip(Letters, zeros))
       
    for i in range(len(col24)):
        for j in col24[i][1]:
            for l in Letters: 
                if j == l:
                    dic[l]= dic[l]+int(col24[i][0])
    return dic


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    File = open("data.csv", "r").readlines()
    File = [z.replace("\n", "") for z in File]
    File = [z.split() for z in File]
    Letter = [z[0] for z in File]
    col1 = [z[0] for z in File]
    Letter = list(set(Letter))
    Letter.sort()
    zeros = [ 0 for _ in Letter]
    Dict = dict(zip(Letter, zeros))
    clave = [z[4].replace(":", ",").split(",") for z in File]
    k=0
    for i in clave:
        suma = 0
        for j in i[1::2]:
            suma += int(j)
        for l in Letter:
            if col1[k] == l:
                Dict[l] += int(suma)     
        k += 1    
    return Dict

