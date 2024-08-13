def fatorial(número, show = False):
    '''
    fatorial(n, show = False)
        -> Calcula o fatorial de um número.
        :param n: O número a ser calculado.
        :para show: (opcional) Mostrar ou não a conta.
        :return: O valor do Fatorial de um número n.
    '''
    lista = []
    cont = 0
    mult = 1
    while cont < número:
        if show == False:
            sub = número - 1
            x = número - cont

            mult *= x
            cont += 1
        if show == False:
            print(f'{mult}')
        if show == True:
            sub = número - 1
            x = número - cont
            mult *= x
            print(x, end='')
            if cont < x or cont > x and x != 1:
                print(f' x ', end='')
            cont += 1
        else:
            print(' = ', end='')
    if show == True:
        print(f' = {mult}')


# Programa Principal
fatorial(2, show=True)
