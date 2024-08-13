from random import randint
cont = -1
total = 0
escolhapc = ''
print('-=' * 13)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=' * 13)
while True:
    print('-' * 15)
    valor = int(input('Diga um valor : '))
    computador = randint(0, 10)
    paoui = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    print('-' * 20)
    x = randint(0, 1)
    cont += 1
    if paoui == 'P':
        escolhapc = 'ÍMPAR'
    else:
        escolhapc = 'PAR'
    soma = valor + computador
    if soma % 2 == 0 and paoui == 'P':
        print(f'Você jogou {valor} e o computador escolheu {computador}. Total de {soma}. \nVOCÊ VENCEU! O computador escolheu {escolhapc}')
        escolhapc = ''
        valor = 0
        paoui = ''
    if soma % 2 == 0 and paoui == 'I':
        print(f'Você jogou {valor} e o computador escolheu {computador}. Total de {soma}. \nVocê perdeu! O computador escolheu {escolhapc}')
        break
    if soma % 2 != 0 and paoui == 'P':
        print(f'Você jogou {valor} e o computador escolheu {computador}. Total de {soma}. \nVocê perdeu! O computador escolheu {escolhapc}')
        break
    if soma % 2 != 0 and paoui == 'I':
        print(f'Você jogou {valor} e o computador escolheu {computador}. Total de {soma}. \nVOCÊ VENCEU! O computador escolheu {escolhapc}')
    print('Vamos jogar Novamente !')
print('PERDEDOR')
print(f'Seu total de vitórias consecutivas foi de {cont}.')





