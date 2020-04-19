import matplotlib.pyplot as plt
import csv


def getFilePath():
    # se tiene que usar la ruta absoluta para poder acceder al archivo

    pathFile = "C:\\Users\\diego-moreno\\Documents\\Python\\3\\ejemplo.csv"
    return open(pathFile, "r")


file = getFilePath()
x = []
y = []
with file as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))

plt.plot(x, y, label='Datos interesantes!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafica interesante\ncon dos picos')
plt.legend()
plt.show()
