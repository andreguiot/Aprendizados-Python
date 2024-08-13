r = ''
cont = 0
aux = 0
media = 0
maior = menor = 0
while r != 'N':
    n = int(input('Digite um número : '))
    r = (input('Deseja continuar? [s/n]')).upper().strip()[0]
    cont = cont + 1
    aux = aux + n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('Acabou')
media = aux/cont
print('Você digitou {} números e a média entre eles foi de {:.2f}'.format(cont,media))
print('O menor número foi {} e o menor número foi {}'.format(menor, maior))
