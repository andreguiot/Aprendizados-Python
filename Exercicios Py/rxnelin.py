lista = []
while True:
        opcao=  str(input('Selecione uma opção : \n[i]nserir  [a]pagar  [l]istar] ')).lower().strip()[0]
        while opcao != 'a' and opcao != 'i' and opcao != 'l':
            opcao = str(input('Erro! Selecione uma opção válida : \n[i]nserir  [a]pagar  [l]istar] ')).lower().strip()[0]
            if opcao == 'ail':
                break
        if opcao == 'i':
            valor_adicionado = str(input('Informe o valor a ser adicionado : '))
            lista.append(valor_adicionado)
            print('Valor adicionado!')
        if opcao == 'a':
            n = int(input('Escolha o índice que deseja apagar : '))
            i=0
            if 0 <= n < len(lista):
                print(lista[n], ' apagado.')
                del lista[n]
            else:
                print('Não foi possível apagar este índice.')
        if opcao == 'l':
            i = 0
            for i, v in enumerate(lista):
                print(f'O valor {v} está na posição {i}')





































