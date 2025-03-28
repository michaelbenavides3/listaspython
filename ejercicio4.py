#generar dos listas de longitudes n y m, la primera lista ordenarla de manera ascendente y la segunda de manera descendente.

"""import random

#pedir al usuario las longitudes de las listas
n = int(input("Ingrese la longitud de la primera lista: "))
m = int(input("Ingrese la longitud de la segunda lista: "))

#generar las listas con valores aleatorios

lista1 = []
lista2 = []"""

n = int(input("Ingrese la longitud de la primera lista: "))
m = int(input("Ingrese la longitud de la segunda lista: "))

#generar las listas con valores aleatorios

lista1 = []
lista2 = []

for i in range(n):
    lista1.append(i+1)
    
for i in range(m, 0, -1):
    lista2.append(i)
    
#imprimir las listas

print("Lista 1: (ascendete)", lista1)
print("Lista 2: (descendente)", lista2)
