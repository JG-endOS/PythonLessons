nome = input("Digite seu nome: ")
tamanho_nome = len(nome)

i = 0
novo_nome = ''

while i < tamanho_nome:
    letra = nome[i]
    novo_nome += letra
    novo_nome += '*'
    i += 1

print(novo_nome)