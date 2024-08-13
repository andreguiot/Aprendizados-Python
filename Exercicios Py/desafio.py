cont = 0
maioridade = 0
maisvelho = "ninguém"
for c in range(1,5):
    print(f'----- {c} PESSOA ----')
    nome = str(input('Nome : '))
    idade = int(input('Idade : '))
    sexo = str(input(' [M/F] : ')).upper().strip()
    while sexo != "M" and sexo != "F":
        sexo = str(input(('Informe um sexo legítimo [M/F] :'))).upper().strip()
    if c == 1:
        n1 = nome
        id1 = idade
        sex1 = sexo
        if sexo == 'M':
            maisvelho = n1
            maioridade = idade
        if sexo == "F" and id1 < 20:
            cont += 1
    if c == 2:
        n2 = nome
        id2 = idade
        sex2 = sexo
        if id2 > maioridade and sexo == 'M':
            maisvelho = n2
            maioridade = id2
        if sexo == "F" and id2 < 20:
            cont += 1
    if c == 3:
        n3 = nome
        id3 = idade
        sex3 = sexo
        if id3 > maioridade and sexo == 'M':
            maisvelho = n3
            maioridade = id3
        if sexo == "F" and id3 < 20:
            cont += 1
    if c == 4 :
        n4 = nome
        id4 = idade
        sex4 = sexo
        if id4 > maioridade and sexo == 'M':
            maisvelho = n4
            maioridade = id4
        if sexo == "F" and id4 < 20:
            cont += 1
media = (id1 + id2 + id3 + id4) / 4
print('A média de idade do grupo é {} anos'.format(media))
print('O nome do homem mais velho é {} e tem {} anos '.format(maisvelho,maioridade))
print('Há {} mulheres com menos de 20 anos'.format(cont))





