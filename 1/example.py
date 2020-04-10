
# Ejemplo 1
print "Ejemplo 1"
quesos = ['Cheddar', 'Edam', 'Gouda']  # definicion de una lista
print(quesos)  # impresion de la lista

###############

# Ejemplo 2
print "Ejemplo 2"
quesoManchego = 'Manchego'
# buscar un elemento en la lista con 'in'
existeElQueso = quesoManchego in quesos
print(existeElQueso)

###########

# Ejemplo 3.1, impresiond e una lista
print "Ejemplo 3.1"
for queso in quesos:
    print(queso)

# Ejemplo 3.2, modificar los elementos del arreglo mutiplicandolos por el indice de la lista
# es necesario usar len para obtener el tamagno de la lista
# range para decirle el limitante de nuetra lista y asi poder mutarla con un indice
# https://www.codecademy.com/forum_questions/54f231c876b8fe4269002f2f
print "Ejemplo 3.2"
numeros = [1, 2, 3]
for i in range(len(numeros)):
    numeros[i] *= numeros[i]
    print(numeros[i])

print "lista numero con valores mutados", numeros
#print numeros

#############

# Ejemplo 4 concatenacion de listas
print "Ejemplo 4"
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print "contatenacion de listas dos listas en una tercer", c
#print c

##########

# Ejemplo 5 suma de 2 listas/vectores
print "Ejemplo 5"
d = []

for i in a:  # iteracion de la primera lista
    for j in b:  # iteracion de la segunda lista
        # sumar de los vectores
        sumaVectores = i + j
        d.append(sumaVectores)
        # validar elementos repetidos
        # if sumaVectores in d:
        #    print "Elemento repetido ", sumaVectores
        # else:
        # agregar la suma de los elementos a la lista con append
        #   d.append(sumaVectores)
print d


###############
e = []
tamagnoVector = range(len(a)) == range(len(b))
if(tamagnoVector):
    tamagnoVector = range(len(a))

for i in tamagnoVector:
    sumaVectores = a[i] + b[i]
    e.append(sumaVectores)

print e
