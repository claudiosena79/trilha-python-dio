# Remove o item referenciado assim como no discard.abs
# A diferença é que o discard não retorna erro caso o elemento
# referenciado não exista no conjunto, enquanto que o método Remove retorna erro nesse caso.
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.remove(0))  # 0
print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
