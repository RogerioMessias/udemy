lista_nomes = []

while True:
    nome = input('Digite o nome ou [S] para sair:  ')
    lista_nomes.append(nome)

    if nome == 's':
        break

for i in lista_nomes: 
    print(i)

print('Finalizando aplicação...')