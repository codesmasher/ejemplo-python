# Creando una función simple
def saludar():
    print("Hola mundo")
    
saludar()

# Creando una función con parámetros
def saludar(nombre):
    print(f"Hola {nombre}")

saludar("Enrique")

# Creando una función con retorno
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)

# Creando una función con parámetros por defecto
def saludar(nombre = "amigo"):
    print(f"Hola {nombre}")
saludar()  # Usará el valor por defecto
saludar("Ana")  # Usará el valor proporcionado

# Creando una función con argumentos variables
def sumar_varios(*numeros):
    return sum(numeros)

resultado = sumar_varios(1, 2, 3, 4, 5)
print(resultado)
