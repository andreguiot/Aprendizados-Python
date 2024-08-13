lisnome = []
lisnota1 = []
lisnota2 = []
lisgeral = [lisnome,lisnota1, lisnota2]
total = z = 0
while True:
    lisnome.append(str(input('Nome : ')))
    lisnota1.append(float(input('Nota 1 : ')))
    lisnota2.append(float(input('Nota 2 : ')))
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if continuar != 'S':
        break
print(lisgeral)
print('\n',lisgeral[0][0], lisgeral[1][0], lisgeral[2][0])
x = len(lisnome) + len(lisnota1) + len(lisnota2)
print(x)

i = 0
j = 0
k = 0
print('-=' * 30)
print('No. NOME       MA')
print('-' * 20)
for k in range(x):
    if k % 2 == 0:
        print(lisgeral[i][j])
        i += 1
        if i == 2:
            j += 1
            i = 0









