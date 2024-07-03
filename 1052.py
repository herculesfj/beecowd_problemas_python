# Lista dos nomes dos meses em inglês
meses = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Leitura do número do mês
numero_mes = int(input())

# Verificação se o número do mês está dentro do intervalo válido (1 a 12)
if 1 <= numero_mes <= 12:
    # Imprimir o nome do mês correspondente ao número
    nome_mes = meses[numero_mes - 1]  # O índice na lista começa em 0, por isso subtraímos 1
    print(nome_mes)
