# Leitura dos três valores inteiros
valores = list(map(int, input().split()))

# Ordenação dos valores
valores_ordenados = sorted(valores)

# Impressão dos valores ordenados
for valor in valores_ordenados:
    print(valor)

# Impressão de uma linha em branco
print()

# Impressão dos valores na sequência original
for valor in valores:
    print(valor)
