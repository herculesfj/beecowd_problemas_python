# Leitura do valor inteiro N
N = int(input())

# Cédulas disponíveis em ordem decrescente
cedulas = [100, 50, 20, 10, 5, 2, 1]

print(N)  # Imprime o valor lido N

# Itera sobre cada cédula para determinar a quantidade necessária
for cedula in cedulas:
    quantidade = N // cedula  # Divide N pela cédula para encontrar quantas vezes ela cabe em N
    print(f"{quantidade} nota(s) de R$ {cedula},00")
    N %= cedula  # Calcula o resto da divisão de N pela cédula, para prosseguir com os valores menores
