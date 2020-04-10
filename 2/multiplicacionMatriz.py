
matriz = [[1, -1], [2, 6]]
exponente = 2


# https://stackoverflow.com/a/22870906
def esMatrizNxN(matriz):
    esCuadrada = False
    filas = len(matriz)
    for fila in matriz:
        if len(fila) == filas:
            esCuadrada = True

    # Regresa 2 valodes, si es NxN la matriz y el numero de filas a iterar
    return [esCuadrada, filas]


# Multiplicacion de matrix 2x2
def elevarEjemplo(matriz, exponente=10):

    esCuadrada, numeroFilas = esMatrizNxN(matriz)
    mensaje = "Se necesita ser cuadrada la matriz"
    if(esCuadrada):

        # contruccion de la matris que regresara para poder iterarla
        C = [[0 for row in range(numeroFilas)] for col in range(numeroFilas)]
        print C

        for i in range(numeroFilas):
            for j in range(numeroFilas):
                for k in range(numeroFilas):
                    # Validar si llego al ultimo elemento del arreglo para poder multiplicar por el anterior
                    if (k+1 == numeroFilas):
                        C[i][j] = (matriz[i][k-1] * matriz[k-1][j]) + \
                            (matriz[i][k] * matriz[k][j])
                    else:
                        C[i][j] = (matriz[i][k] * matriz[k][j]) + \
                            (matriz[i][k+1] * matriz[k+1][j])
        print C
        return "final"
    else:
        return mensaje


print elevarEjemplo(matriz, 3)
