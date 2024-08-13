p1 = int(input('Escreva o primeiro valor : '))
p2 = int(input('Escreva o segundo valor : '))
p3 = int(input('Escreva o terceiro valor : '))

if p1 > p2 and p1 > p3:
    print('O maior valor é {}' .format(p1))
if p2 > p1 and p2 > p3:
    print('O maior valor é {}' .format(p2))
if p3 > p1 and p3 > p2:
    print('O maior valor é {}'.format(p3))
menor = p1
if p2 < p1 and p2 < p3:
    menor = p2
if p3 < p1 and p3 < p2:
    menor = p3

print('O menor valor é {}'.format(menor))