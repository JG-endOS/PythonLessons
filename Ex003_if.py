valor_1 = input('Digite um valor: ')
valor_2 = input('Digite um valor novamente: ')

if valor_1 == valor_2: 
    print('Os valores são iguais!')
elif valor_1 > valor_2:
    print(f'{valor_1} é maior que {valor_2}')
else:
    print(f'{valor_2} é maior que {valor_1}')