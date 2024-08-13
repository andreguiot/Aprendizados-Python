print('-' * 15)
print('MALVADO`S LOJA')
print('-' * 15)
totalgasto = cont = contpreco = menorpreco = maiorpreco = 0
caro = ''
while True:
    cont += 1
    nome = str(input('Insira o nome do produto : ')).upper().strip()
    preco = float(input('R$'))
    if cont == 1:
        barato = nome
        menorpreco = preco
    else:
        if preco < menorpreco:
            menorpreco = preco
            barato = nome
        if preco > maiorpreco:
            maiorpreco = preco
            caro = nome
    totalgasto += preco
    if preco > 1000:
        contpreco += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]')).upper().strip()
    if continuar in 'N':
        break
print('---------- FIM DO PROGRAMA ----------')
print(f'''O total da compra foi de R${totalgasto:.2f}
          Temos {contpreco} produtos custando mais de R$1000 
          O produto mais barato foi {barato} que custa R${menorpreco:.2f}
          Já o mais caro foi {caro}, custando R${maiorpreco:.2f} ''')