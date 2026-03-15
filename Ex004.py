nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome == '' or idade == '': 
    print('Você não digitou seu nome ou idade!')

elif nome != '' and idade != '':
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome têm espaços')
    else:
        print('Seu nome não contém espaços')
        
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letea do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
    
