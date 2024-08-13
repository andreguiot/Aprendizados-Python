numero = []
continuar = ''
while True:
    numero.append(int(input('Digite um número : ')))
    continuar = str(input('Deseja continuar? [S/N] : ')).upper().strip()[0]
    if continuar not in "NS":
        continuar = str(input('Opção inválida! Informe somente [S/N]: ')).upper().strip()[0]
        if continuar in 'N':
            break
    if continuar == 'N':
        break
pos = 0
numimpar = []
numpar = []
while pos < len(numero):
    if numero[pos] % 2 == 0:
        numpar.append(numero[pos])
    else:
        numimpar.append(numero[pos])
    pos += 1
print(f'Todos valores da lista : {numero} ')
print(f'Somente ímpar : {numimpar}')
print(f'Somente par : {numpar}')

