frutas = ["banana", "manzana", "ciruela", "pera", "naranja", "granada", "durazno"]
cadena = "Pablito clavo un clavito en la calva de un calvito"

for fruta in frutas:
    if fruta == 'manzana':
        continue
    print(fruta)
    
    if fruta == "pera":
        break

for letra in cadena:
    print(letra)

# For en una linea de codigo
numeros = [1, 2, 3, 4, 5]
dobles = [x * 2 for x in numeros]
print(dobles)
