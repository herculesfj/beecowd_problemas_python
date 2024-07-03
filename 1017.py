# Leitura dos dados de entrada
tempo = int(input())
velocidade = int(input())

# Cálculo da distância percorrida
distancia = tempo * velocidade

# Cálculo da quantidade de combustível gasto
litros = distancia / 12

# Impressão do resultado com três casas decimais
print(f"{litros:.3f}")
