import matplotlib.pyplot as plt

# https: // matplotlib.org/api/pyplot_api.html
tiempo = [0, 1, 2, 3]
posicion = [0, 100, 200, 300]
plt.plot(tiempo, posicion)
plt.xlabel('Tiempo (h)')
plt.ylabel('Posicion (km)')
plt.show()
