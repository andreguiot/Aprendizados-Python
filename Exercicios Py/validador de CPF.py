#Funções com if para encurtar o codigo 74682489070
def ifs():
    for i, v in enumerate(int_lista):
        if i == 0:
            r = v * 10
            cpf.append(r)
        if i == 1:
            r = v * 9
            cpf.append(r)
        if i == 2:
            r = v * 8
            cpf.append(r)
        if i == 3:
            r = v * 7
            cpf.append(r)
        if i == 4:
            r = v * 6
            cpf.append(r)
        if i == 5:
            r = v * 5
            cpf.append(r)
        if i == 6:
            r = v * 4
            cpf.append(r)
        if i == 7:
            r = v * 3
            cpf.append(r)
        if i == 8:
            r = v * 2
            cpf.append(r)


def segdig(x):
    for i, v in enumerate(int_lista):
        if i == 0:
            r = v * 11
            cpf.append(r)
        if i == 1:
            r = v * 10
            cpf.append(r)
        if i == 2:
            r = v * 9
            cpf.append(r)
        if i == 3:
            r = v * 8
            cpf.append(r)
        if i == 4:
            r = v * 7
            cpf.append(r)
        if i == 5:
            r = v * 6
            cpf.append(r)
        if i == 6:
            r = v * 5
            cpf.append(r)
        if i == 7:
            r = v * 4
            cpf.append(r)
        if i == 8:
            r = v * 3
            cpf.append(r)
        if i == 9:
            r = v * 2
            cpf.append(r)   #Para incluir o primeiro dígito
    return cpf


cpf = []
cont = c = 0
aux = []
int_lista = []
n = str(input(f'Digite o seu CPF : '))
for i in n:                           #For para separar cada item da lista de str em int.
    cpf.append(i)                     #Jogar cada num int separado dentro de uma lista.
for item in cpf:
    try:
        int_lista.append(int(item))
    except ValueError:
        print(f"'{item}' não é um número válido e será ignorado.")
cpf = []
cpf2 = int_lista
ifs()
s1 = sm = soma = 0
for v in cpf:
    soma += v
soma = soma * 10
_ = soma % 11
if _ > 9:
    _ = 0
else:
    _ = _
print(f'O primeiro dígito do CPF é : {_}')
cpf = []
segdig(cpf)
soma = segd = 0
for v in cpf:
    soma += v
soma = soma * 10
segd = soma % 11
if segd > 9:
    segd = 0
else:
    segd = segd
print(f'O segundo dígito do CPF é : {segd}')
if int_lista[9] == _ and int_lista[10] == segd:
    print(f'O cpf : {n} é válido')
else:
    print('CPF inválido!')