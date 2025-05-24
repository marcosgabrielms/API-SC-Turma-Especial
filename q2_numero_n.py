# Data/Hora de Início da questão:  D:24/05/2025 H:14:35:16 p.m
# Data/Hora do Término da questão: D:24/05/2025 H:14:52:38 p.m

def main():
    N = int(input("Digite a quantidade de sequências: "))

    contador = 0
    soma_total = 0
    qtd_total = 0

    menor = None
    maior = None

    while contador < N:
        print(f"\nSequência {contador + 1} (Termine a sequência digitando 0): ")
        soma_pares = 0

        while True:
            num = int(input("Número: "))
            if num == 0:
                break

            if num % 2 == 0:
                soma_pares += num
            
            soma_total += num
            qtd_total += 1

            if menor is None or num < menor:
                menor = num
            if maior is None or num > maior:
                maior = num

        print(f"Soma dos pares da sequência {contador + 1}: {soma_pares}")
        contador += 1 

    media = soma_total / qtd_total
    print(f"Média de todos os números da sequência: {media:.2f}")
    print(f"Menor número: {menor}")
    print(f"Maior número: {maior}")

if __name__ == '__main__':
    main()