listds = []
lispar = []
lisimpar = []
for v in range(0, 7):
    listds.append(int(input(f'Digite o {v+1} número : ')))
    if listds[v] % 2 == 0:
        lispar.append(listds[v])
    if listds[v] % 2 == 1:
        lisimpar.append(listds[v])
print('-=' * 30)
print(f'Os valores digitados foram : {listds}\nOs valores ímpares digitados foram : {lisimpar}')