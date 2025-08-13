# declarar un conjunto con set
conjunto = set(["dato1", "dato2"])
print(conjunto)

# metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato3", "dato4"])
conjunto2 = {conjunto1, "dato5"}
print(conjunto2)

# Teoria de conjuntos
conjunto3 = {1, 3, 5, 7}
conjunto4 = {1, 3, 7}

# Verificando conjuntos (subconjunto)
resultado1 = conjunto3.issubset(conjunto4)
# resultado1 = conjunto3 <= conjunto4 # Esta linea es equivalente a la de arriba
print(resultado1)

# Verificando conjuntos (superconjuntos)
resultado2 = conjunto3.issuperset(conjunto4)
# resultado2 = conjunto3 > conjunto4
print(resultado2)

# Verificar que exista por lo menos un elemento en común entre conjuntos
resultado3 = conjunto3.isdisjoint(conjunto4)
#
print(resultado3)
