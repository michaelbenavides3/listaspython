# Crear una lista de palabras ingresadas por teclado, e identificar si alguna de ellas es palíndroma o no, al final arrojar cuantas, y cuales palabras son palíndromas, y mostrar la lista original.

print("bienvenido al programa")

#crear lista para que el usuario ingrese la palabrra

palabras = []

#definir cantidad de palabras para ingresar

cantidad = int(input("cuantas palabra quiere ingresar ?:  "))

#recibir las palabras

for _ in range (cantidad):
    palabra = input ("ingresar la palabra: ").strip().lower() #convertir a minisculas y eliminar espacios
    palabras.append(palabra) # compresion de lista para verificar palindormas

#identificar palabras palindromas

palindromas =[p for p in palabras if p == p[::-1]]

#mostrar resultado

print("\n lista original", palabras)
print(f"\n total de palabras palindormas: {len(palindromas)}")
print("palabras palindromas: ", palindromas)