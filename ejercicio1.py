#Almacenar en una lista 15 números e imprimir cuantos son ceros, negativos, positivos, además imprimir la suma de números positivos y suma de números negativos.

numeros = []
ceros = 0
negativos = []
positivos = []
#suma_positivos = 0
#suma_negativos = 0

for i in range (15):
    numero = float(input(f"ingrese un numero {i+1}: "))
    numeros.append(numero)
    
for numero in numeros:
    if numero == 0:
        ceros += 1
    elif numero < 0:
        negativos.append(numero)
    else:
        positivos.append(numero)
        
print(f"La cantidad de ceros es: {ceros}")
print(f"La cantidad de negativos es: {len(negativos)}")
print(f"La cantidad de positivos es: {len(positivos)}")
print(f"suma de numeros positivos es: {sum(positivos)}")
print(f"suma de numeros negativos es: {sum(negativos)}")