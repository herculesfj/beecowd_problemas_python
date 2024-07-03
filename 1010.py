# Leitura dos dados da primeira linha
codigo1, num_pecas1, valor_unit1 = input().split()
codigo1 = int(codigo1)
num_pecas1 = int(num_pecas1)
valor_unit1 = float(valor_unit1)

# Leitura dos dados da segunda linha
codigo2, num_pecas2, valor_unit2 = input().split()
codigo2 = int(codigo2)
num_pecas2 = int(num_pecas2)
valor_unit2 = float(valor_unit2)

# Cálculo do valor total a pagar
valor_total = (num_pecas1 * valor_unit1) + (num_pecas2 * valor_unit2)

# Impressão do resultado no formato especificado
print(f"VALOR A PAGAR: R$ {valor_total:.2f}")
