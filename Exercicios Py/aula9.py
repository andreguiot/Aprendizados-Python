peso = float(input('Informe seu peso (Kg) : '))
altura = float(input('Informe sua altura (m) : '))
imc = peso / (altura ** 2)
print('Seu IMC é {:.1f}'.format(imc), end=' ')
if imc < 18.5:
    print('Abaixo do Peso')
if 18.5 < imc < 25:
    print('Peso ideal')