n = 0
soma = 0
cont = 0
while n != 999:
    n = int(input('Digite um número [999 para parar] : '))
    if n != 999:
        cont = cont + 1
        soma = soma + n
print('Você digitou {} números e a soma entre eles foi {}'.format(cont,soma))