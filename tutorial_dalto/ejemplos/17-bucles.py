#
diccionario = {
    "nombre": "Enrique",
    "apaterno": "Sotelo",
    "edad": 45
}

# Recorrer para obtener las claves
for key in diccionario:
    print(key)
    
# Recorrer para obtener las claves y el valor
for key, value in diccionario.items():
    print(f"{key} = {value}")
