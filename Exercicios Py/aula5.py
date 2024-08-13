valorcasa = float(input('Informe o valor da casa : '))
salario = float(input('Agora informe o seu salário : '))
anospagar = int(input('Informe em quantos anos deseja parcelar : '))
aux = (30/100 * salario)
prestmens = valorcasa/(anospagar*12)
if prestmens > aux :
    print('Não será possível parcelar a casa.')
else:
    print('Será possível realizar o pagamento.')
    print('\nVocê pagará {:.2f} reais por {} meses.'.format(prestmens,anospagar*12))