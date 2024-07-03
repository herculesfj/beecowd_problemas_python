# Leitura dos valores de entrada
codigo, quantidade = map(int, input().split())

# Dicionário com os preços dos itens
tabela_precos = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}

# Verifica se o código está na tabela de preços
if codigo in tabela_precos:
    preco_unitario = tabela_precos[codigo]
    valor_total = preco_unitario * quantidade
    print(f"Total: R$ {valor_total:.2f}")
else:
    print("Código inválido.")
