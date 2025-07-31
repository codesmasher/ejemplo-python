lista = ["hola", "mundo", "python", "es", "genial"]

resultado = dir(lista)  # Obtiene los métodos disponibles para lista
largo = len(lista)  # Obtiene la longitud de la lista
print("Métodos disponibles en lista:", resultado)
print("Longitud de la lista:", largo)

lista.append("nuevo elemento")  # Agrega un nuevo elemento al final de la lista
lista.insert(2, "insertado")  # Inserta un elemento en la posición 2
lista.extend(["otro", "elemento"])  # Agrega múltiples elementos al final de la lista
print("Lista después de append, insert y extend:", lista)

lista.pop(0)  # Elimina el primer elemento de la lista
lista.pop(-1)  # Elimina el último elemento de la lista

lista.remove("python")  # Elimina el primer elemento que coincide con "python"
lista.clear()  # Elimina todos los elementos de la lista
print("Lista después de pop, remove y clear:", lista)

lista = ["hola", "mundo", "python", "es", "genial"]
lista.sort()  # Ordena la lista alfabéticamente
lista.reverse()  # Invierte el orden de los elementos en la lista
print("Lista ordenada y luego invertida:", lista)
