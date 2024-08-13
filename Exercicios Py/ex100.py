from random import randint
from time import sleep
def sorteia(lista):
    cont = 0
    while cont < 5:
        n = randint(1, 10)
        numeros.append(n)
        cont += 1
    print('Sorteando 5 valores da lista : ', end='')
    for v in numeros:
        print(f'{v}', end=' ')
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for v in numeros:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {numeros}, temos {soma}')


numeros = []
sorteia(numeros)
somaPar(numeros)



