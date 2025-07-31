# Objeto list (array)
lista = ["Enrique Sotelo", "String", True, 1.85]
print(lista[0])

# Objeto tupla
tupla = ("Enrique Sotelo", "String", True, 1.85)
print(tupla[0])

# Las listas se pueden actualizar
lista[3] = 45

# Las tuplas no se pueden actualizar
tupla[3] = 45

# Objeto conjunto (set)
conjunto = {"Enrique Sotelo", "String", True, 1.85, "Enrique Sotelo"}
print(conjunto)
# No puede accederse desde el indice
# No se repiten valores

# Objeto diccionario (json)
diccionario = {
    "nombre": "Enrique Sotelo",
    "tag": "codesmasher",
    "bandera": True,
    "altura": 1.85
}
print(diccionario["nombre"])
