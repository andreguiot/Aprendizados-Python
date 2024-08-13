nome = str(input('Nome : '))
media = float(input('Média : '))
dici = {'Nome': nome, 'Media': media , 'Situação': 'reprovado'}
if media > 7:
    dici["Situação"] = 'aprovado'
for k, v in dici.items():
    print(f'{k} é igual a {v}')

