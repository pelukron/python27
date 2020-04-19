import matplotlib.pyplot as plt
import numpy as np

# StringIO behaves like a file object
from io import StringIO

data_str = u"""\
10, 11, 12, 13, 14, 15, 16, 17, 18, 19
20, 21, 22, 23, 24, 25, 26, 27, 28, 29
30, 31, 32, 33, 34, 35, 36, 37, 38, 39
40, 41, 42, 43, 44, 45, 46, 47, 48, 49
50, 51, 52, 53, 54, 55, 56, 57, 58, 59
60, 61, 62, 63, 64, 65, 66, 67, 68, 69
70, 71, 72, 73, 74, 75, 76, 77, 78, 79"""

# create a file object from string
data_file = StringIO(data_str)


def getFilePath():
    # se tiene que usar la ruta absoluta para poder acceder al archivo

    pathFile = "C:\\Users\\diego-moreno\\Documents\\Python\\3\\ejemplo2.csv"
    return open(pathFile, "r")


# se puede comentar esta linea para ver ejemplo con el string creado previamente
# data_file = getFilePath()

x, y = np.loadtxt(data_file, delimiter=',', usecols=(0, 1), unpack=True)

plt.plot(x, y, 'o--', label='Datos interesantes!')
plt.plot(x, y, 'o', label='Datos interesantes!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafica interesante\ncon dos picos')
plt.legend()
# plt.savefig('picos.pdf') # si queremos guardar la grafica como un archivo PDF
# plt.savefig('picos.png') # si queremos guardar la grafica como un archivo de imagen

plt.show()
