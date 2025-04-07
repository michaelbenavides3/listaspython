#calcular la nota máxima y nota mínima de cada estudiante del curso de programación. Recordar que por cada estudiante al almacena 5 notas, las dos primeras son evaluaciones que equivalen al 30% de la nota final, la tercera y cuarta nota es de trabajos y equivale el 10% y la última nota es examen final que equivale al 60%. Al final por cada estudiante se debe mostrar su nombre, sus notas y su nota máxima y mínima. el curso está conformado por un total de 20 aprendices en total y con rango de notas que van de 1 al 10 en su escala.

import random

# Generar datos de 20 estudiantes con nombres ficticios y notas aleatorias
estudiantes = []
for i in range(20):
    nombre = f"Estudiante_{i+1}"
    notas = [random.randint(1, 10) for _ in range(5)]  # Genera cinco notas entre 1 y 10, con random,randint genera numero aleatorios
    estudiantes.append((nombre, notas))  #.append, nos quiere decir que se agregrar a la lista de estdudiantes

# Procesar los datos
for nombre, notas in estudiantes:
    nota_maxima = max(notas) #max devolvera la nota mas alta
    nota_minima = min(notas) #min devolvera la nota mas baja

    # Calcular nota final
    nota_final = (sum(notas[:2]) * 0.30) + (sum(notas[2:4]) * 0.10) + (notas[4] * 0.60)
    #usamos sum[:2]--> para sumar las 2 primera notas, sum[2:4]-->para sumar las 2 siguientes y nota[4]--> para acceder a la utlima nota


    # Mostrar resultados
    print(f"Nombre: {nombre}")
    print(f"Notas: {notas}")
    print(f"Nota Máxima: {nota_maxima}, Nota Mínima: {nota_minima}")
    print(f"Nota Final: {nota_final:.2f}")
    print("-" * 30)
