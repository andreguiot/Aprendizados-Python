salario = int(input("Informe o valor do salário : "))
if salario > 1250:
    salario = (salario * 10/100) + salario
elif salario <= 1250:
    salario = (salario * 15/100) + salario
print('O reajuste total do salário informado é de : RS{:.2f}'.format(salario))