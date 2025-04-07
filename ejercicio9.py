# Convertir cada elemento guardado en la lista del ejercicio #6, en mayúsculas y minúsculas, Al final mostrar en pantalla el listado original y luego los dos nuevos listados respectivamente.

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

# Crear nuevas listas para mayúsculas y minúsculas
libros_mayusculas = [libro.upper() for libro in libros]  # Convierte cada título en mayúsculas
libros_minusculas = [libro.lower() for libro in libros]  # Convierte cada título en minúsculas

# Mostrar resultados
print("Lista original:")
for libro in libros:
    print(libro)

print("\nLista en MAYÚSCULAS:")
for libro in libros_mayusculas:
    print(libro)

print("\nLista en minúsculas:")
for libro in libros_minusculas:
    print(libro)
