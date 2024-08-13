preçoproduto = float(input('Informe o preço do produto : R$'))
escolha = int(input('[ 1 ] à vista (Dinheiro ou cheque) \n [ 2 ] à vista no cartão \n [ 3 ] em até 2x no cartão \n [ 4 ] 3x ou mais no cartão '))
if escolha == 1:
    x = ((10/100) * -preçoproduto) + preçoproduto
    print(f'10% de desconto, o valor total a ser pago é de : R${x}')
if escolha == 2:
    x = ((5 / 100) * -preçoproduto) + preçoproduto
    print(f'5% de desconto, o valor total a ser pago é de : R${x}')
if escolha == 3:
    print('2X NO CARTÃO \n Preço normal R${} \n em duas parcelas DE : {}'.format(preçoproduto, preçoproduto/2))
if escolha == 4:
    x = ((20 / 100) * preçoproduto) + preçoproduto
    print(f'20% de JUROS, o valor total a ser pago é de: R${x}')
