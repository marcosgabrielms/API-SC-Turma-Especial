# Data/Hora de Início da questão:  D:24/05/2025 H:15:29:10 p.m
# Data/Hora do Término da questão: D:24/05/2025 H:15:40:06 p.m

def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

def main():
    print("====================================") 
    print("Cálculo do MDC (Máximo Divisor Comum)") 
    print("====================================") 
    while True:
        try:
            x = int(input("\nDigite o primeiro número sendo um inteiro positivo: "))
            y = int(input("Digite o segundo número sendo um inteiro positivo: "))

            if x > 0 and y > 0:
                break
            else:
                print("Ambos os números devem ser positivos")
        except ValueError:
            print("Entrada inválida, digite números inteiros")

    resultado =  mdc(x, y)
    print(f"O MDC de {x} e {y} é igual a {resultado}")

if __name__ == '__main__':
    main()