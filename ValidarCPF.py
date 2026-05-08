cpf = '746.824.890-70'

numeros = ''.join([num for num in cpf if num.isdigit()])
numeros_lista = list(numeros)
lista_ints = [int(i) for i in numeros_lista]
nove_digitos = lista_ints[:9]

d = 0
temp = 0
print("[Validação de CPF]")
print('\n==Primeiro número==')
for n in nove_digitos:
    numero_cpf = (int(n)*(10-d))
    print(n, '=>', numero_cpf)

    temp = numero_cpf+temp
    soma = temp

    d+=1

print('Soma =>', soma)
mult = soma*10
print('Multiplicação =>', mult)
modulo = mult%11

if modulo > 9:
    modulo = 0
else:
    modulo = modulo

primeiro = modulo == lista_ints[-2]

if primeiro:
    print(f'Primeiro número CPF válido => {modulo}')

    print('\n==Segundo número==')
    nove_digitos.append(modulo)

    d = 0
    temp = 0
    for n in nove_digitos:
        numero_cpf = (int(n)*(11-d))
        print(n, '=>', numero_cpf)

        temp = numero_cpf+temp
        soma = temp

        d+=1
    
    print('Soma =>', soma)
    mult = soma*10
    print('Multiplicação =>', mult)
    modulo = mult%11

    if modulo > 9:
        modulo = 0
    else:
        modulo = modulo

    primeiro = modulo == lista_ints[-1]
    print(f'Segundo número CPF válido => {modulo}')

else:
    print(f'Primeiro número CPF inválido => {modulo}')
