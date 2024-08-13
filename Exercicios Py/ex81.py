valores = []
cont = pos = 0
while True:
    cont += 1
    valores.append(int(input('Digite um valor : ')))
    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Opção inválida. Digite somente [S/N] : ')).upper().strip()[0]
        if continuar == 'N':
            break
    if continuar == 'N':
        break


print(f'{valores}')
while pos <= len(valores):
    if 5 in valores:
        pos5 = pos
    pos += 1
valores.sort(reverse = True)
print(f'Foram digiados {cont} valores.\n A lista de forma decrescente é de : {valores}')
if 5 in valores:
    print(f'Foi encontrado o valor 5 na poscição {pos5}')
else:
    print('O número 5 não foi encontrado naa lista!')

