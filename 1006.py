# Leitura dos três valores com uma casa decimal
A = float(input())
B = float(input())
C = float(input())

# Pesos das notas
peso_A = 2
peso_B = 3
peso_C = 5

# Cálculo da média ponderada
MEDIA = (A * peso_A + B * peso_B + C * peso_C) / (peso_A + peso_B + peso_C)

# Impressão do resultado no formato especificado
print(f"MEDIA = {MEDIA:.1f}")
