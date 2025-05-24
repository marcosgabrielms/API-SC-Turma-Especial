# Data/Hora de Início da questão:  D:24/05/2025 H:14:54:21 p.m
# Data/Hora do Término da questão: D:24/05/2025 H:15:12:10 p.m

def main():
    casos_totais = 0
    dias_validos = 0
    anterior = None

    while True:
        entrada = input("\nDigite o número de casos (ou digite 'fim' para encerrar): ").strip().lower()

        if entrada == 'fim':
            break
        try:
            casos = int(entrada)
            
            if casos < 0:
                print(f"Valor não computado (número negativo digitado)")
                continue

            if anterior is None:
                print("Primeiro dia registrado com sucesso")
            else:
                variacao = ((casos - anterior) / anterior) * 100 

                if abs(variacao) < 15:
                    print("\nEm Estabilidade")
                elif variacao >= 15:
                    print("\nEm Alta")
                else:
                    print("\nEm Queda")

            casos_totais += casos
            dias_validos += 1
            anterior = casos
        except ValueError:
            print("Valor não computado, entrada inválida")  

    print("\nFim do programa")
    print(f"Total de casos: {casos_totais}")
    if dias_validos > 0:
        media = casos_totais / dias_validos
        print(f"Média de casos por dia: {media}")
    else:
        print("Nenhum dia válido foi registrado")

if __name__ == '__main__':
    main()      