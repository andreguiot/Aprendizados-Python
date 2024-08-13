anonasc = int(input('Ano de nascimento : '))
idade = 2024 - anonasc
print(f'O atleta tem {idade} anos')
if 0 < idade <= 9:
    print('Classificação : MIRIM')
elif 9 < idade <= 14:
    print('Classificação : INFANTIL')
elif 14 < idade <= 19:
    print('Classificação : JÚNIOR')
elif 19 < idade > 25:
    print('Classificação : MASTER')
