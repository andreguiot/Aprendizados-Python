
termos = float(input('Quantos termos você quer mostrar? '))
x = 0
y = 1

z = 0
cont = 3
print(x,y)
while cont <= termos:
    cont = cont + 1
    z = x + y
    print(z)
    x = y
    y = z



