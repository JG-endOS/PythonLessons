
calculadora = 1
while calculadora == 1:
    num1 = float(input('Digite um número: '))
    num2 = float(input('Digite outro número: '))
    calc = input('Digite um operador [+|-|*|/]: ')

    if calc == '+':
        soma = num1 + num2
        print(soma)

    elif calc == '-':
        sub = num1 - num2
        print(sub)

    elif calc == '*':
        mult = num1 * num2
        print(mult)

    elif calc == '/':
        div = num1 / num2
        print(div)

    else:
        print('Caractere inválido!')

    sla = 1
    while sla == 1:
        op = input('Gostaria de usar a calculadora novamente? [s/n]: ')

        if op == 's' or op == 'S':
            calculadora = 1
            sla = 0
        elif op == 'n' or op == 'N':
            sla = 0
            calculadora = 0
        else: 
            op = input('Escolha inválida => [s/n] <=: ')

print('Até depois!')
