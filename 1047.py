# Leitura dos valores de entrada
hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

# Cálculo da duração do jogo em horas e minutos
if hora_inicial == hora_final and minuto_inicial == minuto_final:
    duracao_horas = 24
    duracao_minutos = 0
else:
    if hora_final > hora_inicial or (hora_final == hora_inicial and minuto_final >= minuto_inicial):
        duracao_horas = hora_final - hora_inicial
        duracao_minutos = minuto_final - minuto_inicial
        if duracao_minutos < 0:
            duracao_minutos += 60
            duracao_horas -= 1
    else:
        duracao_horas = 24 - hora_inicial + hora_final
        duracao_minutos = minuto_final - minuto_inicial
        if duracao_minutos < 0:
            duracao_minutos += 60
            duracao_horas -= 1

# Saída formatada conforme especificação
print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")
