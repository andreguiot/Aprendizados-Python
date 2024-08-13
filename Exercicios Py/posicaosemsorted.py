valores = []
for v in range(0,5):
    n = int(input('Digite um valor : '))
    if v == 0 or n > valores[-1]: #para adicionar valores no inicio e no final da lista
        valores.append(n)
        print('Adicionado no final da lista.')
    else:
        pos = 0
        while pos < len(valores):           #while para PERCORRER O VETOR 'valores', e fazer comparações a cada vez que ele roda
                                            #(rodando a quantade de posições do vetor)
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Valor adicionado na posição {pos}')
                break
            pos += 1
print(f'Os valores digitados fora {valores}')



