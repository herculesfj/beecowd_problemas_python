from datetime import datetime

def ler_data_hora():
    try:
        entrada = input().strip().split()
        
        if len(entrada) != 2 or entrada[0] != "Dia":
            raise ValueError("Formato de entrada inválido")
        
        dia = int(entrada[1])
        entrada_hora = input().strip()
        hora, minuto, segundo = map(int, entrada_hora.split(':'))
        
        return datetime(2024, 4, dia, hora, minuto, segundo)
    
    except ValueError as e:
        print(f"Erro na leitura da entrada: {e}")
        raise

try:
    data_inicio = ler_data_hora()
    data_fim = ler_data_hora()

    diferenca = data_fim - data_inicio
    dias = diferenca.days
    segundos_totais = diferenca.seconds
    horas = segundos_totais // 3600
    segundos_totais %= 3600
    minutos = segundos_totais // 60
    segundos = segundos_totais % 60

    print(f"{dias} dia(s)")
    print(f"{horas} hora(s)")
    print(f"{minutos} minuto(s)")
    print(f"{segundos} segundo(s)")

except Exception as e:
    print(f"Erro inesperado: {e}")
