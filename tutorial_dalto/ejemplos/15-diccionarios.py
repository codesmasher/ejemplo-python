# Crear diccionario con dict()
diccionario = dict(nombre="Enrique", apaterno="Sotelo")

# Las listas no pueden ser claves en los diccionarios, para conjuntos hay que usar la función frozenset
diccionario = {frozenset(["Llave1", "Llave2"]): "Valor1"}

# Diccionario vacio
diccionario = dict.fromkeys(["Llave3", "Llave4", "Llave5"])
print(diccionario)
