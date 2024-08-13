anonasc = int(input('Digite o ano que você nasceu : '))
idade = 2024 - anonasc
x = idade - 18
anoalist = anonasc + 18
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE')
elif idade < 18:
    x = (idade - 18) * -1
    print(f'Ainda faltam {x} anos para o seu alistamento')
    print(f'Você deverá se alistar em {anoalist} ')
elif idade > 18 and x == 1:
    print(f'Já se passou {x} ano desde o seu alistamento')
    print(f'Você se alistou em {anoalist} ')
elif idade > 18 and x > 1:
    print(f'Já se passaram {x} anos desde o seu alistamento')
    print(f'Você se alistou em {anoalist} ')