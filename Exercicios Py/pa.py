p1 = int(input('Primeiro termo : '))
r = int(input('Razão : '))
termo = p1
c = 1
n = 0
mais = 10
x = 0
while mais != 0:
    x = x + mais
    while c <= x:
        print('{} ->'.format(termo), end= ' ')
        c += 1
        termo = termo + r
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais ? '))
print('Progressão finalizada com {} termos mostrados.'.format(x))









