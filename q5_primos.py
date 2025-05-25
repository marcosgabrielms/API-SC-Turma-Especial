# Data/Hora de Início da questão:  D:25/05/2025 H:11:03:57 a.m
# Data/Hora do Término da questão: D:25/05/2025 H:11:11:25 a.m


def eh_primo(n):
    if n < 2:
        return False

    divisor = 2
    while divisor < n:
        if n % divisor == 0:
            return False
        divisor = divisor + 1
    return True


def verificar_primos(atual, fim):
    if atual > fim:
        return

    if eh_primo(atual):
        print(str(atual) + " é primo")
    else:
        print(str(atual) + " não é primo")

    verificar_primos(atual + 1, fim)


def main():
    n = int(input("Digite o valor de N (início): "))
    m = int(input("Digite o valor de M (fim): "))
    verificar_primos(n, m)


if __name__ == '__main__':
    main()
