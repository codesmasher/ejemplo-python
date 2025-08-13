lista = ["Enrique", "Sotelo", 45]
print(type(lista)) # Imprime el tipo de datos

tupla = ("CDMX", "México", "Hombre")
print(type(tupla)) # Imprime el tipo de datos

# desempaquetamiento de listas
nombre, apellido, edad = lista
print(f"Nombre: {nombre}")
print(f"Apellido: {apellido}")
print(f"Edad: {edad}")

# desempaquetamiento de tuplas
ciudad, pais, genero = tupla
print(f"Ciudad: {ciudad}")
print(f"País: {pais}")
print(f"Genero: {genero}")
