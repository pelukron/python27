
# se usa una funcion para poder llamar multiples veces


def getFilePath():
    # se tiene que usar la ruta absoluta para poder acceder al archivo

    pathFile = "C:\\Users\\diego-moreno\\Documents\\Python\\3\\archivo.txt"
    return open(pathFile, "r")


file = getFilePath()

# read es el objeto es el metodo que saca el texto completo, tambien se puede especificar el tamano de las caracteres
print(file.read())

file.close()

fileAsFile = getFilePath()

# se puede imprimir linea por linia
print('\nSe imprimi por separado!!!\n')
for f in fileAsFile:
    print(f)
fileAsFile.close()
