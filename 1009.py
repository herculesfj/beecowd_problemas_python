# Leitura dos dados de entrada
nome_vendedor = input()
salario_fixo = float(input())
total_vendas = float(input())

# Cálculo da comissão (15% sobre o total de vendas)
comissao = total_vendas * 0.15

# Cálculo do total a receber
total_a_receber = salario_fixo + comissao

# Impressão do resultado no formato especificado
print(f"TOTAL = R$ {total_a_receber:.2f}")
