diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "lenguajes": ["Python", "JavaScript", "C++"]
}
print(dir(diccionario))

claves = diccionario.keys()
print("Claves del diccionario:", claves)

un_valor = diccionario.get("nombre")
print("Valor de la clave 'nombre':", un_valor)

un_valor_no_existente = diccionario.get("pais", "No existe")
print("Valor de la clave 'pais':", un_valor_no_existente)

diccionario.pop("ciudad")
print("Diccionario después de pop:", diccionario)

diccionario_iterable = diccionario.items()
print("Elementos del diccionario:", diccionario_iterable)

diccionario.clear()
print("Diccionario después de clear:", diccionario)
