
calculadora = 1
while calculadora == 1:

    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    calc = input('Digite um operador [+|-|*|/]: ')

    num_validos = None

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        num_validos = True
    except:
        num_validos = None 

    if num_validos == None:
        print('Um ou ambos números são inválidos.')
        continue

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
