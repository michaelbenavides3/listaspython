# Almacenar una lista de números, identificar la longitud de la lista si es par: Los elementos invertir los elementos de la lista. Imprimir la lista original y lista invertida.

def invertir_lista_si_par_simple(lista_original):
    """
    Invierte una lista si su longitud es par, de forma simple.
    """
    if len(lista_original) % 2 == 0:
        print("Lista original:", lista_original)
        print("Lista invertida:", lista_original[::-1]) #Se invierte la lista directamente.
    else:
        print("La lista tiene longitud impar, no se invierte ni se imprime")

# Ejemplos de uso
mi_lista = [1, 2, 3, 4, 5, 6]
invertir_lista_si_par_simple(mi_lista)

mi_lista_impar = [1,2,3,4,5]
invertir_lista_si_par_simple(mi_lista_impar)

