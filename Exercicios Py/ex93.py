fut = {}
fut["jogador"] = str(input('Nome do Jogador : '))
partidas = int(input(f'Partidas jogadas pelo jogador {fut["jogador"]}: '))
gols = 0
aux = []
total =0
for n in range(partidas):
    gols = int(input(f'Gols na {n} Partida: '))
    aux.append(gols)
    fut["gols"] = aux
    total += gols
gols = aux[:]
fut["total"] = total
print(fut)
print('-=' * 30)
for i, v in fut.items():
    print(f'O campo {i} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {fut["jogador"]} jogou {partidas} partidas.')
for i, v in enumerate(gols):
    print(f'    => Na partida {i} fez {v} gols. ')
print(f'Foi um total de {total} gols.')
print()