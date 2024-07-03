# Leitura do valor inteiro N (tempo em segundos)
N = int(input())

# Calcula as horas, minutos e segundos
horas = N // 3600
N %= 3600
minutos = N // 60
segundos = N % 60

# Impressão do resultado no formato horas:minutos:segundos
print(f"{horas}:{minutos}:{segundos}")
