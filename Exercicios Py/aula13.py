from datetime import date
vei = 0
novo = 0
atual = date.today().year
for c in range(0,7):
    anonascimento = int(input('INFORME O ANO DE NASCIMENTO : '))
    idade = atual - anonascimento
    if idade >= 18:
        vei += 1
    else:
        novo += 1
print(f'Há {novo} pessoas menores de idade.')
print(f'Há {vei} pessoas maiores de idade.')
