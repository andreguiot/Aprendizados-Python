def notas(nota):
    ntsdic = {}
    cont = 0
    for i, v in enumerate(nota):
        if nota[i] / 1 == nota[i]:
            cont += 1
    ntsdic["total"] = cont
    print(ntsdic)



nts = []
cont = 1
while True:
    nts.append(int(input(f'Digite a nota {cont} : ')))
    cont +=1
    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if continuar != 'S' and continuar != 'N':
        continuar = str(input('Valor inválido! Digite somente [S/N] ')).upper().strip()[0]
    elif continuar == 'N':
        sit = str(input('Deseja informar a situação? [S/N] ')).upper().strip()[0]
        if sit != 'S' and sit != 'N':
            sit = str(input('Valor inválido! Digite somente [S/N] ')).upper().strip()[0]
            if sit == 'N':
                break
        if sit == 'S':
            sit = True
            nts.append(sit)
            break
        if sit == 'N':
            break

notas(nts)
