
n = int(input('Digite um número : '))
soma = n
if n % 2 == 0:
        for c in range(1, 6):
         n = int(input('Digite outro número : '))
         soma = soma + n
else:
    print('Esse número não é par, digite outro valor : ')

print(soma)

