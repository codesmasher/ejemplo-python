cadena1 = "Hola Mundo"
cadena2 = "Python es genial"

resultado = dir(cadena1) # Obtiene los métodos disponibles para cadena1
largo = len(cadena1) # Obtiene la longitud de cadena1
print("Métodos disponibles en cadena1:", resultado)
print("Longitud de cadena1:", largo)

mayuscula = cadena1.upper()
minuscula = cadena2.lower()
primera_letra = cadena1.capitalize()
busqueda_find = cadena2.find("Python")
busqueda_index = cadena2.index("Python")

lista_cadena = cadena2.split(" ")# Divide la cadena en una lista de palabras
print("Lista de palabras en cadena2:", lista_cadena)

