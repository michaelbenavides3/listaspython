# De las listas trabajadas en el ejercicio #2, ingresar nuevos elementos a estas listas en diferentes posiciones y mostrar al final la nueva lista modificada

def invertir_lista_si_par_simple(lista_original):
    """
    Invierte una lista si su longitud es par, de forma simple.
    """
    if len(lista_original) % 2 == 0:
        print("Lista original:", lista_original)
        print("Lista invertida:", lista_original[::-1])  # Se invierte la lista directamente.
    else:
        print("La lista tiene longitud impar, no se invierte ni se imprime.")

# Lista original
mi_lista = [1, 2, 3, 4, 5, 6]

# Agregar nuevos elementos en diferentes posiciones
mi_lista.append(7)  # Agregar un elemento al final
mi_lista.insert(2, 10)  # Insertar 10 en la posición 2
mi_lista.insert(4, 20)  # Insertar 20 en la posición 4

# Ejecutar la función con la lista modificada
invertir_lista_si_par_simple(mi_lista)

# Lista con cantidad impar de elementos para probar
mi_lista_impar = [1, 2, 3, 4, 5]

# Agregar nuevos elementos también a esta lista
mi_lista_impar.append(9)
mi_lista_impar.insert(3, 15)

# Ejecutar la función con la lista modificada
invertir_lista_si_par_simple(mi_lista_impar)
