lista = list()
aux = list()
total = menorpeso = maiorpeso = 0
while True:
    aux.append(str(input('Nome : ')))
    aux.append(int(input('Peso [KG] : ')))
    if len(lista) == 0:           #Quando a lista ainda n foi preenchida.
        maiorpeso = menorpeso = aux[1]
    else:
        if aux[1] > maiorpeso:
            maiorpeso = aux[1]
        if aux[1] < menorpeso:
            menorpeso = aux[1]
    lista.append(aux[:])
    aux.clear()
    continuar = str(input('Deseja continuar? [S/N] : ')).upper().strip()[0]
    while continuar != 'N' and continuar != 'S':
        continuar = str(input('Inválido! Digite somente [S/N] : ')).upper().strip()[0]
        if continuar == 'N':
            break
    total += 1
    if continuar == 'N':
        break

print(f'Foram cadastradas um total de {total} pessoas.')
print(f'O maior peso foi {maiorpeso}. Peso de ', end = '')
for c in lista:
    nome = ''
    if c[1] == maiorpeso:
        nome = c[0]
    print(nome, end= ' ')



