continuar = cont = aux = 0
while True:
    continuar = int(input('Digite um valor (999 para parar) : '))
    if continuar == 999:
        break
    cont += 1
    aux += continuar
print(f'A soma dos {cont} valores foi {aux}')

