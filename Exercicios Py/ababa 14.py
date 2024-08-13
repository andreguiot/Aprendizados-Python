from random import randint
print('Estou pensando em um número de 0 a 10...')
aleatorio = randint(0,10)
numero = int(input('Pronto!\n Agora tente adivinhar o número : '))
while numero != aleatorio:
    if numero < aleatorio:
        numero = int(input('Mais... Tente mais uma vez. '))
    elif numero > aleatorio:
        numero = int(input('Menos... Tente mais uma vez. '))
print('Acertou! o número que escolhi foi {}"'.format(aleatorio))

