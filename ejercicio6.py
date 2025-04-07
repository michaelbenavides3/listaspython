# Generar una lista de nombres de libros del autor Gabriel García Márquez mínimo 10 obras del autor, al final mostrar el nombre del libro, la cantidad de caracteres del título y remplazar cada letra A con la letra X mayúscula. y mostrar el resultado de las modificaciones de la lista original.

# Lista de libros de Gabriel García Márquez
libros = [
    "Cien años de soledad",
    "El amor en los tiempos del cólera",
    "Crónica de una muerte anunciada",
    "El otoño del patriarca",
    "La hojarasca",
    "El general en su laberinto",
    "Memoria de mis putas tristes",
    "El coronel no tiene quien le escriba",
    "Del amor y otros demonios",
    "Los funerales de la Mamá Grande"
]

# Procesar la lista y mostrar resultados
print("Lista original:")

#este bucle for, recorre cada elementos de la lista libros, 
for libro in libros:
    print(libro)

print("\nLista modificada:")
for libro in libros:
    titulo_modificado = libro.replace("a", "X").replace("A", "X")  # Reemplaza cada 'A' por 'X'
    cantidad_caracteres = len(libro)  # Cuenta los caracteres del título
    print(f"Libro: {titulo_modificado} | Cantidad de caracteres: {cantidad_caracteres}")
