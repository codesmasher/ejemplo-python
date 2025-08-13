# Elementos iterables
# Objeto lista
animales = ["gato", "perro", "loro", "cocodrilo"]
numeros = [34, 56, 23, 10]

# Bucle for sencillo
for animal in animales:
    print(animal)

# Bucle for doble (solo es posible si las dos listas tienen la misma cantidad de elementos)
for animal, numero in zip(animales, numeros):
    print(animal)
    print(numero * 11)

# Iterar desde un rango (de 10 a 19)
for index in range(10, 20):
    print(index)

# Forma no optima para recorrer una lista con su indice [no funciona en conjuntos]
# for num in range(len(numeros)):
#     print(numeros[num])
    
# Forma correcta para recorrer una lista con su indice
for ele in enumerate(animales):
    print(ele)
    
# Mismo ejemplo que arriba pero desempaquetando la lista
for idx, val in enumerate(animales):
    print(f"{idx} = {val}")

# Agregar un else al for para que se ejecute al finalizar el recorrido de la lista
for item in animales:
    print("Recorriendo la lista")
else:
    print("Termino de recorrer la lista")

## Todo lo anterior funciona listas [], tuplas () y conjuntos {}

