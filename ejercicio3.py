# Almacenar dos listos de números enteros, lista1 y lista2, y generar la tercera lista con los siguientes criterios: Sumar el primer elemento de la lista1 con el último elemento de la lista2 y guardar el resultado en la lista3, luego el segundo elemento de la lista1 sumarlo con el noveno elemento de la lista2. Al final imprimir las tres listas.

#definir las listas

lista1 = [1, 5, 7, 9, 11, 15, 14, 18, 20, 22, 25]
lista2 = [2, 4, 6, 8, 10, 12, 16, 17, 19, 21, 23]

#definir la lista3

lista3 = []

#recorrer las listas

lista3.append(lista1[0] + lista2[-1])

#for i in range(len(lista1)):
    #lista3.append(lista1[i] + lista2[-i-1])
    #resultado = lista1[i] + lista2[-i -1]
    #lista3.append(resultado)
    
if len(lista2) >= 9:
    lista3.append(lista1[1] + lista2[8])

#imprimir las listas

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista 3:", lista3)