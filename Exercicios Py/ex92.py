valores = {}
valores["nome"] = str(input('Nome : '))
anonasc = int(input('Digite seu ano de nascimento : '))
ctps = int(input('Carteira de Trabalho (0 não tem) : '))
if ctps == 0:
    valores["ctps"] = ctps
    valores["ctps"] = 0
else:
    valores["contratação"] = int(input('Ano de Contratação : '))
    valores["salário"] = float(input('Salário : R$'))
idade = 2024 - anonasc
valores["idade"] = idade
print(valores)
for k, v in valores.items():
    print(f'O {k} tem o valor {v}')