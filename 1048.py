# Leitura do salário do funcionário
salario = float(input())

# Definição das faixas de reajuste e seus percentuais correspondentes
faixas = [
    (0, 400.00, 15),
    (400.01, 800.00, 12),
    (800.01, 1200.00, 10),
    (1200.01, 2000.00, 7),
    (2000.01, float('inf'), 4)
]

# Inicialização das variáveis para armazenar o novo salário e o percentual de reajuste
novo_salario = salario
percentual = 0

# Determinando a faixa de reajuste
for faixa in faixas:
    if salario <= faixa[1]:
        percentual = faixa[2]
        break

# Calculando o reajuste e o novo salário
reajuste = salario * (percentual / 100)
novo_salario = salario + reajuste

# Saída formatada conforme especificação
print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual} %")
