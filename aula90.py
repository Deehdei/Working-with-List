lista_compras = []
while True:
    opcoes = str(input('Selecione uma opção\n[i]nserir [a]pagar [l]istar: '))

    if opcoes == 'i':
        itens = input('Digite o que deseja adicionar a lista: ')
        lista_compras.append(itens)

    elif opcoes == 'a':
        indice_str = input('Escolha o indice para apagar: ')

        try:
            indice = int(indice_str)
            del lista_compras[indice]
        except:
            print('Não foi possível apagar este indice')
    
    elif opcoes == 'l':
        if len(lista_compras) == 0:
            print('Nada para listar')    

        for indice, nome in enumerate(lista_compras):
            print(indice, nome)
    else:
        sair = input('Você deseja sair? [S]im ou [N]ão: ').upper().startswith('S')
        if sair == True:
            break