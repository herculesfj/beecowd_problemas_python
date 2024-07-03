# Leitura dos 5 valores inteiros da entrada
valores = []
for i in range(5):
    valores.append(int(input()))

# Inicialização dos contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

# Verificação de cada valor
for valor in valores:
    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1

# Impressão dos resultados
print(f"{pares} valor(es) par(es)")
print(f"{impares} valor(es) impar(es)")
print(f"{positivos} valor(es) positivo(s)")
print(f"{negativos} valor(es) negativo(s)")
