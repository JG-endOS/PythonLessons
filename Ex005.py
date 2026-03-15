"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num = input('Digite um número inteiro: ')

if num.isdigit():
    num_int = int(num)

    if num_int % 2 == 0:
        print('O número digitado é par.')
    else:
        print('O número é ímpar.')

else: 
    print('Você não digitou um número inteiro!')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Digite a hora atual: ')


hora_int = int(hora)

if hora_int >= 0 and hora_int <= 11:
    print('Bom dia!')

elif hora_int >= 12 and hora_int <= 17:
    print('Boa tarde!')

else:
    print('Boa noite!')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')

if len(nome) <= 4:
    print('Seu nome é curto!')

elif len(nome) >= 5 and len(nome) <= 6:
    print('Seu nome é normal!')

else:
    print('Seu nome é longo!')