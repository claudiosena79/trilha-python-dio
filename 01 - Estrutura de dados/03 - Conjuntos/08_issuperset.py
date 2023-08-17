# Verifica se um conjunto contém todos os elementos de outro conjunto, 
# podendo ter mais elementos além desses.
# Um conjunto A é um superset de um conjunto B se todos os elementos de B também estiverem em A, 
# e possivelmente mais elementos adicionais estiverem em A.

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issuperset(conjunto_b)  # False
print(resultado)

resultado = conjunto_b.issuperset(conjunto_a)  # True
print(resultado)
