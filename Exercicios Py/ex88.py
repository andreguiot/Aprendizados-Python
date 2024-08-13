from random import randint

print('-' * 20)
print('JOGO NA MEGA SENA')
print('-' * 20)

n = int(input('Quantos jogos você quer que eu sorteie? '))

jogos = []

for _ in range(n):
    jogo = []
    while len(jogo) < 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()
    jogos.append(jogo)

print('-=' * 3, f'SORTEANDO {n} JOGOS', '-=' * 3)
for i, jogo in enumerate(jogos):
    print(f'Jogo {i + 1}: {jogo}')
