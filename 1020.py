# Leitura do valor inteiro idade_em_dias
idade_em_dias = int(input())

# Cálculo dos anos, meses e dias
anos = idade_em_dias // 365
idade_em_dias %= 365
meses = idade_em_dias // 30
dias = idade_em_dias % 30

# Impressão do resultado formatado
print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")
