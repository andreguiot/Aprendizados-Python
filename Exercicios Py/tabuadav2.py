cont = -1
while True:
    print('-'*33)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*33)
    if n < 0:
        break
    while cont <= 9:
        cont += 1
        print(f'{n} X {cont} = ', n*cont)
    cont = -1
print('Programa de tabuada encerado. Volte sempre!')