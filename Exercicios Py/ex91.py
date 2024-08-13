from random import randint
from time import sleep
from operator import itemgetter
dici = {}
ranking = {}
dici['jogador1'] = randint(1, 6)
dici['jogador2'] = randint(1, 6)
dici['jogador3'] = randint(1, 6)
dici['jogador4'] = randint(1, 6)
print('Valores sorteados : ')
for k, v in dici.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)
ranking = sorted(dici.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('== RANKING DOS JOGADORES ==')
for i,v in enumerate(ranking):
    print(f'{i+1} lugar : {v}')
