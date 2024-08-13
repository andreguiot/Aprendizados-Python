fut = {}
lista = []
while True:
    fut["jogador"] = str(input('Nome do Jogador : '))
    partidas = int(input(f'Partidas jogadas pelo jogador {fut["jogador"]}: '))
    gols = 0
    aux = []
    total = 0
    for n in range(partidas):
        gols = int(input(f'Gols na {n} Partida: '))
        aux.append(gols)
        fut["gols"] = aux
        total += gols
    fut["total"] = total
    lista.append(fut.copy())
    continuar = str(input('Deseja continuar? [S/N] : ')).upper().strip()[0]
    while True:
        if continuar not in 'SN':
            continuar = str(input('Valor Inválido! Digite somente [S/N] : ')).upper().strip()[0]
        if continuar == 'S':
            break
        if continuar == 'N':
            break
    if continuar == 'N':
        break
print(' cod     nome        gols            total')
print('-' * 60)
for i,v in enumerate(lista):
    print(f'  {i:3}       {v["jogador"]:3}          {v["gols"]}       {v["total"]:3}')
print('-' * 60)
while True:
    dados = int(input('Deseja mostrar dados de qual jogador? '))
    if dados == 999:
        break
    j = 0
    if dados >= len(lista):
        print(f"ERRO! Não existe jogador com o código {dados}")
    else:
        print(f' --Levantamento do jogador {lista[dados]["jogador"]}')
        for i, g in enumerate(lista[dados]["gols"]):
            print(f'Em {i} partidas fez {g} gols')



gols = aux[:]
print(lista)
print('-=' * 30)
