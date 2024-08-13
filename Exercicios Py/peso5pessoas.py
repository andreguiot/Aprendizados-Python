p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
peso = 0
for c in range(0, 5):
    if c == 0:
        p1 = float(input('Informe o peso da primeira pessoa : '))
        p1 = peso + p1
    if c == 1:
        p2= float(input('Informe o peso da segunda pessoa : '))
        p2 = peso + p2
    if c == 2:
        p3 = float(input('Informe o peso da terceira pessoa : '))
        p3 = peso + p3
    if c == 3:
        p4 = float(input('Informe o peso da quarta pessoa : '))
        p4 = peso + p4
    if c == 4:
        p5 = float(input('Informe o peso da quinta pessoa : '))
        p5 = peso + p5
print(p1,p2,p3,p4,p5)
if p1 > p2 and p1 > p3 and p1 > p4 and p1 > p5:
    print('O maior peso foi {}'.format(p1))
elif p2 > p1 and p2 > p3 and p2 > p4 and p2 > p5:
    print('O maior peso foi {}'.format(p2))
elif p3 > p2 and p3 > p1 and p3 > p4 and p3 > p5:
    print('O maior peso foi {}'.format(p3))
elif p4 > p2 and p4 > p3 and p4 > p1 and p4 > p5:
    print('O maior peso foi {}'.format(p4))
elif p5 > p2 and p5 > p3 and p5 > p4 and p5 > p1:
    print('O maior peso foi {}'.format(p5))

if p1 < p2 and p1 < p3 and p1 < p4 and p1 < p5:
    print('O menor peso foi {}'.format(p1))
elif p2 < p1 and p2 < p3 and p2 < p4 and p2 < p5:
    print('O menor peso foi {}'.format(p2))
elif p3 < p2 and p3 < p1 and p3 < p4 and p3 < p5:
    print('O menor peso foi {}'.format(p3))
elif p4 < p2 and p4 < p3 and p4 < p1 and p4 < p5:
    print('O menor peso foi {}'.format(p4))
elif p5 < p2 and p5 < p3 and p5 < p4 and p5 < p1:
    print('O menor peso foi {}'.format(p5))


