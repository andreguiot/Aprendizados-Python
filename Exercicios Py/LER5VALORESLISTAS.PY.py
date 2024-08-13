lista = []
maior = 0
menor = 0
posmenor = []
posmaior = []
for cont in range(0,5):
    lista.append(int(input(f'Digite um valor para posição {cont} : ')))
    if cont == 0:
        maior = menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]
for i, v in enumerate(lista):
    if v == maior:
        posmaior.append(i)
    if v == menor:
        posmenor.append(i)
print()



print(f' O maior valor foi {maior} na posição {posmaior}\n e o menor valor foi {menor} na posição {posmenor}.')