from time import sleep
def contador(ini, fim ,pas):
    if pas < 0:
        pas += -1
    if p == 0 :
        p = 1
    print('-=' * 15)
    print(f'Contagem de {ini} até {fim} de {pas} em {pas}')
    if ini < fim:
        cont = ini
        while cont <= fim:
            print(cont, end = ' ')
            cont += pas
            sleep(0.1)
        print('FIM!')
        print('-=' * 15)
    else:
        cont = ini
        while cont >= fim:
            print(cont, end = ' ')
            cont -= pas
            sleep(0.1)
        print('FIM!')
        print('-=' * 15)
print(contador(1,10,1))
print(contador(10,0, 2))
print('Agora é a sua vez!')
i = int(input('Início : '))
f = int(input('Fim : '))
p = int(input('Passo : '))
contador(i,f,p)
