# Data/Hora de Início da questão:  D:25/05/2025 H:11:14:08 a.m
# Data/Hora do Término da questão: D:25/05/2025 H:11:28:17 a.m


def contar_divisores(n):
    contador = 1
    total = 0

    while contador <= n:
        if n % contador == 0:
            total = total + 1
        contador = contador + 1

    return total


def mostrar_divisores(a, b):
    atual = a
    while atual <= b:
        qtd = contar_divisores(atual)
        print(f"{atual} ({qtd})")
        atual = atual + 1



def main():
    a = int(input("Digite o valor de A (positivo): "))
    b = int(input("Digite o valor de B (positivo, pelo menos 11 unidades a mais que A): "))

    if a < 0 or b < 0:
        print("Erro: Os números devem ser positivos.")
    elif b - a < 11:
        print("Erro: B deve ser pelo menos 11 unidades maior que A.")
    else:
        mostrar_divisores(a, b)


if __name__ == '__main__':
    main()
