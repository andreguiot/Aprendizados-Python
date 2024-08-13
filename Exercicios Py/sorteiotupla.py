from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10) , randint(1, 10), randint(1, 10))
maiorvalor = menorvalor = 0
print(f'Os valores sorteados foram {n}')
if n[0] > maiorvalor:
     maiorvalor = n[0]
     print(f'O menor valor sorteado foi {menorvalor}')
else:
     menorvalor = n
