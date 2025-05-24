# Data/Hora de Início da questão:  D:24/05/2025 H:14:03:44 p.m
# Data/Hora do Término da questão: D:24/05/2025 H:14:32:48 p.m

def obter_inteiro(label):
    while True:
        entrada = input(label)
        try:
            numero =  int(entrada)
            return numero
        except ValueError:
            print(f'Valor inválido, digite um número inteiro')

def obter_inteiro_positivo(label):
    while True:
        numero = obter_inteiro(label)
        if numero >= 0:
            return numero
        else:
            print(f'O número deve ser positivo')

def obter_inteiro_negativo(label):
    while True:
        numero = obter_inteiro(label)
        if numero < 0:
            return numero
        else:
            print(f"O número deve ser negativo")

def obter_numero_minimo(label, minimo):
    while True:
        numero = obter_inteiro(label)
        if numero >= minimo:
            return numero
        else:
            print(f"O número deve ser no mínimo {minimo}")

def obter_numero_maximo(label, maximo):
    while True:
        numero = obter_inteiro(label)
        if numero >= maximo:
            return numero
        else:
            print(f"O número deve ser no máximo {maximo}")

def obter_numero_faixa(label, minimo, maximo):
    while True:
        if minimo > maximo:
            print(f"O mínimo {minimo} não pode ser maior que o valor máximo {maximo}")
            return
        
        numero = obter_inteiro(label)
        if minimo <= numero <= maximo:
            return numero
        else:
            print(f'O número deve estar entre mínimo: {minimo} e máximo: {maximo}')

def main():
    inteiro = obter_inteiro("Digite um número inteiro: ")
    inteiro_positivo = obter_inteiro_positivo("Digite um inteiro positivo: ")
    inteiro_negativo = obter_inteiro_negativo("Digite um inteiro negativo: ")
    numero_minimo = obter_numero_minimo("Digite um inteiro >= 10 (maior ou igual a 10): ", 10)
    numero_maximo = obter_numero_maximo("Digite um inteiro >= 20 (maior ou igual a 20): ", 20)
    faixa_numero = obter_numero_faixa("Digite entre 5 e 15: ", 5, 15)

    print(f"\nResultados:\nInteiro = {inteiro} \nInteiro Positivo = {inteiro_positivo} \nInteiro Negativo = {inteiro_negativo} \nNúmero Mínimo = {numero_minimo} \nNúmero Máximo = {numero_maximo} \nNúmero Faixa = {faixa_numero}")

if __name__ == '__main__':
    main()
