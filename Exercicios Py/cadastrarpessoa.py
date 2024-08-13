print('-' * 20)
print('CADASTRE UMA PESSOA')
contidade = homi = muie = idade = 0


while True:
    print('-' * 20)
    idade = int(input('Idade : '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo : [M/F] ')).upper().strip()[0]
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if idade > 18:
        contidade += 1
    if sexo in 'Mm':
        homi += 1
    if sexo in 'Ff' and idade < 20:
        muie += 1
    if continuar in 'Nn':
        break
print('-' * 20)
print(f'Total de pessoas com mais de 18 anos : {contidade}')
print(f'Ao todo temos {homi} homens cadastrados')
print(f'E temos {muie} mulheres com menos de 20 anos.')


