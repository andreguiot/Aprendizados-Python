decisao = 1
n1 = int(input('Primeiro valor : '))
n2 = int(input('Segundo valor : '))
while decisao != 5:
    decisao = int(input('''Opções : 
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa 
    '''))
    if decisao == 1:
        print('n1 + n2 = ', n1 + n2)
    if decisao == 2:
        print(n1 * n2)
    if decisao == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        else:
            print(f'{n2} é maior que {n1}')
    if decisao == 4:
        n1 = int(input('Digite novamente o valor : '))
        n2 = int(input('Digite novamente o segundo valor : '))
    if decisao > 1 and decisao > 5:
        print('Escreva um valo válido')



