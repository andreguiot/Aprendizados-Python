def leiaInt(num):
    num = input(num)
    while True:
        if num.isnumeric() == False:
            print('Erro! Digite somente números inteiros')
            num = input('Digite um número : ')
        if num.isnumeric() == True:
            return num


n = leiaInt('Digite um número : ')
print(f'Você acabou de digitar o número {n}')