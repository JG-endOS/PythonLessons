import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[I]nserir [A]pagar [L]istar: ')

    if opcao == 'i' or opcao == 'I':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a' or opcao == 'A':
        indice_str = input('Escolha o índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite um número int.')
        except IndexError:
            print('Índice não exite na lista.')
        except Exception:
            print('Erro desconhecido!.')

    elif opcao == 'l' or opcao == 'L':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha uma opção válida!')
    
